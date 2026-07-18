from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)

from config import (
    GOOGLE_API_KEY,
    CHAT_MODEL,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K,
)

# ----------------------------
# Gemini LLM
# ----------------------------

llm = ChatGoogleGenerativeAI(
    model=CHAT_MODEL,
    google_api_key=GOOGLE_API_KEY,
    temperature=0,
)

# ----------------------------
# Embeddings
# ----------------------------

embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    google_api_key=GOOGLE_API_KEY,
)

# ----------------------------
# Load Document
# ----------------------------

def load_document(file_path: str):

    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)

    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)

    else:
        raise ValueError("Only PDF and DOCX files are supported.")

    return loader.load()

# ----------------------------
# Split Documents
# ----------------------------

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    return splitter.split_documents(documents)

# ----------------------------
# Create Vector Store
# ----------------------------

def build_vector_store(file_path: str):

    documents = load_document(file_path)

    chunks = split_documents(documents)

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings,
    )

    return vectorstore

# ----------------------------
# Create Retriever
# ----------------------------

def get_retriever(vectorstore):

    return vectorstore.as_retriever(
        search_kwargs={
            "k": TOP_K
        }
    )

# ----------------------------
# Ask Question
# ----------------------------

def ask_question(retriever, question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are an AI Travel Concierge.

Answer ONLY using the context below.

If the answer isn't available,
say you couldn't find it.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content

