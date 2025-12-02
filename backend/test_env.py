#!/usr/bin/env python3
"""
Test script that loads API key from .env file
"""
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def test_env_setup():
    print("🔧 Environment Configuration Test")
    print("=" * 40)
    
    # Check if API key is loaded
    api_key = os.getenv('OPENROUTER_API_KEY')
    if api_key:
        print(f"✅ OpenRouter API Key: {api_key[:10]}...{api_key[-10:]}")
    else:
        print("❌ OpenRouter API Key not found!")
        return False
    
    # Check other environment variables
    model = os.getenv('LLM_MODEL', 'mistralai/mistral-7b-instruct')
    print(f"🤖 LLM Model: {model}")
    
    host = os.getenv('HOST', '127.0.0.1')
    port = os.getenv('PORT', '8000')
    print(f"🌐 Server: {host}:{port}")
    
    return True

def test_personality_engine():
    print("\n🎭 Testing LLM Personality Engine")
    print("=" * 40)
    
    try:
        from personality_engine import transform_reply
        
        result = transform_reply(
            "Start by setting up your development environment.",
            "witty_friend"
        )
        
        print(f"✅ Transformation successful!")
        print(f"🤖 Model used: {result.get('model_used', 'unknown')}")
        print(f"💡 Used LLM: {result.get('used_llm', False)}")
        print(f"📝 Response preview: {result['transformed_reply'][:80]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    env_ok = test_env_setup()
    
    if env_ok:
        llm_ok = test_personality_engine()
        
        if llm_ok:
            print("\n🎉 All tests passed! Ready to start the server.")
            print("\nTo start the backend:")
            print("  python -c 'from dotenv import load_dotenv; load_dotenv(); import uvicorn; uvicorn.run(\"app:app\", host=\"127.0.0.1\", port=8000)'")
            print("\nOr simply run:")
            print("  start.bat")
        else:
            print("\n⚠️  LLM test failed. Check your API key and internet connection.")
    else:
        print("\n⚠️  Environment setup failed. Check your .env file.")