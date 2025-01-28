def find_multiples(number, limit):
    """
    Găsește toți multiplii unui număr până la o limită.
    :param number: Numărul pentru care se găsesc multiplii
    :param limit: Limita superioară
    :return: Lista de multipli
    """
    if number <= 0 or limit <= 0:
        return "Numărul și limita trebuie să fie pozitive."

    multipli = [i for i in range(number, limit + 1, number)]
    return multipli


# Citire de la utilizator
try:
    numar = int(input("Introdu numărul pentru care să găsești multiplii: "))
    limita = int(input("Introdu limita superioară: "))
    rezultat = find_multiples(numar, limita)
    print(f"Multiplii lui {numar} până la {limita} sunt: {rezultat}")
except ValueError:
    print("Te rog să introduci un număr valid.")