import os
import streamlit as st
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.7, max_tokens=500)
st.title("YOUR SNIFFR")

st.sidebar.title("URLS")
urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
process_url_clicked = st.sidebar.button("Process URL")

file_path = "faiss_store"
main_placeholder = st.empty()

if process_url_clicked:
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("DATA LOADING...")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text splitting...")
    docs = text_splitter.split_documents(data)

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)

    main_placeholder.text("Vector started...")

    # Save vector store locally
    vector_store.save_local(file_path)
    time.sleep(2)

query = st.text_input("Question:")
if query:
    if os.path.exists(file_path):
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.load_local(file_path, embeddings, allow_dangerous_deserialization=True)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vector_store.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)

        st.header("Answer")
        st.write(result["answer"])
