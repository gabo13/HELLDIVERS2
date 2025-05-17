import csv
import json

# Bemeneti és kimeneti fájlnevek
csv_fajl = 'stratagems.csv'
json_fajl = 'stratagems.json'

# Üres lista, ahová az adatok kerülnek
adatok = []

# CSV beolvasása
with open(csv_fajl, mode='r', encoding='utf-8') as f:
    olvaso = csv.DictReader(f, delimiter=';')
    for sor in olvaso:
        adatok.append(sor)

# JSON mentése
with open(json_fajl, mode='w', encoding='utf-8') as f:
    json.dump(adatok, f, ensure_ascii=False, indent=4)

print(f"Sikeresen konvertálva: {csv_fajl} → {json_fajl}")
