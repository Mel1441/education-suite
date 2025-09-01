import pdfplumber
import os

def extract_text_excluding_right_margin(pdf_path, margin_ratio):
    cleaned_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_width = page.width
            crop_box = (0, 0, page_width * margin_ratio, page.height)

            # Crop out margin
            cropped_page = page.crop(bbox=crop_box)
            text = cropped_page.extract_text()

            if text:
                cleaned_text.append(text)

    return "\n".join(cleaned_text)