
import os
import base64
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma


load_dotenv()




knowledge_base = "."




pdf_files = [
    "faq.pdf",
    "installation_guide.pdf",
    "router_user_manual.pdf",
    "troubleshooting_guide.pdf"
]




image_files = [
    "error_message.png",
    "network_diagram.png",
    "router_lights.png"
]




pdf_chunks = []

for filename in pdf_files:

    pdf_path = os.path.join(
        knowledge_base,
        filename
    )

    print(f"Reading PDF: {filename}")

    reader = PdfReader(pdf_path)

    pdf_text = "\n".join(
        page.extract_text() or ""
        for page in reader.pages
    )

   

    pdf_text = f"Source: {filename}\n{pdf_text}"

    pdf_chunks.append(pdf_text)



splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

all_pdf_chunks = []

for pdf_text in pdf_chunks:

    chunks = splitter.split_text(pdf_text)

    all_pdf_chunks.extend(chunks)




vision_model = ChatOpenAI(
    model="gpt-4o-mini"
)

image_texts = []


for filename in image_files:

    image_path = os.path.join(
        knowledge_base,
        filename
    )

    print(f"Reading image: {filename}")


  

    with open(image_path, "rb") as f:

        image_base64 = base64.b64encode(
            f.read()
        ).decode("utf-8")


    

    if filename.lower().endswith(".png"):

        image_type = "image/png"

    else:

        image_type = "image/jpeg"


    

    image_response = vision_model.invoke([
        {
            "role": "user",

            "content": [

                {
                    "type": "text",

                    "text": f"""
Analyze this image carefully for a Wi-Fi router
troubleshooting knowledge base.

Extract all useful technical information, including:

- Visible text
- Error messages
- Error codes
- LED colors
- LED blinking patterns
- Indicator meanings
- Router ports
- Port labels
- Network connections
- Diagram information
- Buttons
- Configuration information
- Troubleshooting instructions
- Any other information useful for diagnosing
  Wi-Fi or Internet connectivity problems.

Do not ignore small labels or numbers.

Image filename:
{filename}
"""
                },

                {
                    "type": "image_url",

                    "image_url": {
                        "url": f"data:{image_type};base64,{image_base64}"
                    }
                }

            ]
        }
    ])


    image_text = image_response.content


    

    image_text = (
        f"Source: {filename}\n"
        f"{image_text}"
    )


    image_texts.append(image_text)




documents = all_pdf_chunks + image_texts


print("\nKnowledge Base Loaded Successfully")

print(
    f"Total knowledge chunks: {len(documents)}"
)




embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)




vectorstore = Chroma.from_texts(
    documents,
    embedding=embeddings,
    collection_name="wifi_router_naive_rag"
)




query = input(
    "\nAsk a Wi-Fi router troubleshooting question: "
)




retrieved_docs = vectorstore.similarity_search(
    query,
    k=5
)




context = "\n\n".join(
    doc.page_content
    for doc in retrieved_docs
)




llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


prompt = f"""
You are a Wi-Fi Router Troubleshooting Assistant.

You have access to a knowledge base containing:

- Router user manual
- Installation guide
- Troubleshooting guide
- FAQ
- Router LED/indicator image
- Error message image
- Network diagram image

Answer the user's question using ONLY the
provided context.

IMPORTANT RULES:

- Carefully read all retrieved context.
- The information may be written using different words.
- Do not require exact keyword matches.
- Use information from both PDF documents and images
  when relevant.
- Do not add information that is not present in the context.
- Do not guess.
- Do not hallucinate troubleshooting steps.
- If the required information is not available in the
  retrieved context, clearly say:

  "The required information is not available
   in the knowledge base."

- Give clear and practical troubleshooting steps.
- Mention the source file whenever possible.

Format your answer as:

Problem Identified:
<problem>

Possible Cause:
<cause>

Recommended Steps:
1. <step>
2. <step>
3. <step>

Reference:
<source file>

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""


answer = llm.invoke(prompt)



print("\n")
print("=" * 60)

print("WI-FI ROUTER TROUBLESHOOTING ASSISTANT")

print("=" * 60)

print("\nAnswer:\n")

print(answer.content)

print("\n")
print("=" * 60)
