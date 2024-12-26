import json

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Données sauvegardées dans {output_file}")

    if not data:
        print("Aucune donnée à sauvegarder.")
        
    return