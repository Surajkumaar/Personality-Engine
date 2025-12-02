# Frontend Setup Instructions

## Memory + Personality Engine Frontend

This is a simple, interactive web interface for the Memory + Personality Engine API.

### Features

🧠 **Memory Extraction**
- Input chat messages to extract user preferences, emotional patterns, and facts
- Visual categorization with color-coded sections
- Sample data loader for quick testing

🎭 **Personality Engine**
- Transform responses using different personality styles (Calm Mentor, Witty Friend, Therapist)
- Side-by-side comparison of all personality variations
- Context-aware adaptations based on extracted memory

✨ **Interactive Interface**
- Clean, modern design with Tailwind CSS
- Real-time API communication
- Error handling and loading states
- Responsive layout for mobile and desktop

### Quick Start

1. **Start the Backend Server**
   ```bash
   cd backend
   uvicorn app:app --host 127.0.0.1 --port 8000
   ```

2. **Open the Frontend**
   - Simply open `index.html` in your web browser
   - Or serve it locally:
   ```bash
   cd frontend
   python -m http.server 3000
   # Then visit http://localhost:3000
   ```

3. **Test the Interface**
   - Click "Load Sample Messages" to populate with test data
   - Click "Extract Memory" to analyze the messages
   - Try different personality transformations
   - Compare all personality styles side-by-side

### API Endpoints Used

- `GET /` - Health check
- `POST /extract` - Extract memory from messages
- `POST /transform` - Transform reply with personality
- `POST /compare` - Compare all personality styles

### Technologies Used

- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Backend**: FastAPI, Python
- **Communication**: Fetch API (REST)

### File Structure

```
frontend/
├── index.html      # Main interface
├── script.js       # JavaScript functionality
└── README.md       # This file
```

### Browser Support

Works in all modern browsers that support:
- ES6+ JavaScript
- Fetch API
- CSS Grid/Flexbox

Enjoy exploring the Memory + Personality Engine! 🚀