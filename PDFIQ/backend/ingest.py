import os
import faiss
import numpy as np
import openai
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

INDEX_FILE = "embeddings.index"
DOCS = []

def embed_text(text):
    resp = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
    return np.array(resp.data[0].embedding, dtype="float32")

def ingest_pdf(file_bytes, filename):
    reader = PdfReader(file_bytes)
    texts = [page.extract_text() for page in reader.pages]
    texts = [t for t in texts if t]
    embs = [embed_text(t) for t in texts]

    if os.path.exists(INDEX_FILE):
        idx = faiss.read_index(INDEX_FILE)
    else:
        idx = faiss.IndexFlatL2(len(embs[0]))

    for i, emb in enumerate(embs):
        idx.add(np.array([emb]))
        DOCS.append({"filename": filename, "page": i, "text": texts[i]})

    faiss.write_index(idx, INDEX_FILE)

def search_sim(query, topk=5):
    query_emb = embed_text(query)
    idx = faiss.read_index(INDEX_FILE)
    D, I = idx.search(np.array([query_emb]), topk)
    return [DOCS[int(i)] for i in I[0]]
