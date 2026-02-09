---
title: Building the AI Book Assistant
---

# Chapter 4 — Building the AI Book Assistant

Now we combine everything into a real product.

Our system has 3 main parts.

---

## Part 1 — The Book Website (Docusaurus)

Docusaurus lets us publish our book as a website.

Why Docusaurus?

• Markdown based  
• Fast and modern  
• Easy GitHub deployment  
• Perfect for documentation  

Our book lives inside the `/docs` folder.

---

## Part 2 — The RAG Backend

We built a backend using:

• FastAPI → API server  
• OpenAI → language model  
• Qdrant → vector database  

This backend:
1. Reads the book
2. Converts chapters into embeddings
3. Stores them in Qdrant
4. Answers questions using RAG

---

## Part 3 — Embedded Chatbot

We embedded a chatbot directly inside the book.

Readers can:
• Ask questions about the whole book  
• Highlight text and ask about it  

This turns a normal book into an **interactive AI tutor**.

---

## What You Built

You didn’t just write a book.

You built:

• A documentation website  
• A vector search engine  
• A RAG AI assistant  
• A deployable AI product  

This project demonstrates real AI engineering skills.

Congratulations 
