@echo off
echo 🤖 Starting Memory + Personality Engine Backend
echo =============================================
echo.

cd /d "%~dp0"

echo 📝 Loading environment variables...
echo ✅ API Key loaded from .env file
echo.

echo 🚀 Starting FastAPI server...
echo 📍 Backend will be available at: http://127.0.0.1:8000
echo 🔧 Using Mistral LLM via OpenRouter
echo.

uvicorn app:app --host 127.0.0.1 --port 8000 --reload

echo.
echo 🛑 Server stopped
pause