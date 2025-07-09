from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()


def create_qa_chain(vectorstore):
    llm = ChatOpenAI(temperature=0, model="gpt-4")
    return RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever()
    )
