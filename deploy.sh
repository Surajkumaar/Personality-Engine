#!/bin/bash

# 🚀 Quick Deployment Script for Memory + Personality Engine

echo "🤖 Memory + Personality Engine Deployment"
echo "========================================"
echo

# Check if we're in the right directory
if [ ! -f "backend/app.py" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

echo "📋 Choose deployment option:"
echo "1. Railway (Recommended)"
echo "2. Docker + Cloud"  
echo "3. Render"
echo "4. Local Production Test"
echo

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo "🚂 Deploying to Railway..."
        echo "1. Install Railway CLI: npm install -g @railway/cli"
        echo "2. Login: railway login"
        echo "3. Initialize: railway init"
        echo "4. Set environment variables in Railway dashboard:"
        echo "   - OPENROUTER_API_KEY=$OPENROUTER_API_KEY"
        echo "   - ENVIRONMENT=production"
        echo "5. Deploy: railway up"
        ;;
    2)
        echo "🐳 Building Docker image..."
        cd backend
        docker build -t memory-personality-engine .
        echo "✅ Docker image built!"
        echo "Deploy to your cloud platform of choice:"
        echo "- Google Cloud Run"
        echo "- AWS ECS"
        echo "- DigitalOcean App Platform"
        ;;
    3)
        echo "🎨 Render deployment:"
        echo "1. Push code to GitHub"
        echo "2. Connect GitHub repo to Render"
        echo "3. Use render.yaml configuration"
        echo "4. Set environment variables"
        echo "5. Deploy!"
        ;;
    4)
        echo "🏠 Testing production build locally..."
        cd backend
        export ENVIRONMENT=production
        echo "Starting server..."
        uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo
echo "🎉 Deployment guide complete!"
echo "📚 Check DEPLOYMENT.md for detailed instructions"