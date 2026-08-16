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

The application provides a conversational travel assistant that can understand uploaded travel guides, search the web, retrieve real-time weather information, search flights, generate basic travel itineraries, and save user searches locally using SQLite.
---

## 🚀 Project Overview

**AI Travel Concierge** is a Retrieval-Augmented Generation (RAG) application combined with a LangGraph-based AI agent.

The system intelligently routes user requests to the appropriate tool instead of relying only on the LLM's internal knowledge.

Depending on the user's request, the assistant can use:

- 📄 Uploaded travel guides
- 🌐 Web search
- 🌦 WeatherStack API
- ✈️ Google Flights through SerpApi
- 🗺️ Basic itinerary generation
- 💾 SQLite search history

The project is designed as an evolving AI Engineering project, with new capabilities being added incrementally.

---

# ✨ Features

## 📄 Document Intelligence

- Upload PDF travel guides
- Upload DOCX travel guides
- Automatic text extraction
- Intelligent document chunking
- Gemini embeddings
- FAISS vector search
- Semantic document retrieval
- Context-aware question answering

---

### 🤖 AI Agent
The application uses Google Gemini 2.5 Flash with LangGraph for intelligent tool routing.

Features include:

-Gemini-powered conversations
-LangGraph agent workflow
-Automatic tool calling
-Multiple specialized tools
-Natural-language travel requests
-Markdown-formatted responses
-Tool-based reasoning

The agent decides which tool should handle a request based on the user's question.

---

### 🔍 Search Tools

#### 📄 Document Search
Searches the uploaded travel guide using the FAISS-based RAG pipeline.

The agent prioritizes the uploaded document whenever the requested information may exist inside the guide.

Examples:

- Compare Goa and Kerala
- Best time to visit Kerala
- Beaches in Goa
- Famous places in Jaipur

---

#### 🌐 Web Search

Uses DuckDuckGo Search to retrieve recent or external information.

Useful for:

-Recent travel information
-Current attractions
-Travel news
-Information not available in the uploaded guide

Example:

-What are the latest tourist attractions in Jaipur?

---

#### 🌦 Weather Search

Uses the WeatherStack API for current weather information.

Example:

-Weather in Goa

Returns information such as:

-Temperature
-Weather description
-Humidity
-Wind speed

---

#### ✈️ Flight Search

Uses SerpApi Google Flights to search for available flights.

The flight tool supports:

-Departure airport
-Arrival airport
-Outbound date
-Airline
-Flight number
-Departure time
-Arrival time
-Flight duration
-Approximate fare

Example:

-Find flights from Delhi to Goa on 2026-08-20.

The agent uses IATA airport codes when calling the flight search tool.

---

#### 🗺️ Basic Itinerary Generation

The project now supports automatic generation of basic day-by-day travel itineraries.

The user can request an itinerary using natural language.

Examples:
-Create a 3-day itinerary for Goa.
-Make a 2-day itinerary for Jaipur.
-Plan a 5-day trip to Kerala.

The itinerary generator creates:

-Daily travel plans
-Morning activities
-Afternoon activities
-Evening activities
-Major attractions
-Travel flow between nearby locations
-Practical tips

The itinerary generator is intentionally kept as a basic planning feature at this stage. More advanced personalization and real-time itinerary optimization can be added in future iterations.

---

#### 💾 SQLite Search History
The application now includes a lightweight SQLite database for storing search interactions.

Saved information includes:

-User question
-Assistant response
-Timestamp

This provides persistent local storage for searches instead of keeping everything only in Streamlit session state.

Example database record:

```
ID | Question                    | Response                  | Created At
---|-----------------------------|---------------------------|---------------------
1  | Tell me about Goa.          | Goa is renowned for...    | 2026-08-13T18:32:09
2  | Best beaches in Goa?        | Information not found... | 2026-08-13T18:33:06
```

The database can also be tested independently using the database test script.

---

#### 🔐 Secure API Key Handling

API keys are handled through environment variables rather than being hard-coded into the application.

The project uses a .env file for local development.

Required API keys include:
```
GOOGLE_API_KEY=your_google_api_key_here
WEATHERSTACK_API_KEY=your_weatherstack_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
```

---

### 💻 User Interface

The application uses Streamlit to provide a conversational travel interface.

Current UI features include:

- 🌍 Travel assistant dashboard
- 💬 Conversational chat
- 📂 PDF/DOCX upload
- 💭 Chat history during the session
- 📋 Sidebar controls
- ⏳ Loading indicators
📄 Document processing feedback
🎨 Custom chat message styling

The UI will be further improved and polished during the upcoming development phase.
---

# 🏗 Project Architecture

```
                         User
                           │
                           ▼
                    ┌─────────────┐
                    │ Streamlit UI│
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ LangGraph   │
                    │ AI Agent    │
                    └──────┬──────┘
                           │
          ┌────────────────┼─────────────────┐
          │                │                 │
          ▼                ▼                 ▼
   Document Search     Web Search       Weather Tool
          │                │                 │
          ▼                ▼                 ▼
       FAISS          DuckDuckGo        WeatherStack
       RAG
          │
          │
          ├───────────────┐
          │               │
          ▼               ▼
   Flight Search    Itinerary Generator
          │               │
          ▼               ▼
       SerpApi        Gemini LLM
          │
          │
          └───────────────┐
                          ▼
                    Final Response
                          │
                          ▼
                    SQLite Database
                    Search History
```

---
### 🧠 RAG Architecture

The document-question-answering pipeline works as follows:

```
Travel Guide
     │
     ▼
Document Loader
     │
     ▼
Text Splitting
     │
     ▼
Gemini Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Retriever
     │
     ▼
Relevant Context
     │
     ▼
Gemini
     │
     ▼
Answer
```

---

# 🛠 Tech Stack

| Category               | Technology              |
| ---------------------- | ----------------------- |
| Language               | Python 3.13             |
| UI Framework           | Streamlit               |
| Agent Framework        | LangGraph               |
| LLM Framework          | LangChain               |
| LLM                    | Google Gemini 2.5 Flash |
| Embeddings             | Gemini Embedding-001    |
| Vector Database        | FAISS                   |
| Local Database         | SQLite                  |
| Web Search             | DuckDuckGo              |
| Weather API            | WeatherStack            |
| Flight Search          | SerpApi Google Flights  |
| Document Parsing       | PyPDF, Docx2txt         |
| Environment Management | python-dotenv           |


---

# 📂 Project Structure

```
AI_Travel_Concierge/
│
├── app.py                    # Streamlit application
├── graph.py                  # LangGraph workflow
├── agent.py                  # Agent interface
├── rag.py                    # RAG pipeline
├── tools.py                  # AI agent tools
├── config.py                 # Configuration and environment variables
├── database.py               # SQLite database operations
│
├── requirements.txt
├── README.md
├── .env            
├── .gitignore
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

Activate the virtual environment

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

SERPAPI_API_KEY=YOUR_SERPAPI_API_KEY
```

---

# ▶ Running the Project

Start Streamlit

```bash
streamlit run app.py
```

---

# 🧠 How It Works

## Step 1 — Upload a Travel Guide

The user uploads a PDF or DOCX travel guide through Streamlit.

↓

## Step 2 — Process the Document

The document is loaded and divided into smaller chunks.

↓

## Step 3 — Generate Embeddings

Gemini Embeddings convert the document chunks into vector representations.

↓

## Step 4 — Store Vectors

FAISS stores the generated embeddings for efficient semantic retrieval.

↓

## Step 5 — User Asks a Question

The user's question is sent to the LangGraph agent.

↓

## Step 6 — Agent Selects a Tool

Gemini determines which tool should handle the request.

Possible tools:

📄 Document Search
🌐 Web Search
🌦 Weather Search
✈️ Flight Search
🗺️ Itinerary Generation

↓

## Step 7 — Tool Executes

The selected tool retrieves or generates the required information.

↓

## Step 8 — Gemini Generates the Response

Gemini converts the tool result into a natural-language response.

↓

## Step 9 — Search Is Saved

Relevant search interactions can be stored locally in SQLite for persistence.

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

### ✈️ Flight Search
```
Find flights from Delhi to Goa on 2026-08-20.
```

```
What flights are available from DEL to GOI?
```

### 🗺️ Itinerary Generation
```
Create a 3-day itinerary for Goa.
```

```
Plan a 5-day trip to Kerala.
```

```
Make a 2-day itinerary for Jaipur.
```

---

# 📦 Week-wise Progress

## ✅ Week 1–2

-Project setup
-Streamlit UI
-Google Gemini integration
-RAG pipeline
-FAISS vector store
-PDF support
-DOCX support
-Semantic search
-Travel guide question answering

## ✅ Week 3–4

-LangGraph integration
-AI agent
-Tool calling
-Document search tool
-DuckDuckGo search tool
-WeatherStack tool
-Automatic tool routing
-Tool testing scripts
-Error handling improvements

## ✅ Week 5–6

### 💾 SQLite Database

-Added SQLite database support
-Added persistent search storage
-Added search retrieval
-Added database testing
-Stored questions, responses, and timestamps

### 🗺️ Basic Itinerary Generation

-Added generate_itinerary tool
-Added Gemini-powered itinerary generation
-Added day-by-day travel planning
-Added morning, afternoon, and evening activities
-Added practical travel tips
-Integrated itinerary generation with LangGraph tool calling
-Added itinerary testing

### ✈️ Flight Search

-Added SerpApi Google Flights integration
-Added departure and arrival airport support
-Added outbound date support
-Added airline and flight information
-Added flight duration and fare information
-Integrated flight search with LangGraph

### 🔐 Secure API Key Handling

-Added environment-variable based API configuration
-Added .env support using python-dotenv
-Added .env.example configuration template
-Added .env to .gitignore
-Removed the need for hard-coded API credentials
-Kept real API keys outside the GitHub repository

---

# 📈 Future Improvements
The next development phase will focus heavily on improving the user experience and overall application quality.

Planned improvements include:

- 🎨 UI/UX redesign
- 💬 Improved chat interface
- 🗂️ Better persistent chat history
- 🧭 More advanced itinerary personalization
- 🏨 Hotel search and booking APIs
- ✈️ Improved flight planning
- 🗺️ Google Maps integration
- 💰 Travel budget planning
- 🌦️ Weather-aware itinerary planning
- 🔐 Authentication
- 🎙️ Voice assistant
- 🖼️ Image-based travel search
- ☁️ Cloud deployment
- 🐳 Docker support

---

# 📷 Screenshots

Recommended screenshots for the project:

- 🏠 Home screen
- 📂 Travel guide upload
- 📄 Document question answering
- 🌐 Web search
- 🌦️ Weather search
- ✈️ Flight search
- 🗺️ Generated itinerary
- 💾 SQLite search history

---

# 🤝 Acknowledgements

This project uses the following technologies and services:

- Google Gemini
- LangChain
- LangGraph
- Streamlit
- FAISS
- SQLite
- DuckDuckGo
- WeatherStack
- SerpApi

---

# 📄 License

This project is developed for educational purposes as part of an AI Engineering learning program.

---

## 👨‍💻 Author

**Kunal Ujjwal**

Built with ❤️ using Python, LangGraph, Google Gemini, and Streamlit.
