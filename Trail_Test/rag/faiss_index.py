import faiss  # type: ignore
import numpy as np
from rag.embedding import get_embedding
from rag.text_splitter import split_text

class FaissIndex:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.data = []

    def load_data(self, file_path: str):
        with open(file_path, 'r') as f:
            lines = f.read().strip().split("\n\n")  # Split entries by blank lines

        # Parse Q&A pairs and chunk answers
        for entry in lines:
            question, answer = entry.split("\n")
            answer_chunks = split_text(answer, max_length=150, min_length=50)
            
            # Generate embeddings for each chunk and add to index
            for chunk in answer_chunks:
                embedding = get_embedding(chunk)
                self.index.add(np.array([embedding]))
                
                # Store metadata for each chunk
                self.data.append({"question": question, "chunk": chunk})

    #
    def search(self, query_embedding, k=1):
        distances, indices = self.index.search(np.array([query_embedding]), k)
        return [(self.data[i]["chunk"], distances[0][j]) for j, i in enumerate(indices[0])]

# Initialize FAISS index with embedding dimension
dimension = 384  # Assuming "all-MiniLM-L6-v2" with 384 dimensions
faiss_index = FaissIndex(dimension)
