from text_extraction_pypdf2 import extract_text_from_pdf_with_pypdf2
from text_extraction_pdfplumber import extract_text_from_pdf_with_pdfplumber
#from text_extraction_ocr import extract_text_from_pdf_with_ocr
from data_processing import extract_information
from save_to_json import save_to_json

def try_extraction_methods(pdf_path): #Try multiple extraction methods in order of priority.
    text = extract_text_from_pdf_with_pypdf2(pdf_path)
    if not text.strip():
        print(f"PyPDF2 a échoué, tentative avec pdfplumber pour {pdf_path}")
        text = extract_text_from_pdf_with_pdfplumber(pdf_path)
    if not text.strip():
        print(f"pdfplumber a échoué, tentative avec OCR pour {pdf_path}")
        text = extract_text_from_pdf_with_ocr(pdf_path)
    return text

if __name__ == "__main__" :
    pdf_files = [
    'C:\\Users\\Jeff31\\Desktop\\dossier-test\\Devis_Iso_Pac_BT_VMC.pdf',
    'C:\\Users\\Jeff31\\Desktop\\dossier-test\\Devis_rectifiee_renovation_totale_chauffage_&_production_d_eau_chaude-Mr_Frezard_a_Montauban.pdf',
    'C:\\Users\\Jeff31\\Desktop\\dossier-test\\Devis.CASTELLE.1.pdf'    
    ] #liste des fichiers pdf à traiter

    for pdf_file in pdf_files: 
        try:
            raw_text = try_extraction_methods(pdf_file)  # Extraire le texte du PDF
            
            print(f"Type de texte extrait de : {type(raw_text)}")

            print(f"Texte extrait de {pdf_file} : {raw_text[:300]}")  # Affiche les 300 premiers caractères

            #text = clean_text(text)
            #print(f"Texte nettoyé de {pdf_file} : {text[:300]}")

            if not isinstance(raw_text, str):
                raise ValueError(f"Le texte extrait de {pdf_file} n\'est pas une chaine valide : {type(raw_text)}")
            
            data = extract_information(raw_text),  # Extraire les informations spécifiques
            
            output_file = pdf_file.replace('.pdf', '.json'),  # Créer un nom de fichier JSON
            
            save_to_json(data, output_file),  # Sauvegarder dans un fichier JSON

        except FileNotFoundError:
            print(f"Le fichier {pdf_file} est introuvable.")

        except Exception as e :
            print(f"Une erreur inattendue est survenue lors du traitement de {pdf_file}: {e}")