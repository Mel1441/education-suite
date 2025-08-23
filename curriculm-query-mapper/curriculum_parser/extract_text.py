import pdfplumber
from bs4 import BeautifulSoup
import os

def extract_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_from_html(html_path):
    if not os.path.exists(html_path):
        raise FileNotFoundError(f"HTML not found: {html_path}")
    with open(html_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        return soup.get_text(separator="\n")

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_from_pdf(file_path)
    elif file_path.endswith(".html") or file_path.endswith(".htm"):
        return extract_from_html(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or HTML.")