from openai import OpenAI  # type: ignore
from rag.faiss_index import faiss_index
from rag.embedding import get_embedding
import json

client=OpenAI()

def generate_response(query: str):
    # Embed user query
    query_embedding = get_embedding(query)

    # Retrieve similar passages from FAISS
    results = faiss_index.search(query_embedding)
    context = results[0][0] if results else "I'm not sure about that."

    # Concatenate context and query
    context_query = context + " " + query

    # Call OpenAI API for generating a response using the context + query
    try:
    # Corrected API call for chat completion
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can choose other models such as GPT-4
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": context_query}
        ],
    )

    # Get the response text from OpenAI API
        response_json = response.choices[0].message.content

    # Print in the desired format
        print(f"User: {query}")
        print(f"Bot: {response_json}")

    # Return the response content
        return response_json

    except Exception as e:
        return f"Error: {e}"