def split_text(text, max_length=150, min_length=50):
    """
    Splits the input text into chunks to improve embedding quality.
    
    Args:
        text (str): The text to split.
        max_length (int): The maximum number of characters in each chunk.
        min_length (int): The minimum number of characters to form a chunk.

    Returns:
        list: A list of text chunks.
    """
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        current_text = ' '.join(current_chunk)
        
        if len(current_text) >= min_length and (len(current_text) >= max_length or len(current_chunk) >= len(words)):
            chunks.append(current_text)
            current_chunk = []

    # Add any remaining text as the last chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
