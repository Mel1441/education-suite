import re

def chunk_grade_text(text, grade_label):
    chunks = []
  
    # Normalize grade code
    grade_code = "K" if "Kindergarten" in grade_label else re.search(r"\d+", grade_label).group()

    # Split into lines
    lines = text.splitlines()

    # Find intro block
    intro_start = next((i for i, line in enumerate(lines) if re.search(rf"mathematics | {grade_label}", line, re.IGNORECASE)), None)
    overview_start = next((i for i, line in enumerate(lines) if re.search(rf"Grade {grade_code} overview", line, re.IGNORECASE)), None)

    if intro_start is not None and overview_start is not None:
        intro_text = "\n".join(lines[intro_start + 1:overview_start]).strip()

    # Find overview block
    domain_line_idx = next((i for i, line in enumerate(lines[overview_start:], start=overview_start)
                            if re.search(rf"\b{grade_code}\.[A-Z]{{1,4}}\b\s*$", line)), None)
    if overview_start is not None and domain_line_idx is not None:
        overview_text = "\n".join(lines[overview_start:domain_line_idx]).strip()

    # Find domain blocks
    domain_pattern = r"(.*?)\b((?:K|[1-8])\.[A-Z]{1,4})\b"   
    
    # Find all domain headers and their positions
    headers = []
    for match in re.finditer(domain_pattern, text, flags=re.IGNORECASE):
        label = match.group(0).strip()
       
        start_idx = match.start()
        headers.append((label, start_idx))

    # Chunk between headers
    domains = []
    for i in range(len(headers) - 1):
        label, start = headers[i]
        end = headers[i + 1][1]
        chunk = text[start:end].strip()
        domains.append({f"{label}":chunk})
    
    # Final chunk (last domain)
    last_label, last_start = headers[-1]
    domains.append({f"{last_label}": text[last_start:].strip()})
    chunks.append({"grade": grade_label, "intro": intro_text, "overview": overview_text, "domains": domains})

    return chunks

def chunk_all_grades(grade_list):
    all_chunks = []
    for entry in grade_list:
        grade = entry["grade"]
        text = entry["chunk"]
        chunks = chunk_grade_text(text, grade)
        all_chunks.extend(chunks)
    return all_chunks