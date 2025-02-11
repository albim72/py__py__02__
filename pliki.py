from pathlib import Path
from datetime import datetime
import os
import shutil

# Tworzenie katalogu
katalog = Path("nowy_katalog")
katalog.mkdir(parents=True, exist_ok=True)

# Tworzenie pliku i zapis daty
plik = katalog / "data.txt"
teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with plik.open("w", encoding="utf-8") as f:
    f.write(f"Aktualna data i godzina: {teraz}\n")

# Uzyskanie listy plików w katalogu
files = os.listdir(katalog)
print("Pliki w katalogu:", files)

# Sprawdzenie, czy plik istnieje
if plik.exists():
    print("Plik istnieje.")

# Kopiowanie pliku
skopiowany_plik = katalog / "kopia_data.txt"
shutil.copy(plik, skopiowany_plik)
print("Plik został skopiowany.")

# Iteracja po plikach .txt w katalogu
for file in katalog.glob("*.txt"):
    print("Znaleziony plik:", file)

# Usunięcie skopiowanego pliku
skopiowany_plik.unlink()
print("Skopiowany plik usunięty.")

# Usunięcie katalogu wraz z zawartością
shutil.rmtree(katalog)
print("Katalog usunięty.")
