def citeste_si_calculeaza_suma(nume_fisier):
    """Citește un fișier text cu numere și calculează suma acestora.

    Args:
        nume_fisier (str): Numele fișierului text de citit.

    Returns:
        str: Suma numerelor sau un mesaj de eroare, dacă există probleme.
    """
    try:
        with open(nume_fisier, 'r') as fisier:
            suma = 0
            for linie in fisier:
                try:
                    numar = float(linie.strip())
                    suma += numar
                except ValueError:
                    return f"Eroare: '{linie.strip()}' nu este un număr valid."
            return f"Suma numerelor din fișier este: {suma}"
    except FileNotFoundError:
        return f"Eroare: Fișierul '{nume_fisier}' nu a fost găsit."
    except IOError:
        return f"Eroare: A apărut o problemă la citirea fișierului '{nume_fisier}'."

# Exemplu de utilizare:
if __name__ == "__main__":
    while True:
        nume_fisier = input("Introdu numele fișierului text: ").strip()
        rezultat = citeste_si_calculeaza_suma(nume_fisier)
        print(rezultat)

        continua = input("Dorești să încerci alt fișier? (da/nu): ").strip().lower()
        if continua != "da":
            print("Ieșire. La revedere!")
            break