# Funcție pentru a verifica dacă un număr este prim
def este_prim(numar):
    if numar <= 1:
        return False
    for i in range(2, int(numar ** 0.5) + 1):
        if numar % i == 0:
            return False
    return True

# Exemplu de utilizare
numar = int(input("Introduceți un număr: "))
if este_prim(numar):
    print(f"Numărul {numar} este prim.")
else:
    print(f"Numărul {numar} nu este prim.")