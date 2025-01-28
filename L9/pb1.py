class BankAccount:
    def __init__(self, sold_initial=0):
        """Inițializează un nou obiect BankAccount cu un sold inițial opțional."""
        self._balance = sold_initial

    def depune(self, suma):
        """Adaugă suma specificată în soldul contului."""
        if suma > 0:
            self._balance += suma
            print(f"Ai depus: {suma:.2f}. Sold nou: {self._balance:.2f}.")
        else:
            print("Suma depusă trebuie să fie pozitivă.")

    def retrage(self, suma):
        """Retrage suma specificată din soldul contului, dacă există fonduri suficiente."""
        if suma > 0:
            if suma <= self._balance:
                self._balance -= suma
                print(f"Ai retras: {suma:.2f}. Sold nou: {self._balance:.2f}.")
            else:
                print("Fonduri insuficiente.")
        else:
            print("Suma retrasă trebuie să fie pozitivă.")

    def obtine_sold(self):
        """Returnează soldul curent al contului."""
        return self._balance

# Exemplu de utilizare:
if __name__ == "__main__":
    sold_initial = float(input("Introdu soldul inițial: "))
    cont = BankAccount(sold_initial)

    while True:
        print("\nOpțiuni:\n1. Depune bani\n2. Retrage bani\n3. Verifică soldul\n4. Ieșire")
        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            suma = float(input("Introdu suma de depus: "))
            cont.depune(suma)
        elif optiune == "2":
            suma = float(input("Introdu suma de retras: "))
            cont.retrage(suma)
        elif optiune == "3":
            print(f"Sold curent: {cont.obtine_sold():.2f}")
        elif optiune == "4":
            print("Ieșire. La revedere!")
            break
        else:
            print("Opțiune invalidă. Te rog să încerci din nou.")