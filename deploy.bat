@echo off
echo 🚀 Memory + Personality Engine - Windows Deployment
echo ================================================
echo.

REM Check if we're in the right directory
if not exist "backend\app.py" (
    echo ❌ Please run this script from the project root directory
    pause
    exit /b 1
)

echo 📋 Choose deployment option:
echo 1. Railway ^(Backend^)
echo 2. Docker + Cloud
echo 3. Render ^(Backend^) 
echo 4. Vercel ^(Frontend^)
echo 5. Local Production Test
echo.

set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo 🚂 Deploying to Railway...
    echo 1. Install Railway CLI: npm install -g @railway/cli
    echo 2. Login: railway login
    echo 3. Initialize: railway init
    echo 4. Set environment variables in Railway dashboard:
    echo    - OPENROUTER_API_KEY=your_openrouter_api_key_here
    echo    - ENVIRONMENT=production
    echo 5. Deploy: railway up
) else if "%choice%"=="2" (
    echo 🐳 Building Docker image...
    cd backend
    docker build -t memory-personality-engine .
    echo ✅ Docker image built!
    echo Deploy to your cloud platform of choice:
    echo - Google Cloud Run
    echo - AWS ECS  
    echo - DigitalOcean App Platform
) else if "%choice%"=="3" (
    echo 🎨 Render deployment:
    echo 1. Push code to GitHub
    echo 2. Connect GitHub repo to Render
    echo 3. Use render.yaml configuration
    echo 4. Set environment variables
    echo 5. Deploy!
) else if "%choice%"=="4" (
    echo ⚡ Vercel deployment ^(Frontend^):
    echo 1. Install Vercel CLI: npm install -g vercel
    echo 2. Login: vercel login
    echo 3. Deploy: vercel
    echo 4. Or use one-click deploy from GitHub
    echo 5. Backend is already on Render: https://personality-engine.onrender.com
    echo 📚 See VERCEL_DEPLOY.md for detailed guide
) else if "%choice%"=="5" (
    echo 🏠 Testing production build locally...
    cd backend
    set ENVIRONMENT=production
    echo Starting server...
    uvicorn app:app --host 0.0.0.0 --port 8000 --workers 1
) else (
    echo ❌ Invalid choice
    pause
    exit /b 1
)

echo.
echo 🎉 Deployment guide complete!
echo 📚 Check DEPLOYMENT.md for detailed instructions
pause