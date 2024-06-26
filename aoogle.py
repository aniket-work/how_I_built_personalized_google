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
    """
    Loads the vector store for document retrieval.

    Returns:
    langchain_community.vectorstores.Chroma: Chroma vector store object.
    """
    vectorstore_directory = "indexer"  # Adjust this directory if needed
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma(persist_directory=vectorstore_directory, embedding_function=embeddings)
    return vectorstore


def format_docs(docs):
    """
    Formats retrieved documents.

    Args:
    docs (List[Document]): List of Document objects.

    Returns:
    str: Formatted document content.
    """
    return "\n\n".join(doc.page_content for doc in docs)


def rag_chain(question):
    """
    Generates response using the RAG (Retrieval-Augmented Generation) chain.

    Args:
    question (str): Input question.

    Returns:
    str: Response generated by the RAG chain.
    """
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
