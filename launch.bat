@echo off
echo 🚀 Memory + Personality Engine Launcher
echo =======================================
echo.

echo 📦 Starting Backend Server...
cd /d "%~dp0backend"
start "Backend Server" cmd /k "uvicorn app:app --host 127.0.0.1 --port 8000"

echo.
echo ⏳ Waiting for backend to start...
timeout /t 3 /nobreak >nul

echo.
echo 🌐 Starting Frontend Server...
cd /d "%~dp0frontend"
start "Frontend Server" cmd /k "python serve.py"

echo.
echo ✅ Both servers are starting!
echo.
echo 🔗 Frontend: http://localhost:3000
echo 🤖 Backend:  http://127.0.0.1:8000
echo.
echo Press any key to exit launcher...
pause >nul