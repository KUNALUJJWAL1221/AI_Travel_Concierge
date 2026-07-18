# 🌍 AI Travel Concierge

An intelligent **Retrieval-Augmented Generation (RAG)** application that allows users to upload travel guides (PDF or DOCX) and ask questions about their contents using **Google Gemini**, **LangChain**, and **FAISS**.

Instead of searching the internet, the assistant answers **only from the uploaded document**, making it useful for personalized travel guides, brochures, itineraries, and tourism documents.

---

## 🚀 Features

- 📄 Upload PDF or DOCX travel guides
- 🔍 Automatic document parsing and chunking
- 🧠 Semantic search using Google Gemini Embeddings
- ⚡ Fast retrieval with FAISS Vector Store
- 💬 Natural language Q&A powered by Gemini
- 📚 Answers are generated only from the uploaded document
- 🖥️ Clean Streamlit interface
- 💾 Chat history during the session

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | User Interface |
| LangChain | RAG Pipeline |
| Google Gemini | LLM |
| Gemini Embeddings | Vector Embeddings |
| FAISS | Vector Database |
| PyPDFLoader | PDF Parsing |
| Docx2txtLoader | DOCX Parsing |

---

## 📂 Project Structure

```
AI_Travel_Concierge/
│
├── assets/
├── data/
├── utils/
│
├── app.py              # Streamlit application
├── rag.py              # RAG pipeline
├── config.py           # Configuration
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI_Travel_Concierge.git

cd AI_Travel_Concierge
```

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` File

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

You can obtain a Gemini API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 📖 How It Works

### Step 1

Upload a travel guide in PDF or DOCX format.

↓

### Step 2

The document is:

- Loaded
- Split into smaller chunks
- Converted into embeddings
- Stored inside FAISS

↓

### Step 3

When a user asks a question:

- Relevant chunks are retrieved
- Context is sent to Gemini
- Gemini generates an answer only from the retrieved content

---

## 🧠 RAG Pipeline

```
User Upload
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
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
Gemini LLM
      │
      ▼
Answer
```

---

## 📸 Demo

Example questions:

```
Compare Goa and Kerala.

What are the best foods to try in Delhi?

Which destinations are suitable for adventure sports?

What is the best time to visit Rajasthan?

How many days are recommended for Kerala?
```

---

## 📌 Example Output

**Question**

> Compare Goa and Kerala.

**Answer**

> Goa offers relaxing beaches, Portuguese architecture, seafood, and water sports, while Kerala is known for its backwaters, tea plantations, wildlife sanctuaries, and houseboat experiences.

---

## 🔒 Limitations

- Supports only PDF and DOCX files.
- Answers are limited to the uploaded document.
- No internet search.
- Chat history resets after restarting the application.

---

## 🔮 Future Improvements

- Multiple document support
- Persistent vector database
- Conversation memory
- Source citations
- Hybrid Search
- Voice interaction
- Image understanding
- Multi-language support
- Travel itinerary generation
- Hotel and flight search integration

---

## 👨‍💻 Author

**Kunal Ujjwal**

AI Travel Concierge is a learning project demonstrating Retrieval-Augmented Generation (RAG) using Google's Gemini models with LangChain and FAISS.

---

## 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and improve it for educational or personal projects.

---

⭐ If you found this project useful, consider giving it a star on GitHub!