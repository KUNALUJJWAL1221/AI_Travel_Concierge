# 🌍 AI Travel Concierge

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent_Framework-00A67E?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_2.5_Flash-4285F4?style=for-the-badge&logo=google)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Database-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-success?style=for-the-badge)

![GitHub stars](https://img.shields.io/github/stars/KUNALUJJWAL1221/AI_Travel_Concierge?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/KUNALUJJWAL1221/AI_Travel_Concierge?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/KUNALUJJWAL1221/AI_Travel_Concierge?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/KUNALUJJWAL1221/AI_Travel_Concierge?style=for-the-badge)

An intelligent **AI-powered Travel Assistant** built with **LangGraph, LangChain, Google Gemini, FAISS, and Streamlit**.

The application allows users to upload travel guides (PDF/DOCX), ask questions about the uploaded document, search the web for the latest travel information, and retrieve real-time weather updates—all through a single conversational interface.

---

## 🚀 Project Overview

AI Travel Concierge is a Retrieval-Augmented Generation (RAG) application that combines:

- 📄 Document Question Answering
- 🌐 Live Web Search
- 🌦 Real-Time Weather Information
- 🤖 Tool Calling using LangGraph
- 💬 Conversational Chat Interface

Instead of relying only on an LLM's internal knowledge, the assistant intelligently decides whether to answer from:

- the uploaded travel guide,
- the internet,
- or the WeatherStack API.

---

# ✨ Features

### 📄 Document Intelligence
- Upload PDF travel guides
- Upload DOCX travel guides
- Automatic text extraction
- Intelligent chunking
- Vector embeddings
- Semantic document search
- Context-aware question answering

---

### 🤖 AI Agent

- Google Gemini 2.5 Flash
- LangGraph Agent
- Automatic Tool Calling
- Multi-tool reasoning
- Natural language conversations

---

### 🔍 Search Tools

#### 📄 Document Search
Answers questions using only the uploaded travel guide.

Examples:

- Compare Goa and Kerala
- Best time to visit Kerala
- Beaches in Goa
- Famous places in Jaipur

---

#### 🌐 Web Search

Uses DuckDuckGo Search for recent information.

Examples:

- Latest tourist attractions in Jaipur
- Top restaurants in Delhi
- Recent travel news

---

#### 🌦 Weather Search

Uses WeatherStack API.

Examples:

- Weather in Delhi
- Weather in Mumbai
- Weather in Goa

---

### 💻 User Interface

- Streamlit Chat Interface
- Chat History
- File Upload
- Responsive Layout
- Sidebar Controls
- Loading Indicators

---

# 🏗 Project Architecture

```
                    User
                      │
                      ▼
               Streamlit UI
                      │
                      ▼
               LangGraph Agent
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
   Document Tool   Web Search   Weather Tool
          │            │             │
          ▼            ▼             ▼
      FAISS RAG    DuckDuckGo   WeatherStack
          │
          ▼
   Gemini Embeddings
          │
          ▼
 Google Gemini 2.5 Flash
```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Framework | Streamlit |
| Agent Framework | LangGraph |
| LLM Framework | LangChain |
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Gemini Embedding-001 |
| Vector Database | FAISS |
| Web Search | DuckDuckGo |
| Weather API | WeatherStack |
| Document Parsing | PyPDF, Docx2txt |

---

# 📂 Project Structure

```
AI_Travel_Concierge/

│
├── app.py                 # Streamlit application
├── graph.py               # LangGraph workflow
├── agent.py               # Agent interface
├── rag.py                 # RAG pipeline
├── tools.py               # Tool definitions
├── config.py              # Configuration
│
├── requirements.txt
├── README.md
├── .env
│
└── Travel Guides/
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI_Travel_Concierge.git

cd AI_Travel_Concierge
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

WEATHERSTACK_API_KEY=YOUR_WEATHERSTACK_API_KEY
```

---

# ▶ Running the Project

Start Streamlit

```bash
streamlit run app.py
```

---

# 🧠 How It Works

## Step 1

User uploads a travel guide.

↓

## Step 2

The document is loaded.

↓

## Step 3

The document is split into chunks.

↓

## Step 4

Gemini Embeddings generate vector representations.

↓

## Step 5

FAISS stores the vectors.

↓

## Step 6

The LangGraph Agent receives the user's question.

↓

## Step 7

The agent automatically decides which tool to use.

Possible tools:

- 📄 Document Search
- 🌐 Web Search
- 🌦 Weather Tool

↓

## Step 8

The tool returns information.

↓

## Step 9

Gemini generates the final response.

---

# 💬 Example Questions

### Document Search

```
Compare Goa and Kerala.
```

```
Best time to visit Kerala.
```

```
Tell me about Jaipur.
```

---

### Weather

```
Weather in Delhi
```

```
Weather in Goa
```

```
Weather in Mumbai
```

---

### Web Search

```
Latest tourist attractions in Jaipur
```

```
Top restaurants in Goa
```

```
Travel news in India
```

---

# 📦 Week-wise Progress

## ✅ Week 1–2

- Project Setup
- Streamlit UI
- Google Gemini Integration
- RAG Pipeline
- FAISS Vector Store
- PDF Support
- DOCX Support
- Semantic Search
- Travel Guide Chat

---

## ✅ Week 3–4

- LangGraph Integration
- AI Agent
- Tool Calling
- Document Search Tool
- DuckDuckGo Search Tool
- WeatherStack Tool
- Automatic Tool Routing
- Tool Testing Scripts
- Error Handling Improvements

---

# 📈 Future Improvements

- Conversation Memory
- Persistent FAISS Database
- Hotel Booking APIs
- Flight Booking APIs
- Google Maps Integration
- Voice Assistant
- Image-based Travel Search
- Authentication
- Deployment on Streamlit Cloud
- Docker Support

---

# 📷 Screenshots

Add screenshots of:

- Home Screen
- Uploading Document
- Document Search
- Web Search
- Weather Search

---

# 🤝 Acknowledgements

- Google Gemini
- LangChain
- LangGraph
- Streamlit
- FAISS
- DuckDuckGo
- WeatherStack

---

# 📄 License

This project is developed for educational purposes as part of an AI Engineering learning program.

---

## 👨‍💻 Author

**Kunal Ujjwal**

Built with ❤️ using Python, LangGraph, Google Gemini, and Streamlit.
