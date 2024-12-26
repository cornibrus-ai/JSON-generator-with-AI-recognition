#gérer l’extraction et la structuration des informations en fonction des variations de champ de chaque pdf

import re

def extract_information(text):

    if not isinstance(text, str):
        raise ValueError(f"Le texte passé n\'est pas une chaine valide : {type(text)}")

    # Mention explicite « Devis »
    mention_devis = re.search(r'(Devis n°|Devis)\s*:\s*(.*)', text)

    # Nom et prénom du client
    nom_client = re.search(r'(Nom du client|Nom client|Chantier|Client|Nom)\s*:\s*(.*)', text)

    # Adresse de facturation
    adresse_facturation = re.search(r'(Adresse de facturation|Facturation|Adresse)\s*:\s*(.*)', text)

    # Adresse des travaux
    adresse_travaux = re.search(r'(Adresse des travaux|Travaux|Adresse)\s*:\s*(.*)', text)

    # Dénomination sociale, forme juridique, capital social et SIRET
    siret = re.search(r'\bSIRET\s*:\s*(\d{14})', text)
    denom_sociale = re.search(r'Dénomination sociale\s*:\s*(.*?)(?:\s*Forme juridique|$)', text, re.DOTALL)
    forme_jurid = re.search(r'Forme juridique\s*:\s*(.*?)(?:\s*Capital|$)', text, re.DOTALL)

    # Adresse du siège social
    adresse_siege_social = re.search(r'(Siège social|Adresse du siège)\s*:\s*(.*)', text)

    # Numéro de TVA intracommunautaire
    num_tva_intracom = re.search(r'(Numéro TVA|Numéro TVA Intracommunautaire|TVA intracommunautaire)\s*:\s*(.*)', text)

    # Qualification RGE
    qualif_rge = re.search(r'Qualification RGE\s*:\s*(.*)', text)

    # Date d'émission du devis
    date_emission_devis = re.search(r'Date d\'émission\s*:\s*(\d{2}/\d{2}/\d{4})', text)

    # Date de pré-visite technique
    date_previsite_tech = re.search(r'Date de pré-visite technique\s*:\s*(\d{2}/\d{2}/\d{4})', text)

    # Date prévisionnelle du début des travaux
    date_prev_debut_travaux = re.search(r'Début des travaux\s*:\s*(\d{2}/\d{2}/\d{4})', text)

    # Validité du devis
    valid_devis = re.search(r'Validité du devis\s*:\s*(.*)', text)

    # Décompte détaillé
    decompte = re.search(r'Décompte détaillé\s*:\s*(.*)', text, re.DOTALL)

    # Prix horaire ou forfaitaire main d'œuvre
    prix_horaire_forfait = re.search(r'Prix main d\'œuvre\s*:\s*(.*)', text)

    # Montant global HT et TTC
    montants_globaux = {
        montant_ht : re.search(r'(Montant total HT)\s*:\s*([0-9,.]+)', text),
        montant_ttc : re.search(r'(Montant total TTC)\s*:\s*([0-9,.]+)', text)
    }

    # Intitulé des travaux de « Mise en place d’une Pompe à chaleur »
    install_pompe_chaleur = re.search(r'(Pompe à chaleur|Mise en place d\'un chauffe-eau thermodynamique individuel à accumulation).*:\s*(.*)', text)

    # Marque et référence du chauffe-eau
    brand_ref_chauffe_eau = re.search(r'(Marque et référence|Modèle|Marque commerciale)\s*:\s*(.*)', text)

    data = {
        "Devis": mention_devis.group(2).strip() if mention_devis else None,

        "Nom et prénom du client": nom_client.group(2).strip() if nom_client else None,

        "Adresse de facturation": adresse_facturation.group(2).strip() if adresse_facturation else None,

        "Adresse des travaux" : adresse_travaux.group(2).strip() if adresse_travaux else (adresse_facturation.group(2).strip() if adresse_facturation else None),

        "Dénomination sociale" : denom_sociale.group(1).strip() if denom_sociale else None,
        "Forme juridique" : forme_jurid.group(1).strip() if forme_jurid else None,
        "Numéro SIRET": siret.group(1).strip() if siret else None,

        "Adresse du siège social" : adresse_siege_social.group(2).strip() if adresse_siege_social else None,

        "Numéro de TVA intracommunautaire" : num_tva_intracom.group(2).strip() if num_tva_intracom else None,

        "Qualification RGE" : qualif_rge.group().strip() if qualif_rge else None,

        "Date d'émission du devis" : date_emission_devis.group(1).strip() if date_emission_devis else None,

        "Date de pré-visite technique" : date_previsite_tech.group(1).strip() if date_previsite_tech else None,

        "Date prévisionnelle du début des travaux" : date_prev_debut_travaux.group(1).strip() if date_prev_debut_travaux else None,

        "Validité du devis" : valid_devis.group().strip() if valid_devis else None,

        "Décompte détaillé de chaque prestation et produit" : decompte.group().strip() if decompte else None,

        "Prix horaire ou forfaitaire de main d'œuvre et éventuels frais de déplacement" : prix_horaire_forfait.group().strip() if prix_horaire_forfait else None,

        "Montant total HT": montants_globaux["montant_ht"].group(2).strip() if montants_globaux["montant_ht"] else None,
        "Montant total TTC": montants_globaux["montant_ttc"].group(2).strip() if montants_globaux["montant_ttc"] else None,

        "Intitulé des travaux" : install_pompe_chaleur.group(2).strip() if install_pompe_chaleur else None,

        "Marque et référence du chauffe-eau thermodynamique" : brand_ref_chauffe_eau.group(2).strip() if brand_ref_chauffe_eau else None,

        "Efficacité énergétique pour le chauffage de l’eau et COP de l’équipement (mesuré conformément aux conditions de la norme EN 16147)" : {
        check_efficiency_and_cop(text)
        }
    }

    return data