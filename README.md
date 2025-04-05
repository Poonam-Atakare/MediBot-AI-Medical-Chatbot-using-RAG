# MediBot: AI Medical Chatbot using RAG

MediBot is an AI-powered medical chatbot leveraging **Retrieval Augmented Generation (RAG)** to provide responses based on medical documents. It uses **Mistral LLM**, **FAISS vector database**, and **LangChain** to efficiently process and retrieve information from a medical knowledge base.

## Features
- Load and process medical PDFs.
- Generate vector embeddings using **HuggingFace Embeddings**.
- Store and retrieve data using **FAISS**.
- Connect memory to **Mistral LLM** for query-based responses.
- **Streamlit-based UI** for user interaction.

## Project Structure
```
├── connect_memory_with_llm.py  # Connects FAISS with LLM
├── create_memory_for_llm.py     # Processes PDFs and creates vector embeddings
├── medibot.py                   # Streamlit-based chatbot UI
├── medical-chatbot-ppt.pdf      # Project overview presentation
```

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python installed, then run:
```sh
pip install -r requirements.txt
```

### 2. Set Up Hugging Face API Token
Create a `.env` file and add your **HF_TOKEN**:
```
HF_TOKEN=your_huggingface_api_token
```
Alternatively, export the token as an environment variable:
```sh
export HF_TOKEN=your_huggingface_api_token
```

### 3. Prepare Vector Database
Run the following script to load and process medical PDFs:
```sh
python create_memory_for_llm.py
```
This script will:
- Load medical PDFs.
- Split text into chunks.
- Generate vector embeddings.
- Store them in FAISS.

### 4. Connect LLM with Memory
Execute:
```sh
python connect_memory_with_llm.py
```
This script:
- Loads the **Mistral LLM**.
- Connects it with **FAISS**.
- Creates a query-response pipeline.

### 5. Run the Chatbot UI
Launch the Streamlit chatbot UI using:
```sh
streamlit run medibot.py
```
This will start an interactive web-based chatbot.

## Technologies Used
- **LangChain** - AI framework for LLM applications.
- **HuggingFace** - Machine learning model hub.
- **Mistral** - LLM for text generation.
- **FAISS** - Vector database for efficient search.
- **Streamlit** - Web-based chatbot interface.
- **Python** - Core programming language.

## Future Improvements
- Authentication for chatbot UI.
- User-uploaded documents for real-time embeddings.
- Support for multiple document sources.
- Unit testing for RAG pipeline.

## Contributing
Feel free to fork the repository, submit issues, and create pull requests!

---
Developed with ❤️ using AI and NLP!

