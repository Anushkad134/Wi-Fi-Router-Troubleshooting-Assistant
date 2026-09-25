# Wi-Fi Router Troubleshooting Assistant

A simple **Naïve RAG-based troubleshooting assistant** that uses router manuals, installation guides, FAQs, troubleshooting documents, and images as its knowledge base.

The application retrieves relevant information from the knowledge base and uses an LLM to provide a concise, grounded troubleshooting response.

## Features

- 📄 Supports multiple PDF documents
- 🖼️ Uses a **Vision Language Model (VLM)** to extract useful information from router images
- 🔎 Retrieves relevant information using vector similarity search
- 🧠 Uses an LLM to generate answers from retrieved context
- 🚫 Avoids adding information that is not present in the knowledge base
- 📚 Provides the source/reference document used for the answer

## Knowledge Base

The application uses:

- `faq.pdf`
- `installation_guide.pdf`
- `router_user_manual.pdf`
- `troubleshooting_guide.pdf`
- `error_message.png`
- `network_diagram.png`
- `router_lights.png`

## How It Works

```text
PDF Files ──────────────┐
                        │
                        ▼
                 Text Extraction
                        │
                        ▼
Images ──► VLM ──► Image Information
                        │
                        ▼
                 Text Chunking
                        │
                        ▼
              OpenAI Embeddings
                        │
                        ▼
                   ChromaDB
                        │
User Question ───────► Retrieval
                        │
                        ▼
                  Relevant Context
                        │
                        ▼
                  GPT-4o-mini
                        │
                        ▼
             Troubleshooting Answer
```

## Tech Stack

- **Python**
- **LangChain**
- **OpenAI GPT-4o-mini**
- **OpenAI Embeddings**
- **ChromaDB**
- **PyPDF**
- **RecursiveCharacterTextSplitter**
- **Vision Language Model (VLM)**

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd "Wi-Fi Router Troubleshooting Assistant"
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run the Application

Make sure all the PDF and image files are in the same folder as `app.py`.

Then run:

```bash
python app.py
```

Enter a troubleshooting question when prompted.

Example:

```text
Why does my Wi-Fi keep disconnecting even though the router is connected?
```

## Example Output

```text
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

## Project Structure

```text
Wi-Fi Router Troubleshooting Assistant/
│
├── app.py
├── requirements.txt
├── .env
│
├── faq.pdf
├── installation_guide.pdf
├── router_user_manual.pdf
├── troubleshooting_guide.pdf
│
├── error_message.png
├── network_diagram.png
└── router_lights.png
```

## Key Concept

This project demonstrates how **text-based and image-based knowledge can be combined in a RAG pipeline**. PDF content is extracted directly, while router images are processed using a Vision Language Model and converted into textual information before being added to the retrieval system.

The retrieved context is then passed to the language model so that the final response remains grounded in the available troubleshooting knowledge.

## Future Improvements

- Add a Streamlit interface
- Add persistent ChromaDB storage
- Support additional image formats
- Add conversation history
- Add metadata-based document filtering
- Improve retrieval with hybrid search
- Add evaluation for retrieval and answer quality

## Author

**Anushka Dabhade**

B.Tech CSE | AI/ML
