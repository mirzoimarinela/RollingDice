# main.py

from geometry import aria_cerc, circumferinta, aria_dreptunghi, perimetru

# Calcularea ariei și circumferinței unui cerc
radius = float(input("Introdu raza cercului: "))
print(f"Aria cercului: {aria_cerc(radius)}")
print(f"Circumferința cercului: {circumferinta(radius)}")

# Calcularea ariei și perimetrului unui dreptunghi
lungime = float(input("Introdu lungimea dreptunghiului: "))
latime = float(input("Introdu lățimea dreptunghiului: "))
print(f"Aria dreptunghiului: {aria_dreptunghi(lungime, latime)}")
print(f"Perimetrul dreptunghiului: {perimetru(lungime, latime)}")