YourSniffr — AI Web Information Extractor

YourSniffr is an AI-powered web assistant built with Streamlit and LangChain.
It allows users to input multiple URLs and ask natural-language questions about the content on those webpages. The application automatically retrieves, processes, and embeds the information before generating accurate, context-based answers.

Features

Accepts up to three webpage URLs

Automatically loads and processes webpage content

Splits long text into smaller, meaningful chunks

Generates embeddings using OpenAI’s OpenAIEmbeddings

Stores and retrieves information using the FAISS vector database

Answers user questions with LangChain’s RetrievalQAWithSourcesChain

Provides a simple and interactive Streamlit interface

Technologies Used

Python 3.10+

Streamlit

LangChain

OpenAI API

FAISS

Installation and Setup
1. Clone the repository
git clone https://github.com/Sane1204/your-sniffr-.git
cd your-sniffr-

2. Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Set your OpenAI API key

You can set your key as an environment variable:

On Windows (PowerShell):

setx OPENAI_API_KEY "sk-your-api-key"


On macOS/Linux/WSL:

export OPENAI_API_KEY="sk-your-api-key"


Alternatively, you can create a .env file:

OPENAI_API_KEY=sk-your-api-key

Running the Application

Once everything is set up, start the Streamlit app with:

streamlit run main.py


Open the URL that appears in your terminal (usually http://localhost:8501) in your browser.

How It Works

Enter one to three URLs in the sidebar.

Click “Process URL” to fetch and embed their content.

Type a question in the input box.

The model searches for the most relevant text and returns an informed answer.

Example Use Cases

Summarizing long web articles or research papers

Extracting information from blogs or documentation pages

Creating a lightweight, AI-powered research assistant

Project Structure
your-sniffr-
│
├── main.py             
├── requirements.txt     
├── .gitignore          
└── README.md           

Future Improvements

Add document upload support (PDFs, text files)

Improve UI and feedback messages

Deploy the app to Streamlit Cloud or Hugging Face Spaces

Author

Developed by Sanskar Verma
GitHub: Sane1204
