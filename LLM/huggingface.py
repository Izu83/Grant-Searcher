from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain.prompts import PromptTemplate

from langchain.chains import RetrievalQA

from langchain_huggingface import HuggingFaceEmbeddings
import os
import numpy as np

## Read the PDFs from the folder

loader = PyPDFDirectoryLoader("./Elements")

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500, 
    chunk_overlap=300
)


final_documents=text_splitter.split_documents(documents)

## Embedding Using Hugging Face
huggingface_embeddings=HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs = {'device':'cpu'},
    encode_kwargs = {'normalize_embeddings':True}

)

# print(np.array(huggingface_embeddings.embed_query(final_documents[0].page_content)))
# print(np.array(huggingface_embeddings.embed_query(final_documents[0].page_content)).shape)

## VectorStore Creation
vectorstore=FAISS.from_documents(final_documents[:120],huggingface_embeddings)

## Query using Similarity Search
query = "ENTRY INTO FORCE"
relevant_documents = vectorstore.max_marginal_relevance_search(query, k=3)


print(relevant_documents[0].page_content)

retriever=vectorstore.as_retriever(search_type="similarity",search_kwargs={"k":3})

os.environ["HUGGING_FACE_API"] = "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"

