@echo off
echo 🌐 Starting Memory + Personality Engine Frontend
echo ============================================
echo.
echo Make sure the backend is running first:
echo   cd backend
echo   uvicorn app:app --host 127.0.0.1 --port 8000
echo.
echo Starting frontend server...
python serve.py