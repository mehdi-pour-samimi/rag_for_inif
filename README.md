CSV-Based RAG Chatbot
A simple Retrieval-Augmented Generation (RAG) application built with Python, LangChain, OpenRouter, Hugging Face embeddings, and FAISS.

This project allows users to ask questions about information stored in a CSV file. It retrieves relevant information using semantic search and uses an LLM to generate answers based on the retrieved context.

🚀 Features
Load knowledge from a CSV file.
Support three CSV columns: category, question, and answer.
Generate text embeddings using Hugging Face.
Store and search vectors using FAISS.
Retrieve relevant documents based on semantic similarity.
Generate contextual answers using OpenRouter API.
Run locally using Python and uv.
🛠️ Technologies

Technology	Purpose
Python	Programming language
LangChain	RAG application framework
OpenRouter	LLM API
Hugging Face	Text embedding model
FAISS	Vector database
Pandas	CSV processing
uv	Python package and project management
📁 Project Structure

text
simple_rag/
│
├── knowledge.csv          # Knowledge source
├── main.py                # Main RAG application
├── pyproject.toml         # Project dependencies
├── uv.lock                # Dependency lock file
├── .env                   # API credentials
├── .env.example           # Example environment variables
├── .gitignore             # Git ignored files
└── README.md
📊 CSV Data Format
The application expects a CSV file with three columns:


category	question	answer

⚙️ Installation
1. Clone the repository

bash
git clone YOUR_REPOSITORY_URL
cd simple_rag
2. Install uv

bash
pip install uv
3. Create a virtual environment

bash
uv venv
Activate it:

Windows:


powershell
.venv\Scripts\activate
Linux / macOS:


bash
source .venv/bin/activate
4. Install dependencies
If the project contains pyproject.toml and uv.lock:


bash
uv sync
Otherwise, install the required packages:


bash
uv pip install langchain langchain-core langchain-community langchain-openrouter langchain-huggingface sentence-transformers faiss-cpu pandas python-dotenv
🔑 API Configuration
This project uses OpenRouter to access language models.

Create an account at https://openrouter.ai/
Generate an API key at https://openrouter.ai/settings/keys
Create a .env file in the project root.
Add:


env
OPENROUTER_API_KEY=your_openrouter_api_key
Never commit your actual API key to GitHub.

🤖 Embedding Model
The project uses:

sentence-transformers/all-MiniLM-L6-v2

This model converts text into numerical vectors for semantic similarity search.

The embedding model runs locally, so a separate embedding API key is not required.

🗄️ Vector Database
FAISS is used to store document embeddings and retrieve relevant information.

The vector database is saved locally in the faiss_index/ directory.

▶️ Usage
Run the application:


bash
uv run python main.py
Ask questions through the terminal:


text
===== CSV RAG CHATBOT =====

🔄 How RAG Works
The application follows these steps:

Load: Read CSV data using Pandas.
Prepare: Convert each CSV row into a LangChain document.
Embed: Generate embeddings using Hugging Face.
Store: Save document vectors in FAISS.
Retrieve: Find the most relevant documents using semantic similarity.
Generate: Send the retrieved context and user question to OpenRouter.
Answer: Return an answer based on the retrieved information.
🏗️ Architecture

text
          CSV File
              |
              v
        Pandas Loader
              |
              v
       LangChain Documents
              |
              v
      Hugging Face Embeddings
              |
              v
          FAISS Index
              |
              v
       User Question
              |
              v
      Semantic Retrieval
              |
              v
        Retrieved Context
              |
              v
         OpenRouter API
              |
              v
       Generated Answer

⚠️ Limitations
Answers depend on the quality of the CSV data.
Retrieval may return irrelevant documents.
LLM answers are not guaranteed to be factually correct.
OpenRouter free models may have usage limits or availability restrictions.
The initial embedding model download requires an internet connection.
📄 License
This project is available for educational and personal use. Add a specific open-source license if you intend to distribute it.

Built with Python, LangChain, and OpenRouter.

