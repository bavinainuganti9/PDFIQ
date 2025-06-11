# PDFIQ

## Overview / Description  
PDFIQ is a semantic search and Q&A engine for research papers that lets users upload PDFs, extract and vectorize their content, then ask natural language questions. The system retrieves relevant document passages and generates concise answers using GPT-4, making academic research faster and more accessible.

## Features  
- Upload and ingest PDFs with automatic text extraction  
- Generate semantic embeddings for document pages using OpenAI’s embedding models  
- Perform semantic similarity search to find relevant content for user questions  
- Generate natural language answers grounded on retrieved document text via GPT-4  
- Simple React-based frontend for uploading PDFs and asking questions  
- Lightweight FastAPI backend serving ingestion and Q&A endpoints  

## Architecture  
Ingestion: Python FastAPI service extracts text from PDFs, generates embeddings with OpenAI API, and stores vectors in FAISS index  
Search & Q&A: Queries embed user questions, search FAISS for top relevant passages, then compose prompt for GPT-4 to generate grounded answers  
Frontend: React UI provides PDF upload and Q&A interface, communicates with backend via REST API  

## Tech Stack  
- Python (FastAPI, PyPDF for PDF parsing, FAISS for vector search)  
- OpenAI API (text-embedding-ada-002 for embeddings, GPT-4 for answers)  
- React with TailwindCSS for frontend  
- Axios for frontend-backend communication  
- dotenv for environment variable management  
