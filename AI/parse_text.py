import re

def parse_text_deepseek(text):
    match = re.search(r"<think>(.*?)</think>", text, re.DOTALL)
    if match:
        think_text = match.group(1).strip()  # Extract and remove extra spaces/newlines
        remaining_text = text.replace(match.group(0), "").strip()  # Remove the <think> tag and its content
        return think_text, remaining_text
    return None, text  # Return the original text if no <think> tag is found
    