import re

def chunk_by_grade_headers(text):
    """
    Extracts curriculum chunks between grade-level headers.
    Returns a list of dicts: {grade, chunk}
    """
    # Match headers like "mathematics | Grade 3" or "mathematics | Kindergarten"
    header_pattern = r"(mathematics\s*\|\s*(Kindergarten|Grade\s+\d+))"
    
    # Find all headers and their positions
    headers = []
    for match in re.finditer(header_pattern, text, re.IGNORECASE):
        label = match.group(1).strip()
        grade = match.group(2).strip()
        start_idx = match.start()
        headers.append((grade, start_idx))
    
    # Chunk between headers
    chunks = []
    for i in range(len(headers) - 1):
        grade, start = headers[i]
        end = headers[i + 1][1]
        chunk_text = text[start:end].strip()
        chunks.append({"grade": grade, "chunk": chunk_text})
    
    # Final chunk (Grade 8)
    last_grade, last_start = headers[-1]
    chunks.append({"grade": last_grade, "chunk": text[last_start:].strip()})
    
    return chunks

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