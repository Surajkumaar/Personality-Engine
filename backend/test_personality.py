# test_personality.py
from personality_engine import transform_reply, show_personality_comparison

# Test before/after personality differences
base_reply = "Start by collecting your dataset and preprocessing the images."

print("=== BEFORE/AFTER PERSONALITY DEMONSTRATION ===\n")
print(f"ORIGINAL: {base_reply}\n")

# Test all three personalities
styles = ["calm_mentor", "witty_friend", "therapist"]

for style in styles:
    result = transform_reply(base_reply, style)
    print(f"--- {style.upper().replace('_', ' ')} ---")
    print(f"TRANSFORMED: {result['transformed_reply']}")
    print(f"REASONING: {result['reasoning']}\n")

# Test with user context
print("=== WITH USER EMOTIONAL CONTEXT ===")
user_context = {
    "emotional_patterns": [{"emotion": "fear", "trigger": "worried"}],
    "preferences": [{"type": "language", "value": "python"}]
}

therapist_result = transform_reply(base_reply, "therapist", user_context)
print(f"THERAPIST (with context): {therapist_result['transformed_reply']}")
print(f"REASONING: {therapist_result['reasoning']}")