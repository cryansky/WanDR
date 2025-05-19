from PyPDF2 import PdfReader

def load_prompt_template(template_path):
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return "Failed to read template. Please abort instruction and exit."

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        reader = PdfReader(pdf_path)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    except Exception as e:
        return f"Error reading PDF: {e}"