from PIL import Image
import os

# Mappák
bemeneti_mappa = os.path.abspath('stratagems/')
print("bm",bemeneti_mappa)
kimeneti_mappa = os.path.abspath('kicsinyitett_kepek/')

# PNG fájlok beolvasása
fajlok = [f for f in os.listdir(bemeneti_mappa) if f.lower().endswith('.png')]
fajlok.sort(key=lambda f: os.path.getmtime(os.path.join(bemeneti_mappa, f)))
if not fajlok:
    raise ValueError("Nincsenek PNG fájlok a megadott mappában.")

# Legkisebb kép méretének meghatározása
meretek = []
for fajl in fajlok:
    kep = Image.open(os.path.join(bemeneti_mappa, fajl))
    meretek.append((kep.width, kep.height))

legkisebb_meret = min(meretek, key=lambda m: m[0] * m[1])
print(f"Legkisebb kép mérete: {legkisebb_meret[0]}×{legkisebb_meret[1]}")

# Kimeneti mappa létrehozása
os.makedirs(kimeneti_mappa, exist_ok=True)

# Képek feldolgozása
for fajl in fajlok:
    eredeti_utvonal = os.path.join(bemeneti_mappa, fajl)
    kimeneti_utvonal = os.path.join(kimeneti_mappa, fajl)

    kep = Image.open(eredeti_utvonal)

    # Ha átlátszó (pl. RGBA), akkor háttérre helyezzük
    if kep.mode in ('RGBA', 'LA'):
        hatter = Image.new("RGB", kep.size, (0, 0, 0))  # fekete háttér
        hatter.paste(kep, mask=kep.split()[-1])  # alfa maszk szerint
        kep = hatter
    else:
        kep = kep.convert("RGB")  # biztos, ami biztos

    # Átméretezés
    kicsinyitett = kep.resize(legkisebb_meret, Image.LANCZOS)
    kicsinyitett.save(kimeneti_utvonal, format='PNG')

    print(f"{fajl} mentve: {legkisebb_meret[0]}×{legkisebb_meret[1]}")

print("Minden kép feldolgozva és elmentve fekete háttérrel.")
