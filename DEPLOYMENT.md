# 🚀 Deployment Guide for Memory + Personality Engine

This guide covers multiple deployment options for your AI companion system.

## 📋 Pre-Deployment Checklist

### 1. Environment Variables
- ✅ `.env` file with `OPENROUTER_API_KEY`
- ✅ Model configuration (`mistralai/mistral-7b-instruct`)
- ✅ CORS settings for production domains

### 2. Security Updates Needed
- 🔒 Restrict CORS origins (remove `*`)
- 🔒 Add rate limiting
- 🔒 Environment-specific configurations
- 🔒 API key validation

---

## 🌟 Option 1: Railway (Recommended - Easy)

### Steps:
1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   railway login
   ```

2. **Prepare for Railway**
   ```bash
   cd backend
   # Railway will auto-detect and deploy
   railway init
   railway up
   ```

3. **Set Environment Variables**
   - Go to Railway dashboard
   - Add `OPENROUTER_API_KEY` in environment variables
   - Set `PORT=8000`

**Frontend**: Deploy to Vercel/Netlify (static hosting)

---

## 🐳 Option 2: Docker + Cloud (Scalable)

### Docker Configuration:
Already created `Dockerfile` - let me update it:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Start command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Deployment Commands:
```bash
# Build and test locally
docker build -t memory-personality-engine .
docker run -p 8000:8000 --env-file .env memory-personality-engine

# Deploy to cloud (choose one):
# - Google Cloud Run
# - AWS ECS
# - DigitalOcean App Platform
```

---

## ⚡ Option 3: Render (Free Tier Available)

### Steps:
1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial deployment"
   git remote add origin <your-github-repo>
   git push -u origin main
   ```

2. **Deploy to Render**
   - Connect GitHub repo
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - Add environment variables

---

## 🔧 Production Configuration Updates

Let me update your code for production: