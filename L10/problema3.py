def imparte_numere(numar1, numar2):
    """Împarte două numere și gestionează excepția de împărțire la zero."""
    try:
        rezultat = numar1 / numar2
        return f"Rezultatul împărțirii este: {rezultat}"
    except ZeroDivisionError:
        return "Eroare: Împărțirea la zero nu este permisă."

# Exemplu de utilizare:
if __name__ == "__main__":
    while True:
        try:
            numar1 = float(input("Introdu primul număr: "))
            numar2 = float(input("Introdu al doilea număr: "))
            print(imparte_numere(numar1, numar2))
        except ValueError:
            print("Eroare: Te rog să introduci un număr valid.")

        continua = input("Dorești să încerci din nou? (da/nu): ").strip().lower()
        if continua != "da":
            print("Ieșire. La revedere!")
            break