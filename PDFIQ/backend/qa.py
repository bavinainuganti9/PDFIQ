import openai
import os
from dotenv import load_dotenv
from ingest import search_sim

load_dotenv()

def answer_question(question):
    docs = search_sim(question, topk=3)
    context = "\n---\n".join([d["text"] for d in docs])
    prompt = f"Use the following context:\n{context}\n\nAnswer: {question}"
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2
    )
    return resp.choices[0].message.content
