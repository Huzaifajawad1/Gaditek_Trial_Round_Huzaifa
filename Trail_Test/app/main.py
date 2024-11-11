from fastapi import FastAPI # type: ignore
from app.routes import router as query_router
from rag.faiss_index import faiss_index

app = FastAPI()

# Load data into FAISS on startup
@app.on_event("startup")
async def startup_event():
    faiss_index.load_data("data/knowledge_base.txt")

# Include the query router
app.include_router(query_router)
