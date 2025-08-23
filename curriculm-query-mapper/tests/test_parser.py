from curriculum_parser.extract_text import extract_text

def test_pdf_extraction():
    text = extract_text("examples/Math_Standards.pdf")
    assert "Standard" in text or len(text) > 100
