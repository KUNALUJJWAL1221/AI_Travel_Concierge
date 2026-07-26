import os
import tempfile

import streamlit as st

from rag import (
    build_vector_store,
    get_retriever,
)

from tools import set_retriever
from agent import ask_agent
# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="AI Travel Concierge",
    page_icon="🌍",
    layout="wide",
)

# ----------------------------------
# Session State
# ----------------------------------

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------------
# Header
# ----------------------------------

st.title("🌍 AI Travel Concierge")

st.markdown(
    """
Ask questions about your uploaded travel guide.

### Supported files
- PDF
- DOCX

Powered by **Gemini + LangGraph + FAISS + DuckDuckGo + WeatherStack**
"""
)

# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.header("📂 Upload Travel Guide")

    uploaded_file = st.file_uploader(
        "Choose a PDF or DOCX",
        type=["pdf", "docx"],
    )

    if uploaded_file is not None:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=os.path.splitext(uploaded_file.name)[1],
        ) as tmp_file:

            tmp_file.write(uploaded_file.read())
            temp_path = tmp_file.name

        with st.spinner("Building Vector Database..."):

            vectorstore = build_vector_store(temp_path)
            retriever = get_retriever(vectorstore)
            st.session_state.retriever = retriever

            # Make the retriever available to LangGraph
            set_retriever(retriever)

        st.success("✅ Travel guide processed successfully!")

# ----------------------------------
# Display Chat History
# ----------------------------------

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------
# Chat Input
# ----------------------------------

prompt = st.chat_input(
    "Ask anything about your travel guide..."
)

if prompt:

    if st.session_state.retriever is None:
        st.warning("Please upload a travel guide first.")
        st.stop()

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = ask_agent(prompt)

        st.markdown(answer)

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )
