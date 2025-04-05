import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Step 1: Define the path to the directory containing PDFs
DATA_PATH = "C:/Users/HPCND/OneDrive/Desktop/medi/data"

def load_pdf_files(data_path):
    if not os.path.exists(data_path):
        raise ValueError(f"Path does not exist: {data_path}")

    # Get all PDF files in the directory
    pdf_files = [f for f in os.listdir(data_path) if f.endswith(".pdf")]

    if not pdf_files:
        raise ValueError("No PDF files found in the directory.")

    documents = []
    for pdf_file in pdf_files:
        file_path = os.path.join(data_path, pdf_file)
        loader = PyMuPDFLoader(file_path)
        documents.extend(loader.load())

    return documents

documents = load_pdf_files(DATA_PATH)
#print("Total number of pages loaded:", len(documents))



# step 2: Create Chunks
def create_chunks(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,
                                                 chunk_overlap=50)
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks

text_chunks=create_chunks(extracted_data=documents)
#print("Length of Text Chunks: ", len(text_chunks))


# step 3: Create Vector Embeddings 
def get_embedding_model():
    embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

embedding_model=get_embedding_model()

# step 4: Store embeddings in FAISS
DB_FAISS_PATH="vectorstore/db_faiss"
db=FAISS.from_documents(text_chunks, embedding_model)
db.save_local(DB_FAISS_PATH)
