#!/usr/bin/env python3
"""
Test the LLM-powered personality engine
"""
import os
import sys
import json

# Set the API key
os.environ['OPENROUTER_API_KEY'] = "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"

try:
    from personality_engine import transform_reply
    from memory_extractor import extract_messages
    
    print("🤖 Testing LLM-Powered Personality Engine")
    print("=" * 50)
    
    # Test messages
    test_messages = [
        "I love Python programming",
        "I'm worried about my project deadline", 
        "My name is Alex and I study at MIT"
    ]
    
    # Extract memory
    print("📝 Extracting memory...")
    memory = extract_messages(test_messages)
    print(f"✅ Found {len(memory.get('preferences', []))} preferences")
    print(f"✅ Found {len(memory.get('emotional_patterns', []))} emotions")
    print(f"✅ Found {len(memory.get('facts', []))} facts")
    
    # Test personality transformation
    base_reply = "Start by organizing your code structure and then implement the main functionality."
    
    print(f"\n🎭 Testing Personality Transformations")
    print(f"Original: {base_reply}")
    print("-" * 50)
    
    for style in ['calm_mentor', 'witty_friend', 'therapist']:
        print(f"\n--- {style.upper().replace('_', ' ')} ---")
        try:
            result = transform_reply(base_reply, style, memory)
            print(f"✅ Transformed: {result['transformed_reply'][:100]}...")
            print(f"🔧 Model: {result.get('model_used', 'unknown')}")
            print(f"🤖 Used LLM: {result.get('used_llm', False)}")
            if result.get('reasoning'):
                print(f"💭 Reasoning: {result['reasoning'][:80]}...")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n🎉 Test completed!")
    
except Exception as e:
    print(f"❌ Import error: {e}")
    print("Make sure all dependencies are installed:")
    print("pip install openai fastapi pydantic")