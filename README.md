# Information Retrieval from Multiple PDFs with PaLM 2

A Streamlit application that leverages Google’s PaLM 2 model, LangChain, and FAISS to perform efficient, conversational information retrieval across multiple PDF documents.

---

## Features

- **Multi‐PDF Ingestion**  
  Upload and index multiple PDF files simultaneously.  
- **Conversational Q&A**  
  Ask natural-language questions and receive precise answers drawn from your documents.  
- **Fast Similarity Search**  
  Uses FAISS vector store for sub-second retrieval of relevant passages.  
- **Scalable & Extensible**  
  Built on LangChain—easily swap in other LLMs or vector backends.

---

## Prerequisites

- **Python 3.8**  
- A valid Google API key with PaLM 2 access  
- [Conda](https://docs.conda.io/en/latest/) (optional, but recommended)  

---

## Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
   cd <YOUR_REPO>


2. **Create and activate a Conda environment**
    ```bash
    conda create -n llmapp python=3.8 -y
    conda activate llmapp


3. **Install dependencies**
    ```bash
    pip install -r requirements.txt


4. **Configure your environment**
    Create a file named .env in the project root and add your API key:
    ```ini
    GOOGLE_API_KEY="your_google_api_key_here"


5. **Run the app**
    ```bash
    streamlit run app.py


6. **Access in your browser**
    Open http://localhost:8501 to start querying your PDFs.


### Techstack Used:

- Python
- LangChain
- Streamlit 
- PaLM2
- FAISS
