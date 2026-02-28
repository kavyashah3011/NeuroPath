import re

def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.findall(pattern, text)
    return match[0] if match else None

def extract_phone(text):
    pattern = r"\+?\d[\d -]{8,}\d"
    match = re.findall(pattern, text)
    return match[0] if match else None