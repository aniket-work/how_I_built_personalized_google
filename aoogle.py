import gradio as gr
from dotenv import load_dotenv
from groq import Groq
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
import os

# Load environment variables from a .env file
load_dotenv()

# Retrieve the Groq API key from environment variables
client = Groq(api_key=os.getenv('GROQ_API_KEY'))
MODEL = 'llama3-70b-8192'

def load_vectorstore():
    vectorstore_directory = "indexer"  # Adjust this directory if needed
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma(persist_directory=vectorstore_directory, embedding_function=embeddings)
    return vectorstore


# Function to format documents
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Function that defines the RAG chain
def rag_chain(question):
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever()
    retrieved_docs = retriever.invoke(question)
    formatted_context = format_docs(retrieved_docs)
    formatted_prompt = f"Question: {question}\n\nContext: {formatted_context}"
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": formatted_prompt}],
        max_tokens=4096
    )
    return response.choices[0].message.content

iface = gr.Interface(
    fn=rag_chain,
    inputs="text",
    outputs=gr.Markdown(),
    title='<h1 style="font-size: 5em;">🔍 Aoogle</h1> <div style="font-size: 2em;"><b> Personalized Search Engine</b></div>',
    allow_flagging="never",
    submit_btn="Search"
)

iface.launch()
