# Vercel Deployment Guide 🚀

## Prerequisites
- Git repository pushed to GitHub/GitLab/Bitbucket
- Vercel account (free tier available)
- Your backend already deployed on Render: https://personality-engine.onrender.com

## Quick Deploy to Vercel

### Option 1: One-Click Deploy (Recommended)
1. Click this button to deploy directly:
   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Surajkumaar/Personality-Engine)

### Option 2: Manual Deployment

#### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

#### Step 2: Login to Vercel
```bash
vercel login
```

#### Step 3: Deploy from Project Root
```bash
# Navigate to your project directory
cd "c:\Users\91735\Desktop\rag\task"

# Deploy to Vercel
vercel
```

#### Step 4: Configure During Deployment
When prompted:
- **Set up and deploy?** → Yes
- **Which scope?** → Your username/team
- **Link to existing project?** → No (first time)
- **Project name?** → personality-engine-frontend (or your choice)
- **Directory with code?** → `./` (current directory)
- **Want to override settings?** → Yes
- **Output Directory?** → `frontend`
- **Build Command?** → Leave empty (static files)
- **Development Command?** → Leave empty

#### Step 5: Set Environment Variables
```bash
# Set backend URL
vercel env add BACKEND_URL
# Enter: https://personality-engine.onrender.com
```

### Option 3: Web Interface Deployment

1. **Go to Vercel Dashboard**
   - Visit: https://vercel.com/dashboard
   - Click "New Project"

2. **Connect Repository**
   - Select your Git provider (GitHub recommended)
   - Choose your repository: `Personality-Engine`
   - Click "Import"

3. **Configure Project**
   - **Framework Preset:** Other
   - **Root Directory:** `./` (leave default)
   - **Build Command:** Leave empty
   - **Output Directory:** `frontend`
   - **Install Command:** Leave empty

4. **Environment Variables**
   - Add: `BACKEND_URL` = `https://personality-engine.onrender.com`

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete

## Post-Deployment

### Update CORS in Backend
Your Render backend needs to allow requests from Vercel. Update your backend's CORS settings to include your Vercel domain.

### Test Your Deployment
1. Visit your Vercel URL (e.g., https://personality-engine-frontend.vercel.app)
2. Test the memory extraction feature
3. Test personality transformation
4. Verify backend communication

## Custom Domain (Optional)
1. Go to your Vercel project dashboard
2. Click "Settings" → "Domains"
3. Add your custom domain
4. Configure DNS records as instructed

## Useful Commands

```bash
# Deploy to production
vercel --prod

# View deployment logs
vercel logs

# List all deployments
vercel ls

# View project settings
vercel inspect

# Remove deployment
vercel remove
```

## Troubleshooting

### CORS Issues
If you get CORS errors, make sure your backend allows your Vercel domain:
```python
# In your backend app.py, update CORS origins:
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000", 
    "https://your-app-name.vercel.app",  # Add your Vercel domain
    "https://personality-engine.onrender.com"
]
```

### API Connection Issues
- Verify your backend URL in `frontend/script.js`
- Check that your backend is running on Render
- Test API endpoints directly in browser

## Architecture Overview
```
Frontend (Vercel) → Backend (Render) → OpenRouter API
     ↓                    ↓                 ↓
Static Files        FastAPI Server    Mistral LLM
HTML/CSS/JS         Memory Engine     Personality AI
```

## Environment Variables Summary
- **BACKEND_URL:** https://personality-engine.onrender.com
- **NODE_ENV:** production (automatically set by Vercel)

## Next Steps
1. Deploy to Vercel using preferred method above
2. Test all functionality
3. Optional: Set up custom domain
4. Optional: Configure analytics and monitoring

🎉 Your Memory + Personality Engine will be live on Vercel!