def verifica_paritate(numar):
    if numar % 2 == 0:
        return "par"
    else:
        return "impar"

# Exemplu de utilizare
numar = int(input("Introduceți un număr: "))
paritate = verifica_paritate(numar)
print(f"Numărul {numar} este {paritate}.")