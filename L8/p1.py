import math

def calculeaza_racina_factorial_sinus(num, angle):
    # 1. Calcularea rădăcinii pătrate a unui număr
    radacina = math.sqrt(num)

    # 2. Calcularea factorialului unui număr
    factorial = math.factorial(num)

    # 3. Calcularea sinusului unui unghi în grade
    # Convertim unghiul din grade în radiani
    radiani = math.radians(angle)
    sinus = math.sin(radiani)

    # Afișarea rezultatelor
    print(f"Rădăcina pătrată a {num} este {radacina}")
    print(f"Factorialul lui {num} este {factorial}")
    print(f"Sinusul unghiului de {angle} grade este {sinus}")

# Introducerea valorilor
num = int(input("Introduceți un număr pentru calcularea rădăcinii și a factorialului: "))
angle = float(input("Introduceți un unghi în grade pentru calcularea sinusului: "))

# Apelarea funcției
calculeaza_racina_factorial_sinus(num, angle)