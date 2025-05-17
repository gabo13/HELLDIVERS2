from PIL import Image
import os

# Beállítások
sorok = 8
oszlopok = 10
mappa = 'kicsinyitett_kepek/'  # ahol a képek vannak
kimenet_fajl = 'output.png'

# Csak PNG fájlokat keresünk
fajlok = [f for f in os.listdir(mappa) if f.lower().endswith('.png')]

# Dátum szerinti rendezés (fájl módosítási ideje szerint)
fajlok.sort(key=lambda f: os.path.getmtime(os.path.join(mappa, f)))

# Ellenőrizzük a képszámot
if len(fajlok) > sorok * oszlopok:
    raise ValueError("Túl sok kép: legfeljebb 80 képet tudsz elhelyezni.")

# Első kép betöltése a méret meghatározásához
elso_kep = Image.open(os.path.join(mappa, fajlok[0]))
szelesseg, magassag = elso_kep.size

# Új, üres kép létrehozása (átlátszó háttérrel)
mozaik = Image.new('RGBA', (oszlopok * szelesseg, sorok * magassag), (0, 0, 0, 0))

# Képek elhelyezése a rácsban
for index, fajlnev in enumerate(fajlok):
    sor = index // oszlopok
    oszlop = index % oszlopok
    kep = Image.open(os.path.join(mappa, fajlnev))
    mozaik.paste(kep, (oszlop * szelesseg, sor * magassag))

# Kép mentése
mozaik.save(kimenet_fajl)
print(f"A mozaikkép elkészült: {kimenet_fajl}")
