import os

import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks.base import BaseCallbackHandler
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from streamlit.logger import get_logger
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from chains import (
    load_embedding_model,
    load_llm,
)

groq_api_key = 'your groq api key'
logger = get_logger(__name__)

def is_valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

def main():
        st.header("📄Chat using LangChain")

        # upload a your pdf file
        pdf = st.text_input("Enter URL")
        check = is_valid_url(pdf)
        print(check)
        if check is not None:
            pdf_reader = WebBaseLoader(pdf)#"https://docs.smith.langchain.com/"

            documents = pdf_reader.load()

            # langchain_textspliter
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=200, length_function=len
            )

            chunks = text_splitter.split_documents(documents=documents)
            st.write("Data is getting Processed")
            model_name = "BAAI/bge-large-en-v1.5"
            model_kwargs = {'device':'cpu'}
            encode_kwargs = {'normalize_embeddings':True}

            embedding_function = HuggingFaceBgeEmbeddings(
                model_name = model_name,
                model_kwargs = model_kwargs,
                encode_kwargs = encode_kwargs
            )
            # Store the chunks part in db (vector)
            vectorstore = FAISS.from_documents(
                                chunks,
                                embedding_function
                            )

            retriever = vectorstore.as_retriever()

            llm=ChatGroq(groq_api_key=groq_api_key,
            model_name="mixtral-8x7b-32768")

            # Accept user questions/query
            query = st.text_input("Ask questions about your Web URL")

            if query:
                # context = retriever.get_relevant_documents(query)
                prompt=ChatPromptTemplate.from_template(
                """
                Answer the questions based on the provided context only.
                Please provide the most accurate response based on the question
                <context>
                {context}
                <context>
                Questions:{input}
                """
                )
                document_chain = create_stuff_documents_chain(llm, prompt)
                retrieval_chain = create_retrieval_chain(retriever, document_chain)
                response=retrieval_chain.invoke({"input":query})
                st.write(response['answer'])
        else:
            try:
                st.write('Enter a valid URL')
            except:
                st.write('Enter a valid URL')

if __name__ == "__main__":
     main()



#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
