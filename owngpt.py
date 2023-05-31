# -*- coding: utf-8 -*-
"""
Create ownChat web application streamlit and private gpt
@author: Avinash G
"""
from dotenv import load_dotenv
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
import os
from fastapi import FastAPI, UploadFile, File
from typing import List, Optional
import urllib.parse

load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')

from constants import CHROMA_SETTINGS

secret = ''
st.set_page_config(
    page_title="Own ChatGPT App",
    page_icon=":robot:"
)


def private_gpt_generate_msg(human_msg):
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    db = Chroma(persist_directory=persist_directory,collection_name=collection_name, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
    retriever = db.as_retriever()
    # Prepare the LLM
    callbacks = [StreamingStdOutCallbackHandler()]
    match model_type:
        case "LlamaCpp":
            llm = LlamaCpp(model_path=model_path, n_ctx=model_n_ctx, callbacks=callbacks, verbose=False)
        case "GPT4All":
            llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='gptj', callbacks=callbacks, verbose=False)
        case _default:
            print(f"Model {model_type} not supported!")
            exit;
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
    
    # Get the answer from the chain
    res = qa(human_msg)
    print(res)   
    answer, docs = res['result'], res['source_documents']
    return answer
	


st.header("Own ChatGPT App Private")

if 'Bot_msg' not in st.session_state:
    st.session_state['Bot_msg'] = []

if 'History_msg' not in st.session_state:
    st.session_state['History_msg'] = []


def get_text():
    input_text = st.text_input("Enter Your Text", key="input")
    return input_text 


user_input = get_text()

if user_input:
    st.session_state.History_msg.append(user_input)
    st.session_state.Bot_msg.append(Bot_generate_msg(user_input))

if st.session_state['Bot_msg']:
    for i in range(len(st.session_state['Bot_msg'])-1, -1, -1):
        st.markdown("BOT :- "+" "+st.session_state["Bot_msg"][i])
        st.markdown("HUMAN :- "+"\n"+st.session_state['History_msg'][i])
 
        