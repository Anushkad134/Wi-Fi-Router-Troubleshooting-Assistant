// naïve RAG · troubleshooting agent

# Wi‑Fi Router Troubleshooting Assistant

A retrieval-augmented assistant that reads router manuals, FAQs, and diagnostic images, then answers connectivity problems with grounded, cited steps.

## overview

This is a simple **naïve RAG-based troubleshooting assistant** built on router manuals, installation guides, FAQs, troubleshooting documents, and images. It retrieves relevant context from a knowledge base and asks an LLM to produce a concise, grounded answer — one that never states anything the source documents don't support.

## features

📄

### Multi-document PDFs

Ingests manuals, guides, and FAQs as one knowledge base.

🖼️

### Vision-language extraction

A VLM reads router images and converts them into usable text.

🔎

### Vector similarity search

Retrieves the passages most relevant to the question asked.

🧠

### Grounded generation

The LLM answers strictly from retrieved context — no invention.

📚

### Source attribution

Every answer names the document it was drawn from.

🚫

### No hallucinated fixes

If it's not in the knowledge base, it's not in the answer.

## knowledge base

faq.pdftext

installation_guide.pdftext

router_user_manual.pdftext

troubleshooting_guide.pdftext

error_message.pngimage · VLM

network_diagram.pngimage · VLM

router_lights.pngimage · VLM

## how it works

01

#### Extract

Text is pulled directly from PDFs; router photos are read by a Vision Language Model and converted into descriptive text.

02

#### Chunk

All extracted text is split into overlapping chunks with a RecursiveCharacterTextSplitter.

03

#### Embed

Each chunk is embedded using OpenAI Embeddings and stored in ChromaDB.

04

#### Retrieve

A user's question is embedded and matched against the vector store for the most relevant chunks.

05

#### Answer

GPT‑4o‑mini generates a troubleshooting response grounded only in the retrieved context, with its source cited.

## tech stack

Python LangChain GPT‑4o‑mini OpenAI Embeddings ChromaDB PyPDF RecursiveCharacterTextSplitter Vision Language Model

## installation

clone the repository

\# git clone \<your-repository-url> cd "Wi-Fi Router Troubleshooting Assistant"

install dependencies

pip install -r requirements.txt

add your OpenAI key — create a .env file

OPENAI_API_KEY=your_api_key_here

## run

Make sure every PDF and image file sits in the same folder as `app.py`, then run:

python app.py

You'll be prompted for a troubleshooting question, for example:

\> Why does my Wi‑Fi keep disconnecting even though the router is connected?

## example output

```
Problem Identified:
The Wi-Fi connection is repeatedly disconnecting.

Possible Cause:
The troubleshooting information indicates that the issue may be related
to the router connection or configuration.

Recommended Steps:
1. Check the physical connections.
2. Check the router indicator lights.
3. Restart the router.
4. Verify the router configuration.

Reference:
troubleshooting_guide.pdf
```

## project structure

Wi-Fi Router Troubleshooting Assistant/ │ ├── app.py ├── requirements.txt ├── .env │ ├── faq.pdf ├── installation_guide.pdf ├── router_user_manual.pdf ├── troubleshooting_guide.pdf │ ├── error_message.png ├── network_diagram.png └── router_lights.png

## future improvements

- Add a Streamlit interface
- Add persistent ChromaDB storage
- Support additional image formats
- Add conversation history
- Add metadata-based document filtering
- Improve retrieval with hybrid search
- Add evaluation for retrieval and answer quality

**Anushka Dabhade** · B.Tech CSE, AI/ML naïve RAG · LangChain · ChromaDB
