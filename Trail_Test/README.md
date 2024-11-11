# Simple Q/A Bot with RAG Technique

This project is a basic Q/A bot that answers questions using Retrieval-Augmented Generation (RAG) with a vector database for context retrieval.

## Project Structure
- `app/`: FastAPI application files
- `rag/`: RAG utility files for embedding and FAISS management
- `data/`: Text file for knowledge data

## Setup

1. Clone this repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI app:
    ```bash
    uvicorn app.main:app --reload
    ```
4. Enter query on this url: 
    ```"http://127.0.0.1:8000/docs#/default/get_answer_query_post"
    ```

## Knowledge Base Format
- Store Q&A pairs in `data/knowledge_base.txt`. Each entry should have a question on the first line and an answer on the second line, separated by a blank line.

Example format:
```plaintext
What is science?
Science is the systematic study of the structure and behavior of the physical and natural world through observation and experimentation.

What is physics?
Physics is a branch of science that studies matter, its motion, and behavior through space and time.
