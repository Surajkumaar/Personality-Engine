# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from memory_extractor import extract_messages
from personality_engine import transform_reply


app = FastAPI(
    title="Memory + Personality API",
    description="AI companion that learns user preferences and adapts personality styles",
    version="1.0.0"
)

# Production CORS configuration
allowed_origins = [
    "http://localhost:3000",
    "http://localhost:3001", 
    "http://localhost:3002",
    "http://127.0.0.1:3000",
    "https://*.vercel.app",  # Allow all Vercel subdomains
    "https://personality-engine-frontend.vercel.app",  # Specific Vercel domain
    "https://your-frontend-domain.netlify.app",  # Update with your frontend URL
]

# Use environment variable for allowed origins in production
if os.getenv("ENVIRONMENT") == "production":
    frontend_url = os.getenv("FRONTEND_URL")
    if frontend_url:
        allowed_origins = [frontend_url]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if os.getenv("ENVIRONMENT") == "production" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ExtractRequest(BaseModel):
    messages: List[str]


class TransformRequest(BaseModel):
    messages: List[str]
    style: Optional[str] = "calm_mentor"
    sample_reply: Optional[str] = "Here is a suggested plan."


@app.post("/extract")
def extract_endpoint(req: ExtractRequest):
    return extract_messages(req.messages)


@app.post("/transform")
def transform_endpoint(req: TransformRequest):
    extracted = extract_messages(req.messages)
    # Pass extracted context to personality engine for better adaptation
    transformed = transform_reply(req.sample_reply, req.style, extracted)
    return {"extracted": extracted, "personality_response": transformed}

@app.post("/compare")
def compare_personalities_endpoint(req: TransformRequest):
    """Show before/after personality differences for the same reply."""
    from personality_engine import show_personality_comparison
    extracted = extract_messages(req.messages)
    comparison = show_personality_comparison(req.sample_reply, extracted)
    return {"extracted_context": extracted, "personality_comparison": comparison}


@app.get("/")
def root():
    return {
        "message": "Memory + Personality API", 
        "endpoints": ["/extract", "/transform", "/compare", "/health"],
        "version": "1.0.0",
        "status": "operational"
    }

@app.get("/health")
def health_check():
    """Health check endpoint for deployment monitoring"""
    api_key_available = bool(os.getenv('OPENROUTER_API_KEY'))
    return {
        "status": "healthy",
        "llm_available": api_key_available,
        "timestamp": "2025-12-02"
    }

@app.get("/health")
def health_check():
    """Health check endpoint for deployment monitoring"""
    api_key_available = bool(os.getenv('OPENROUTER_API_KEY'))
    return {
        "status": "healthy",
        "llm_available": api_key_available,
        "timestamp": "2025-12-02"
    }