# Funcție pentru a calcula dobânda
def calculeaza_dobanda(principal, rata, timp):
    return (principal * rata * timp) / 100

# Exemplu de utilizare
principal = float(input("Introduceți suma inițială (capitalul principal): "))
rata = float(input("Introduceți rata dobânzii (în procente): "))
timp = float(input("Introduceți timpul (în ani): "))

dobanda = calculeaza_dobanda(principal, rata, timp)
print(f"Dobânda pentru suma {principal} la o rată de {rata}% pe o perioadă de {timp} ani este: {dobanda:.2f}")