import json
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


def load_and_retrieve_docs(url, persist_directory):
    """
    Load and retrieve documents from a given URL.

    Args:
    url (str): The URL to load documents from.
    persist_directory (str): The directory to persist indexed documents.

    Returns:
    langchain_community.vectorstores.Chroma: The Chroma vector store.
    """
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict()
    )
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    vectorstore.persist()
    return vectorstore


def index_active_urls(json_file):
    """
    Index active URLs from a JSON file.

    Args:
    json_file (str): The path to the JSON file containing active URLs.
    """
    with open(json_file, 'r') as file:
        data = json.load(file)
    active_urls = data.get("Active", [])

    for url in active_urls:
        persist_directory = f"indexer/{url.split('//')[1].replace('/', '_')}"
        os.makedirs(persist_directory, exist_ok=True)
        load_and_retrieve_docs(url, persist_directory)


if __name__ == "__main__":
    index_active_urls('indexer/active_urls.json')
