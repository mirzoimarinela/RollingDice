# main.py

import math_operations

# Citirea valorilor de la tastatură
a = float(input("Introdu primul numar: "))
b = float(input("Introdu al doilea numar: "))

# Apelarea funcțiilor din modulul math_operations
print(f"Adunare: {math_operations.adunare(a, b)}")
print(f"Scădere: {math_operations.scadere(a, b)}")
print(f"Înmulțire: {math_operations.inmultire(a, b)}")
print(f"Împărțire: {math_operations.impartire(a, b)}")