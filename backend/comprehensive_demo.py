# comprehensive_demo.py
"""
Comprehensive demonstration of Memory + Personality Engine for 30 chat messages.
This demonstrates all task requirements:
1. Memory extraction (preferences, emotional patterns, facts)
2. Personality Engine with different tones
3. Before/after personality response differences
4. Reasoning and prompt design
5. Structured output parsing
6. Modular system design
"""

import json
from memory_extractor import extract_messages
from personality_engine import transform_reply, show_personality_comparison

# Sample 30 chat messages representing diverse user interactions
sample_30_messages = [
    "I love Python and VSCode for coding.",
    "I'm worried I won't finish the assignment on time.",
    "Contact: alex.smith@example.com",
    "My number is 9876543210",
    "I prefer Colab for quick GPU testing.",
    "I enjoy working on cybersecurity projects.",
    "I'm happy with fast iterations in development.",
    "I'm sad about delays sometimes in my projects.",
    "Living in San Francisco, California.",
    "I use Git and GitHub for version control.",
    "No experience in mobile conversion yet.",
    "I like DenseNet169 for transfer learning.",
    "I use Obsidian to save my research notes.",
    "I worry about dataset size limitations.",
    "I feel excited when experiments succeed.",
    "I don't like noisy labels in my datasets.",
    "I love writing clean, maintainable code.",
    "My mentor is Dr. Sarah Johnson.",
    "I want to deploy models on Hugging Face Spaces.",
    "I prefer concise, direct replies over long explanations.",
    "I enjoy using Tailwind CSS for frontend work.",
    "I worked on the ThreatNet security project last year.",
    "I have intermediate ethical hacking skills.",
    "I want to run models on-device with TFLite optimization.",
    "I use VS Code on Ubuntu for my main development.",
    "I enjoy data analysis tasks and visualization.",
    "I sometimes feel frustrated with environment setup issues.",
    "I prefer technical answers without too much hand-holding.",
    "My name is Alex and I'm a CS graduate student.",
    "I study machine learning at Stanford University."
]

def main():
    print("🤖 MEMORY + PERSONALITY ENGINE DEMONSTRATION")
    print("=" * 60)
    print(f"Processing {len(sample_30_messages)} user messages...")
    
    # 1. MEMORY EXTRACTION
    print("\n📝 1. MEMORY EXTRACTION RESULTS:")
    print("-" * 40)
    
    extracted_memory = extract_messages(sample_30_messages)
    
    print(f"✅ Preferences found: {len(extracted_memory['preferences'])}")
    for pref in extracted_memory['preferences'][:3]:  # Show first 3
        print(f"   • {pref['type']}: {pref['value']} (confidence: {pref.get('confidence', 'N/A')})")
    
    print(f"✅ Emotional patterns: {len(extracted_memory['emotional_patterns'])}")
    for emotion in extracted_memory['emotional_patterns'][:3]:  # Show first 3
        print(f"   • {emotion['emotion']}: '{emotion['trigger']}' ({emotion.get('intensity', 'moderate')})")
    
    print(f"✅ Facts extracted: {len(extracted_memory['facts'])}")
    for fact in extracted_memory['facts'][:3]:  # Show first 3
        print(f"   • {fact['type']}: {fact['value']}")
    
    # 2. PERSONALITY ENGINE DEMONSTRATION
    print("\n🎭 2. PERSONALITY ENGINE - BEFORE/AFTER COMPARISON:")
    print("-" * 55)
    
    base_reply = "Start by collecting a diverse dataset, then preprocess your images using standard augmentation techniques. Consider using transfer learning with a pre-trained model."
    
    print(f"ORIGINAL REPLY:\n'{base_reply}'\n")
    
    # Show all personality transformations
    personalities = ["calm_mentor", "witty_friend", "therapist"]
    
    for personality in personalities:
        result = transform_reply(base_reply, personality, extracted_memory)
        print(f"--- {personality.upper().replace('_', ' ')} STYLE ---")
        print(f"TRANSFORMED: {result['transformed_reply']}")
        print(f"REASONING: {result['reasoning']}")
        print()
    
    # 3. CONTEXT-AWARE ADAPTATION
    print("🧠 3. CONTEXT-AWARE PERSONALITY ADAPTATION:")
    print("-" * 45)
    
    # Demonstrate how the system adapts based on user's emotional state
    worried_context = {
        "emotional_patterns": [{"emotion": "fear", "trigger": "worried", "intensity": "high"}],
        "preferences": [{"type": "language", "value": "python"}]
    }
    
    adapted_response = transform_reply(base_reply, "therapist", worried_context)
    print("When user shows anxiety/worry, therapist style adapts:")
    print(f"ADAPTED RESPONSE: {adapted_response['transformed_reply']}")
    print(f"REASONING: {adapted_response['reasoning']}")
    
    # 4. SYSTEM ARCHITECTURE OVERVIEW
    print("\n🏗️  4. MODULAR SYSTEM ARCHITECTURE:")
    print("-" * 40)
    print("✅ Memory Extractor: Structured parsing with confidence scoring")
    print("✅ Personality Engine: Context-aware response transformation")
    print("✅ API Endpoints: RESTful interface (/extract, /transform, /compare)")
    print("✅ Reasoning Engine: Transparent decision-making process")
    print("✅ Testing Suite: Comprehensive validation")
    
    # 5. CONFIDENCE AND METADATA
    print("\n📊 5. EXTRACTION CONFIDENCE & METADATA:")
    print("-" * 40)
    metadata = extracted_memory.get('extraction_metadata', {})
    confidence = metadata.get('confidence_scores', {})
    
    print(f"Messages processed: {metadata.get('total_messages_processed', 'N/A')}")
    print(f"Preference confidence: {confidence.get('preferences', 0):.2f}")
    print(f"Emotion confidence: {confidence.get('emotional_patterns', 0):.2f}")
    print(f"Facts confidence: {confidence.get('facts', 0):.2f}")
    
    print("\n🎉 DEMONSTRATION COMPLETE!")
    print("The system successfully demonstrates:")
    print("• Memory extraction from 30 messages")
    print("• Personality-aware response transformation")
    print("• Clear before/after differences")
    print("• Reasoning and structured output")
    print("• Modular, testable architecture")

if __name__ == "__main__":
    main()