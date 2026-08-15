import os
import tempfile

import streamlit as st

from rag import (
    build_vector_store,
    get_retriever,
)

from tools import set_retriever
from agent import ask_agent

from database import (
    initialize_database,
    save_search,
)

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="AI Travel Concierge",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)
# ----------------------------------
# Global CSS
# ----------------------------------

st.markdown(
    """
    <style>

    /* Main App */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    /* Chat message spacing */
    [data-testid="stChatMessage"] {
        margin-bottom: 18px;
        background: transparent !important;
    }

    /* --------------------------------
       USER MESSAGE
       -------------------------------- */

    [data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageAvatarUser"]
    ) {
        display: flex;
        flex-direction: row-reverse;
        align-items: flex-start;
    }

    [data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageAvatarUser"]
    )
    [data-testid="stChatMessageContent"] {
        background: #2563eb !important;
        color: white !important;

        padding: 12px 18px !important;

        border-radius: 18px !important;

        max-width: 70% !important;

        margin-left: auto !important;
        margin-right: 10px !important;

        width: fit-content !important;
    }

    /* --------------------------------
       ASSISTANT MESSAGE
       -------------------------------- */

    [data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageAvatarAssistant"]
    ) {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
    }

    [data-testid="stChatMessage"]:has(
        [data-testid="stChatMessageAvatarAssistant"]
    )
    [data-testid="stChatMessageContent"] {
        background: #2b2d35 !important;
        color: white !important;

        padding: 12px 18px !important;

        border-radius: 18px !important;

        max-width: 75% !important;

        margin-left: 10px !important;
        margin-right: auto !important;

        width: fit-content !important;
    }

    /* --------------------------------
       MARKDOWN INSIDE CHAT
       -------------------------------- */

    [data-testid="stChatMessageContent"] p {
        margin-top: 0.25rem;
        margin-bottom: 0.65rem;
    }

    [data-testid="stChatMessageContent"] ul,
    [data-testid="stChatMessageContent"] ol {
        margin-top: 0.4rem;
        margin-bottom: 0.7rem;
        padding-left: 1.4rem;
    }

    [data-testid="stChatMessageContent"] h1,
    [data-testid="stChatMessageContent"] h2,
    [data-testid="stChatMessageContent"] h3 {
        margin-top: 0.7rem;
        margin-bottom: 0.5rem;
    }

    [data-testid="stChatMessageContent"] hr {
        margin: 0.8rem 0;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

#----------------------------------
#Session State
#----------------------------------

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------------
# SQLite Database
# ----------------------------------

initialize_database()


# ----------------------------------
# Header
# ----------------------------------

st.title("🌍 AI Travel Concierge")

st.caption("Your AI-powered travel planning assistant")

st.markdown("---")

# Show Welcome Screen only before chatting
if len(st.session_state.chat_history) == 0:

    st.markdown(
        """
# 👋 Welcome!

### Where do you want to travel today?

Upload a travel guide or ask me anything about your destination.
"""
    )

    st.markdown("### 💡 Try asking")

    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "🏖️ Compare Goa and Kerala",
            use_container_width=True,
            disabled=True,
        )

        st.button(
            "🗺️ Plan a 5-day Rajasthan Trip",
            use_container_width=True,
            disabled=True,
        )

    with col2:
        st.button(
            "🌦️ Weather in Delhi",
            use_container_width=True,
            disabled=True,
        )

        st.button(
            "💰 Budget for Kashmir",
            use_container_width=True,
            disabled=True,
        )

    st.markdown("---")

# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    # -------------------------
    # App Logo
    # -------------------------
    st.title("🌍 AI Travel Concierge")

    st.caption("Your Personal Travel Assistant")

    st.divider()

    # -------------------------
    # Chat History (Placeholder)
    # -------------------------
    st.subheader("💬 Chat History")

    st.info("No previous conversations")

    st.divider()

    # -------------------------
    # Upload Guide
    # -------------------------
    st.subheader("📂 Upload Travel Guide")

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

            set_retriever(retriever)

        st.success("✅ Travel guide ready!")

    st.divider()

    # -------------------------
    # User Section (Placeholder)
    # -------------------------
    st.subheader("👤 User")

    st.caption("Guest User")

# ----------------------------------
# Display Chat History
# ----------------------------------

for message in st.session_state.chat_history:

    if message["role"] == "user":

        with st.chat_message("user", avatar="👤"):
            st.markdown(message["content"])

    else:

        with st.chat_message("assistant", avatar="🤖"):
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

    with st.spinner("🤖 Thinking..."):

        answer = ask_agent(prompt)

    # Save the search to SQLite
    save_search(
        prompt,
        answer,
    )

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )
    st.rerun()
