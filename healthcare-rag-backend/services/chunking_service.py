import tiktoken
from typing import List

def split_text_into_chunks(text: str, max_tokens: int = 500, overlap: int = 50) -> List[str]:
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)

    chunks = []
    start = 0
    while start < len(tokens):
        end = start + max_tokens
        chunk = tokenizer.decode(tokens[start:end])
        chunks.append(chunk)
        start += max_tokens - overlap  # sliding window

    return chunks
