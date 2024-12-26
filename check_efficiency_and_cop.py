def check_efficiency_and_cop(text):
    """Check if efficiency and COP meet the required criteria."""
    result = {}

    # Efficacité énergétique
    classe_energ = re.search(r'(Efficacité énergétique|Classe énergétique)\s*:\s*(\d+)%', text)
    profile_souterage = re.search(r'Profil de soutirage selon EN16147\s*:\s*classe\s*(\w+)', text, re.IGNORECASE)

    if classe_energ and profile_souterage:
        efficiency = int(classe_energ.group(1))
        profile = profile_souterage.group(1).upper()

        if profile == 'M':
            result['Efficacité énergétique conforme'] = efficiency >= 95
        elif profile == 'L':
            result['Efficacité énergétique conforme'] = efficiency >= 100
        elif profile == 'XL':
            result['Efficacité énergétique conforme'] = efficiency >= 110
        else:
            result['Efficacité énergétique conforme'] = False
        result['Efficacité énergétique (%)'] = efficiency
        result['Profil de soutirage'] = profile
    else:
        result['Efficacité énergétique conforme'] = None
        result['Efficacité énergétique (%)'] = None
        result['Profil de soutirage'] = None

    # COP de l'équipement
    cop_equip = re.search(r'f(COP de l\'équipement|COP{" degrees"},"°C")\s*:\s*(\d+\.?\d*)', text)

    if cop_equip:
        cop = float((cop_equip).group(1))

        # Déterminer le type d'installation en fonction du COP
        if cop >= 2.5:
            installation_type = "sur air extrait"
        elif cop >= 2.4:
            installation_type = "autre"
        else:
            installation_type = "non conforme"


         # Vérifier si le COP est conforme en fonction du type d'installation
        if installation_type == "sur air extrait":
            result['COP conforme'] = cop >= 2.5
        elif installation_type == "autre":
            result['COP conforme'] = cop >= 2.4
        else:
            result['COP conforme'] = False

        result['COP mesuré'] = cop
        result['Type d\'installation'] = installation_type
    
    else:
        result['COP conforme'] = None
        result['COP mesuré'] = None
        result['Type d\'installation'] = None

    return result