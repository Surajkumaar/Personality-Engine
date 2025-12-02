# 🤖 Memory + Personality Engine

A complete AI companion system that extracts user memory and adapts personality styles for personalized responses.

## 📋 Project Overview

This system demonstrates advanced companion AI capabilities by:

1. **Memory Extraction**: Analyzing chat messages to identify user preferences, emotional patterns, and important facts
2. **Personality Engine**: Transforming responses with different personality styles (Calm Mentor, Witty Friend, Therapist)
3. **Context Adaptation**: Using extracted memory to personalize interactions
4. **Modular Architecture**: Clean separation between memory extraction, personality transformation, and API layers

## 🏗️ Architecture

```
Memory + Personality Engine/
├── backend/                 # FastAPI server & AI logic
│   ├── app.py              # Main API endpoints
│   ├── memory_extractor.py # Memory parsing & extraction
│   ├── personality_engine.py # Personality transformations
│   ├── requirements.txt    # Python dependencies
│   ├── comprehensive_demo.py # CLI demonstration
│   └── test/               # Test suite
├── frontend/               # Web interface
│   ├── index.html          # Main UI
│   ├── script.js           # Frontend logic
│   ├── serve.py            # Local server
│   └── README.md           # Frontend docs
└── launch.bat              # Start both servers
```

## 🚀 Quick Start

### Option 1: Automatic Launch (Windows)
```bash
# Start both frontend and backend
launch.bat
```

### Option 2: Manual Setup

**1. Start Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --host 127.0.0.1 --port 8000
```

**2. Start Frontend**
```bash
cd frontend
python serve.py
# Visit http://localhost:3000
```

## 🎯 Key Features

### Memory Extraction
- **User Preferences**: Programming languages, tools, topics of interest
- **Emotional Patterns**: Joy, sadness, anger, fear with intensity levels
- **Personal Facts**: Names, contact info, locations, relationships
- **Confidence Scoring**: Reliability metrics for extracted information

### Personality Engine
- **Calm Mentor**: Encouraging, step-by-step guidance with supportive tone
- **Witty Friend**: Humorous, casual approach with jokes and emoji
- **Therapist**: Empathetic, validating responses with reflective questions
- **Context Awareness**: Adapts personality based on user's emotional state

### API Endpoints
- `POST /extract` - Extract memory from messages
- `POST /transform` - Transform reply with personality
- `POST /compare` - Compare all personality styles
- `GET /` - Health check

## 🧪 Testing & Demo

### CLI Demo
```bash
cd backend
python comprehensive_demo.py
```

### Web Interface Demo
1. Visit http://localhost:3000
2. Click "Load Sample Messages"
3. Click "Extract Memory" 
4. Try personality transformations
5. Compare all styles side-by-side

### Test Suite
```bash
cd backend
python test/test_extraction.py
```

## 📊 Sample Output

**Memory Extraction:**
```json
{
  "preferences": [
    {"type": "language", "value": "python", "confidence": 0.9},
    {"type": "tools", "value": "vscode", "confidence": 0.7}
  ],
  "emotional_patterns": [
    {"emotion": "joy", "trigger": "love", "intensity": "high"},
    {"emotion": "fear", "trigger": "worried", "intensity": "moderate"}
  ],
  "facts": [
    {"type": "personal_info", "value": "Alex", "subtype": "name"},
    {"type": "contact_info", "value": "alex@example.com", "subtype": "email"}
  ]
}
```

**Personality Comparison:**
```
ORIGINAL: "Start by collecting your dataset and preprocessing images."

CALM MENTOR: "Let me guide you step by step. Start by collecting your dataset... 
✨ Remember, every expert was once a beginner. You're making progress!"

WITTY FRIEND: "Hey! Start by collecting your dataset... 
😄 Pro tip: You've got this! (And if not, we'll figure it out with coffee ☕)"

THERAPIST: "I understand this might feel challenging. Start by collecting your dataset...
How are you feeling about this approach? It's okay to take things one step at a time."
```

## 🔧 Technical Implementation

### Memory Extractor Features
- **Structured Pattern Matching**: Uses regex and keyword maps for reliable extraction
- **Confidence Scoring**: Provides reliability metrics for each extraction
- **Hierarchical Classification**: Organizes facts by type and subtype
- **Context Preservation**: Maintains original message context for each extraction

### Personality Engine Features  
- **Template-Based Transformation**: Deterministic, controllable personality adaptation
- **Reasoning Transparency**: Explains why each transformation was applied
- **Context Integration**: Uses extracted memory to inform personality choices
- **Modular Design**: Easy to add new personality styles

### Frontend Features
- **Responsive Design**: Works on mobile and desktop with Tailwind CSS
- **Real-time API Communication**: Live updates with fetch API
- **Interactive Comparison**: Side-by-side personality demonstrations
- **Error Handling**: Graceful degradation with informative messages

## 📈 Use Cases

- **AI Companions**: Personalized chatbots that adapt to user preferences
- **Customer Support**: Context-aware response styling based on user emotions
- **Educational Tools**: Adaptive learning systems with personality-matched explanations
- **Mental Health**: Therapy-style interactions with empathetic response patterns
- **Content Creation**: Personality-aware writing assistance

## 🛠️ Technologies Used

**Backend:**
- FastAPI for REST API
- Pydantic for data validation
- Python regex for pattern matching
- Uvicorn ASGI server

**Frontend:**
- HTML5 & modern CSS
- Tailwind CSS for styling
- Alpine.js for reactivity
- Vanilla JavaScript

## 🎯 Task Requirements Fulfilled

✅ **Memory Extraction Module**: Identifies user preferences, emotional patterns, and facts  
✅ **Personality Engine**: Transforms agent reply tone with multiple styles  
✅ **Before/After Differences**: Clear demonstration of personality variations  
✅ **Reasoning & Prompt Design**: Transparent transformation logic  
✅ **Structured Output Parsing**: Well-defined JSON schemas  
✅ **User Memory Integration**: Context-aware personality adaptation  
✅ **Modular System Design**: Clean architecture with separated concerns  

## 📝 License

This project is created for educational/demonstration purposes as part of an AI assignment.

---

**🎉 Ready to explore personalized AI interactions!**