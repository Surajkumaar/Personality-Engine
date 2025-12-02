# personality_engine.py
from typing import Dict, Optional
import openai
import json
import os


PROMPT_TEMPLATES = {
    "calm_mentor": "You are a calm, patient mentor. Reply concisely and guide the user step-by-step. Maintain encouragement.",
    "witty_friend": "You are a witty friend. Use short jokes, casual tone, but provide correct guidance.",
    "therapist": "You are an empathetic therapist-style assistant. Validate feelings, ask reflective questions, keep language gentle."
}


def transform_reply_with_llm(base_reply: str, style: str, user_context: Dict = None) -> Dict:
    """Use OpenRouter LLM for intelligent personality transformation"""
    
    # Get API key from environment
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY environment variable not set")
    
    # Configure OpenAI client for OpenRouter
    client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    
    # Build context-aware prompt
    context_info = ""
    if user_context:
        prefs = user_context.get('preferences', [])
        emotions = user_context.get('emotional_patterns', [])
        facts = user_context.get('facts', [])
        
        if prefs:
            pref_summary = ", ".join([f"{p.get('type', 'unknown')}: {p.get('value', 'unknown')}" for p in prefs[:3]])
            context_info += f"User preferences: {pref_summary}. "
        
        if emotions:
            emotion_summary = ", ".join([f"{e.get('emotion', 'unknown')} (trigger: {e.get('trigger', 'unknown')})" for e in emotions[:2]])
            context_info += f"Emotional patterns: {emotion_summary}. "
        
        if facts:
            fact_summary = ", ".join([f"{f.get('value', 'unknown')}" for f in facts[:3] if f.get('type') == 'personal_info'])
            if fact_summary:
                context_info += f"Personal info: {fact_summary}. "
    
    # Style-specific instructions
    style_instructions = {
        "calm_mentor": {
            "persona": "You are a wise, patient mentor who provides gentle guidance and encouragement.",
            "tone": "Use a calm, supportive tone with step-by-step guidance. Add encouraging phrases and wisdom. Use emojis sparingly (✨, 🌟).",
            "approach": "Break down complex topics, offer reassurance, and remind the user of their progress."
        },
        "witty_friend": {
            "persona": "You are a funny, casual friend who's knowledgeable but keeps things light and humorous.",
            "tone": "Use casual language, jokes, and friendly banter. Add humor while staying helpful. Use fun emojis (😄, ☕, 🚀).",
            "approach": "Make technical content approachable with humor, offer to help together, use casual expressions."
        },
        "therapist": {
            "persona": "You are an empathetic therapist who validates feelings and encourages self-reflection.",
            "tone": "Use gentle, validating language with reflective questions. Be emotionally supportive. Use calming emojis (💭, 🌸).",
            "approach": "Acknowledge challenges, ask about feelings, offer emotional support alongside technical guidance."
        }
    }
    
    current_style = style_instructions.get(style, style_instructions["calm_mentor"])
    
    # Create the prompt
    system_prompt = f"""
{current_style['persona']}

Your task: Transform technical responses to match your personality style.

Style Guidelines:
- Tone: {current_style['tone']}
- Approach: {current_style['approach']}

Context about the user: {context_info if context_info else "No specific context available."}

Important:
- Keep the technical accuracy intact
- Adapt the delivery to your personality
- Consider the user's emotional state if provided
- Be natural and authentic to your character
"""
    
    user_prompt = f"""
Transform this technical response using the '{style}' personality:

Original: "{base_reply}"

Please provide a transformed version that maintains technical accuracy while embodying your personality style. Also explain your reasoning for the transformation choices.
"""
    
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",  # Use Mistral model
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,  # Allow creativity for personality expression
            max_tokens=500
        )
        
        llm_output = response.choices[0].message.content.strip()
        
        # Try to extract reasoning if the LLM provided it
        reasoning = "LLM-generated personality transformation"
        transformed_reply = llm_output
        
        # Simple parsing to separate response and reasoning
        if "Reasoning:" in llm_output or "Explanation:" in llm_output:
            parts = llm_output.split("Reasoning:") if "Reasoning:" in llm_output else llm_output.split("Explanation:")
            if len(parts) == 2:
                transformed_reply = parts[0].strip()
                reasoning = parts[1].strip()
        
        return {
            "original_reply": base_reply,
            "transformed_reply": transformed_reply,
            "personality_style": style,
            "reasoning": f"LLM transformation: {reasoning}",
            "adaptations_applied": user_context is not None,
            "used_llm": True,
            "model_used": "mistralai/mistral-7b-instruct"
        }
        
    except Exception as e:
        # If LLM fails, raise error to trigger fallback
        raise Exception(f"LLM transformation failed: {str(e)}")


def transform_reply(base_reply: str, style: str, user_context: Dict = None) -> Dict:
    """Main transform function with LLM primary and rule-based fallback"""
    
    try:
        # Try LLM first if API key is available
        if os.getenv('OPENROUTER_API_KEY'):
            return transform_reply_with_llm(base_reply, style, user_context)
        else:
            # No API key, use rule-based
            return transform_reply_rule_based(base_reply, style, user_context)
            
    except Exception as e:
        print(f"LLM transformation failed: {e}")
        print("Falling back to rule-based transformation...")
        # Fallback to rule-based approach
        return transform_reply_rule_based(base_reply, style, user_context)


def transform_reply_rule_based(base_reply: str, style: str, user_context: Dict = None) -> Dict:
    """Rule-based personality transformation (fallback method)
    
    Args:
        base_reply: The original response content
        style: Personality style to apply
        user_context: Optional user memory context for personalization
    
    Returns:
        Dict with original, transformed reply, and reasoning
    """
    style = style or "calm_mentor"
    prompt = PROMPT_TEMPLATES.get(style, PROMPT_TEMPLATES['calm_mentor'])
    
    # Reasoning for personality adaptation
    reasoning = f"Rule-based adaptation using '{style}' personality style."
    
    if user_context:
        preferences = user_context.get('preferences', [])
        emotions = user_context.get('emotional_patterns', [])
        
        # Adapt based on user's emotional state
        if emotions:
            dominant_emotion = emotions[0].get('emotion', '') if emotions else ''
            if dominant_emotion in ['sadness', 'fear'] and style != 'therapist':
                reasoning += f" Detected {dominant_emotion} - adding empathetic tone."
    
    transformed = ""
    if style == "calm_mentor":
        transformed = f"Let me guide you step by step. {base_reply}\n\n✨ Remember, every expert was once a beginner. You're making progress!"
        reasoning += " Using encouraging, step-by-step guidance approach."
        
    elif style == "witty_friend":
        transformed = f"Hey! {base_reply}\n\n😄 Pro tip: You've got this! (And if not, we'll figure it out together with some coffee ☕)"
        reasoning += " Adding humor and casual friendship tone."
        
    elif style == "therapist":
        transformed = f"I understand this might feel challenging. {base_reply}\n\nHow are you feeling about this approach? Remember, it's okay to take things one step at a time."
        reasoning += " Using validation and reflective questioning approach."
        
    else:
        transformed = base_reply
    
    return {
        "original_reply": base_reply,
        "transformed_reply": transformed,
        "personality_style": style,
        "reasoning": reasoning,
        "adaptations_applied": user_context is not None,
        "used_llm": False,
        "model_used": "rule-based"
    }

def show_personality_comparison(base_reply: str, user_context: Dict = None) -> Dict:
    """Demonstrate before/after differences across all personality styles."""
    styles = ["calm_mentor", "witty_friend", "therapist"]
    comparison = {
        "original_reply": base_reply,
        "personality_variations": []
    }
    
    for style in styles:
        result = transform_reply(base_reply, style, user_context)
        comparison["personality_variations"].append(result)
    
    return comparison


if __name__ == '__main__':
    # Demo: Before/After personality response differences
    base_reply = "Start by collecting your dataset and then preprocess the images."
    
    print("=== PERSONALITY ENGINE DEMONSTRATION ===\\n")
    print(f"Original Reply: '{base_reply}'\\n")
    
    # Show individual transformations
    styles = ["calm_mentor", "witty_friend", "therapist"]
    for style in styles:
        result = transform_reply(base_reply, style)
        print(f"--- {style.upper().replace('_', ' ')} STYLE ---")
        print(f"Transformed: {result['transformed_reply']}")
        print(f"Reasoning: {result['reasoning']}\\n")
    
    # Show comparison with user context
    print("=== WITH USER CONTEXT (Emotional Adaptation) ===")
    user_context = {
        "preferences": [{"type": "language", "value": "python"}],
        "emotional_patterns": [{"emotion": "fear", "trigger": "worried"}],
        "facts": [{"type": "name", "value": "Sarah"}]
    }
    
    therapist_result = transform_reply(base_reply, "therapist", user_context)
    print(f"Therapist with context: {therapist_result['transformed_reply']}")
    print(f"Reasoning: {therapist_result['reasoning']}")
    
    print("\\n=== COMPARISON ACROSS ALL STYLES ===")
    comparison = show_personality_comparison(base_reply, user_context)
    import json
    print(json.dumps(comparison, indent=2))