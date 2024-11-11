from sentence_transformers import SentenceTransformer # type: ignore

# Load the embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    """
    Generate an embedding for the given text.
    
    Args:
        text (str): The text to embed.

    Returns:
        list: The embedding vector as a list of floats.
    """
    embedding = embedding_model.encode(text)
    return embedding
