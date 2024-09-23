import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

# from langchain_openai import OpenAIEmbeddings
# from langchain_pinecone import PineconeVectorStore
# import pyloader

loader = PyPDFLoader("data/a_mind_for_numbers.pdf")
document = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100)

texts = text_splitter.split_documents(document)
print(f"There is {len(texts)} chunks")