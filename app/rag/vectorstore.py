from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


def store_embeddings(docs, persist_dir="chroma_db"):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(
        documents=docs, embedding=embeddings, persist_directory=persist_dir
    )

    return vectordb
