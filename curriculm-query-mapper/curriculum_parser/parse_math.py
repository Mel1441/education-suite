import re

def parse_prefix_tag(text: str) -> List[str]:
    """
    Splits curriculum text into atomic objectives using regex heuristics.
    Assumes objectives are numbered or bulleted.
    """
    # Example: matches lines starting with digits or bullets
    grade = 4
    start_pattern = rf"Grade {grade} overview"
    print(start_pattern)
    # Case-insensitive pattern
    # Use non-capturing group or no group at all
    pattern = r"(.*?)\b((?:K|\d{1,2})\.[A-Z]{1,4})\b"

    
    match = re.search(pattern, text)
    if match:
        prefix = match.group(1).strip()
        tag = match.group(2)
        print("Prefix:", prefix)
        print("Tag:", tag)

    matches = re.findall(pattern, text, flags=re.IGNORECASE)#flags=re.MULTILINE
    return matches