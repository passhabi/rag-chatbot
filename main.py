import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
import pypdf
#
# from langchain_text_splitters import CharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings
# from langchain_pinecone import PineconeVectorStore

loader = PyPDFLoader("data/a_mind_for_numbers.pdf")
document = loader.load()