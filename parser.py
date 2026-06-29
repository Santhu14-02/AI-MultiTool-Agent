import json
import re


def parse_json(text):
    """
    Extracts and parses the first JSON object from the model output.
    """

    text = text.strip()

    # Try direct JSON parsing
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Extract the first JSON object if extra text exists
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    raise ValueError(f"Invalid JSON returned by model:\n{text}")