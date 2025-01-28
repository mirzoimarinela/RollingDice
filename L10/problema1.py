class Inventar:
    def __init__(self):
        self.produse = {}

    def adauga_produs(self, nume, cantitate):
        """Adaugă un produs nou sau actualizează cantitatea unui produs existent."""
        try:
            cantitate = int(cantitate)
            if cantitate < 0:
                raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
            if nume in self.produse:
                self.produse[nume] += cantitate
            else:
                self.produse[nume] = cantitate
            print(f"Produsul '{nume}' a fost adăugat/actualizat cu succes.")
        except ValueError as e:
            print(f"Eroare: {e}")

    def cauta_produs(self, nume):
        """Caută un produs după nume."""
        if nume in self.produse:
            return f"Produs: {nume}, Cantitate: {self.produse[nume]}"
        else:
            return f"Eroare: Produsul '{nume}' nu există în inventar."

    def actualizeaza_cantitate(self, nume, cantitate):
        """Actualizează cantitatea unui produs existent."""
        try:
            cantitate = int(cantitate)
            if cantitate < 0:
                raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
            if nume in self.produse:
                self.produse[nume] = cantitate
                print(f"Cantitatea produsului '{nume}' a fost actualizată la {cantitate}.")
            else:
                print(f"Eroare: Produsul '{nume}' nu există în inventar.")
        except ValueError as e:
            print(f"Eroare: {e}")

# Program principal
if __name__ == "__main__":
    inventar = Inventar()

    while True:
        print("\n=== Sistem de Gestionare a Inventarului ===")
        print("1. Adaugă produs")
        print("2. Caută produs")
        print("3. Actualizează cantitatea unui produs")
        print("4. Ieșire")

        optiune = input("Alege o opțiune: ").strip()

        if optiune == "1":
            nume = input("Introdu numele produsului: ").strip()
            cantitate = input("Introdu cantitatea: ").strip()
            inventar.adauga_produs(nume, cantitate)

        elif optiune == "2":
            nume = input("Introdu numele produsului pe care vrei să-l cauți: ").strip()
            print(inventar.cauta_produs(nume))

        elif optiune == "3":
            nume = input("Introdu numele produsului: ").strip()
            cantitate = input("Introdu cantitatea actualizată: ").strip()
            inventar.actualizeaza_cantitate(nume, cantitate)

        elif optiune == "4":
            print("Ieșire. La revedere!")
            break

        else:
            print("Eroare: Opțiune invalidă. Încearcă din nou.")