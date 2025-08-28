import re

def parse_prefix_tag(text: str) -> List[str]:
    """
    Splits curriculum text into atomic objectives using regex heuristics.
    Assumes objectives are numbered or bulleted.
    """
    # Example: matches lines starting with digits or bullets
    # Case-insensitive pattern
    # Use non-capturing group or no group at all
    pattern = r"(.*?)\b((?:K|\d{1,2})\.[A-Z]{1,4})\b"

    matches = re.findall(pattern, text, flags=re.IGNORECASE)#flags=re.MULTILINE
    return matches


def extract_domain_chunks(text):
    """
    Extracts curriculum domain blocks from a standards document.
    Returns a list of tuples: (domain_header, domain_text)
    """
    domain_pattern = r"(.*?)\b((?:K|\d{1,2})\.[A-Z]{1,4})\b"
    
    # Find all domain headers and their positions
    headers = []
    for match in re.finditer(domain_pattern, text, flags=re.IGNORECASE):
        label = match.group(0).strip()       
        start_idx = match.start()
        headers.append((label, start_idx))

        print(headers)
    # Chunk between headers
    chunks = []
    for i in range(len(headers) - 1):
        label, start = headers[i]
        end = headers[i + 1][1]
        chunk = text[start:end].strip()
        chunks.append((label, chunk))
    
    # Final chunk (last domain)
    last_label, last_start = headers[-1]
    chunks.append((last_label, text[last_start:].strip()))
    
    return chunks