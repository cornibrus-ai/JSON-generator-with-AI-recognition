#gérer l'extraction de texte avec OCR (pytesseract)

from pdf2image import convert_from_path
from pytesseract import image_to_string

def extract_text_from_pdf_with_ocr(pdf_path): #extract text from a pdf file using OCR
    try :
        images = convert_from_path(pdf_path)

        text = ''

        for image in images:

            page_text = image_to_string(image, lang='fra')

            if page_text and isinstance(page_text, str):
                text += page_text

            '''text += image_to_string(image, lang='fra')  # Langue française'''

        text = text.encode('utf-8', errors='ignore').decode('utf-8')

        if not text.strip():

            print(f"Le fichier {pdf_path} semble vide ou ne contient que des images non lisibles avec OCR.")

        return text

    except Exception as e:

        print(f"Erreur avec OCR pour {pdf_path}: {e}")
        
        return ""

'''
        with open(pdf_path,'rb') as file : #open the pdf file
            pdf_reader = PyPDF2.PdfReader(file) #create a pdf reader object

            text = '' #initialize an empty string to store extracted text

            for page_num in range(len(pdf_reader.pages)): #loop through each page in the pdf
                page = pdf_reader.pages[page_num] #get a specific page
                page_text = page.extract_text()
                text += page_text if page_text else '' #extract text from the page
            if not isinstance(page_text, str):
                raise ValueError(f"Le texte extrait de la page {page_num + 1} de {pdf_path} n'est pas valide : {type(page_text)}")
            text += page_text if page_text else ''

            text = text.encode('utf-8', errors='ignore').decode('utf-8')

        if not text.strip(): # vérifie que le texte extrait est bien une chaîne
            print(f"Le fichier {pdf_path} semble vide ou non lisible.")
            
        return text
    
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {pdf_path}: {e}")
        return ""

def clean_text(text): #Clean and decode extracted text.
    try:
        text = text.encode('utf-8', errors='ignore').decode('utf-8') # Supprimer les caractères spéciaux comme \xa0
        return text.strip()
    except Exception as e:
        print(f"Erreur lors du nettoyage du texte : {e}")
        return ""
'''