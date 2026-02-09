---
title: How RAG Works
---

# Chapter 3 — How Retrieval-Augmented Generation Works

RAG combines **search engines + AI generation**.

Think of it as:

User Question → Search → Read → Answer

---

## Step 1 — Convert Text Into Embeddings

Computers don’t understand text directly.

We convert text into numbers called **embeddings**.

Embeddings capture meaning.

Example:
"cat" and "kitten" will have similar embeddings.

This allows AI to find similar text.

---

## Step 2 — Vector Database

We store embeddings inside a **vector database**.

We use:
👉 Qdrant

Vector databases allow us to:
• Search by meaning  
• Find similar text instantly  

This is like Google Search, but for meaning.

---

## Step 3 — Semantic Search

When user asks a question:
1. Question → converted to embedding
2. Database → finds similar content
3. Relevant text → returned

Now AI has the correct knowledge.

---

## Step 4 — AI Generates Answer

We give the LLM:

• The question  
• The retrieved text  

Then ask:

"Answer ONLY using this information"

This makes answers:
• Accurate  
• Context aware  
• Reliable  

Next we build the real system.
