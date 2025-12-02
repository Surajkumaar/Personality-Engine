# test_extraction.py
import json
import sys
import os

# Add parent directory to path so we can import memory_extractor
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from memory_extractor import extract_messages


def test_extract_sample():
    with open("sample_messages.json", "r") as f:
        messages = json.load(f)
    res = extract_messages(messages)
    assert "preferences" in res
    assert "emotional_patterns" in res
    assert "facts" in res
    # expect at least one preference and one fact
    assert len(res['preferences']) > 0
    assert len(res['facts']) > 0
    

if __name__ == "__main__":
    test_extract_sample()
    print("All tests passed!")