from PyPDF2 import PdfReader
from .skills_extractor import extract_skills_from_text

def extract_text_from_pdf(file_like):
    reader = PdfReader(file_like)
    text = []
    for p in reader.pages:
        try:
            text.append(p.extract_text() or '')
        except Exception:
            continue
        return '\n'.join(text)
    
def extract_skills_from_resume(file_like, use_fuzzy=False):
    text = extract_text_from_pdf(file_like)
    skills = extract_skills_from_text(text, use_fuzzy=use_fuzzy)
    return skills

