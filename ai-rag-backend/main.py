from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer
import uuid
import os
from openai import OpenAI

app = FastAPI()

# allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- OPENAI CLIENT ----------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------- EMBEDDING MODEL (FREE) ----------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------- QDRANT CLOUD ----------------
qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

# create collection if not exists
collections = [c.name for c in qdrant.get_collections().collections]

if "book" not in collections:
    qdrant.create_collection(
        collection_name="book",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

# ---------------- REQUEST MODELS ----------------
class Chapter(BaseModel):
    text: str

class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"status": "RAG API running ONLINE 🚀"}


# ---------------- UPLOAD BOOK TEXT ----------------
@app.post("/upload")
def upload(chapter: Chapter):

    embedding = model.encode(chapter.text).tolist()

    qdrant.upsert(
        collection_name="book",
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={"text": chapter.text}
            )
        ]
    )

    return {"message": "Text uploaded to CLOUD vector DB ✅"}


# ---------------- RAG CHAT ----------------
@app.post("/chat")
def chat(q: Question):
    try:
        # 1️⃣ embed question
        question_embedding = model.encode(q.question).tolist()

        # 2️⃣ search from Qdrant Cloud
        hits = qdrant.query_points(
            collection_name="book",
            query=question_embedding,
            limit=3
        ).points

        if len(hits) == 0:
            return {"answer": "No book data uploaded yet."}

        context = "\n\n".join([hit.payload["text"] for hit in hits])

        # 3️⃣ Ask LLM (OpenAI free tier)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Answer ONLY from the provided book context. If answer not present say: Not in book."
                },
                {
                    "role": "user",
                    "content": f"Context:\n{context}\n\nQuestion:{q.question}"
                }
            ]
        )

        return {"answer": completion.choices[0].message.content}

    except Exception as e:
        print("ERROR:", e)
        return {"answer": "Server error"}
