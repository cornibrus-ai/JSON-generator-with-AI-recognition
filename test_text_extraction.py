from text_extraction_pypdf2 import extract_text_from_pdf_with_pypdf2
from text_extraction_pdfplumber import extract_text_from_pdf_with_pdfplumber
from text_extraction_ocr import extract_text_from_pdf_with_ocr

pdf_path = ('Devis_Iso_Pac_BT_VMC.pdf')
print(extract_text_from_pdf_with_pypdf2(pdf_path))