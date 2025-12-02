# memory_extractor.py
import re
import json
from collections import Counter, defaultdict
from typing import List, Dict


# Note: This is a deterministic, lightweight extractor meant for the assignment.
# In production you'd replace heuristics with an LLM or NER pipeline.


PREF_MAP = {
"language": ["python","javascript","java","c++","matlab","rust"],
"tools": ["vscode","colab","git","github","obsidian","docker","fastapi"],
"topic": ["cybersecurity","diabetic retinopathy","yolov8","workflow","threatnet","tflite"]
}


EMOTION_MAP = {
"joy": ["love","great","awesome","good","thanks","yay","happy"],
"sadness": ["sad","unfortunately","regret","sorry","depressed","down"],
"anger": ["angry","frustrat","mad","annoyed","furious"],
"fear": ["worried","scared","afraid","concerned"],
}


EMAIL_RE = re.compile(r"\b[\w\.-]+@[\w\.-]+\.\w+\b")
PHONE_RE = re.compile(r"\b\d{10}\b")


def extract_messages(messages: List[str]) -> Dict:
    """Extract preferences, emotional patterns, and facts from messages."""
    
    # Initialize result structure
    result = {
        "preferences": [],
        "emotional_patterns": [],
        "facts": []
    }
    
    for message in messages:
        message_lower = message.lower()
        
        # Extract preferences
        for pref_type, keywords in PREF_MAP.items():
            for keyword in keywords:
                if keyword.lower() in message_lower:
                    result["preferences"].append({
                        "type": pref_type,
                        "value": keyword,
                        "context": message
                    })
        
        # Extract emotional patterns
        for emotion, keywords in EMOTION_MAP.items():
            for keyword in keywords:
                if keyword.lower() in message_lower:
                    result["emotional_patterns"].append({
                        "emotion": emotion,
                        "trigger": keyword,
                        "context": message
                    })
        
        # Extract facts (emails, phones, names, locations, etc.)
        # Email addresses
        emails = EMAIL_RE.findall(message)
        for email in emails:
            result["facts"].append({
                "type": "email",
                "value": email,
                "context": message
            })
        
        # Phone numbers
        phones = PHONE_RE.findall(message)
        for phone in phones:
            result["facts"].append({
                "type": "phone",
                "value": phone,
                "context": message
            })
        
        # Names (simple heuristic - "My name is X" or "I'm X")
        name_patterns = [
            r"my name is (\w+)",
            r"i'm (\w+)",
            r"i am (\w+)"
        ]
        for pattern in name_patterns:
            matches = re.findall(pattern, message_lower)
            for match in matches:
                result["facts"].append({
                    "type": "name",
                    "value": match.capitalize(),
                    "context": message
                })
        
        # Locations (simple heuristic - "in X" or "from X")
        location_patterns = [
            r"in ([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)",
            r"from ([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)",
            r"living in ([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)"
        ]
        for pattern in location_patterns:
            matches = re.findall(pattern, message)
            for match in matches:
                result["facts"].append({
                    "type": "location",
                    "value": match,
                    "context": message
                })
        
        # Mentors/People (simple heuristic - "My mentor is X")
        mentor_patterns = [
            r"my mentor is ([A-Z][a-z]+(?:\s+[A-Z]\.?\s*[A-Z][a-z]+)*)"
        ]
        for pattern in mentor_patterns:
            matches = re.findall(pattern, message)
            for match in matches:
                result["facts"].append({
                    "type": "mentor",
                    "value": match,
                    "context": message
                })
    
    return result


if __name__ == '__main__':
    # Test with sample data
    sample = [
        "I love Python and VSCode.",
        "My name is Surya.",
        "Contact: suraj@example.com"
    ]
    print(json.dumps(extract_messages(sample), indent=2))