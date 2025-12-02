# Memory + Personality Engine
## AI Companion with Personality Adaptation

A production-ready AI system that learns user preferences and adapts response personalities using LLM technology.

## 🚀 Live Demo
- **Frontend**: [Your Frontend URL]
- **API**: [Your Backend URL]
- **Documentation**: [Your Backend URL]/docs

## ⚡ Quick Deploy

### Option 1: Railway (Recommended)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

1. Click the Railway button above
2. Connect your GitHub repository
3. Set environment variable: `OPENROUTER_API_KEY`
4. Deploy automatically!

### Option 2: Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Click the Render button above
2. Connect your repository
3. Set environment variables
4. Deploy with zero configuration

### Option 3: Vercel + Railway
**Frontend on Vercel:**
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

**Backend on Railway:**
Use Railway option above

## 🔧 Environment Variables

### Required:
```bash
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

### Optional:
```bash
ENVIRONMENT=production
FRONTEND_URL=https://your-frontend.vercel.app
LLM_MODEL=mistralai/mistral-7b-instruct
```

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend API   │
│   (Vercel)      │───▶│   (Railway)     │
│   Static Site   │    │   FastAPI       │
└─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   OpenRouter    │
                       │   Mistral LLM   │
                       └─────────────────┘
```

## 📊 Features

- **Memory Extraction**: Learns user preferences, emotions, and facts
- **Personality Adaptation**: 3 distinct AI personalities with LLM power
- **Real-time API**: RESTful endpoints with automatic documentation
- **Production Ready**: Docker, health checks, security headers
- **Scalable**: Microservices architecture

## 🛠️ Local Development

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

# Frontend  
cd frontend
python serve.py
```

## 📈 Monitoring

- Health check: `/health`
- API docs: `/docs`
- Metrics: Available via deployment platform

## 🔒 Security

- CORS protection
- Environment-based configuration
- Rate limiting ready
- Non-root Docker user

## 📄 License

Educational/Demo Project - 2025