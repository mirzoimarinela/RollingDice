import math
from functools import lru_cache  # Pentru optimizarea Fibonacci

# Funcție pentru calculul Fibonacci utilizând memoization optimizat
@lru_cache(maxsize=None)
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Inputul trebuie să fie un număr întreg.")
    if n < 0:
        raise ValueError("Fibonacci nu este definit pentru numere negative.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Funcție pentru calculul ariei unui cerc cu validare robustă
def circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Raza trebuie să fie un număr.")
    if radius < 0:
        raise ValueError("Raza nu poate fi negativă.")
    return math.pi * radius ** 2


# Funcție pentru găsirea valorii maxime într-o listă (iterativ)
def find_max(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Inputul trebuie să fie o listă.")
    if not numbers:
        raise ValueError("Lista nu poate fi goală.")
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value

# Funcție pentru calculul mediei geometrice
def geometric_mean(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Inputul trebuie să fie o listă.")
    if not numbers:
        raise ValueError("Lista nu poate fi goală.")
    if any(num <= 0 for num in numbers):
        raise ValueError("Toate numerele trebuie să fie strict pozitive pentru media geometrică.")
    product = 1
    for num in numbers:
        product *= num
    return product ** (1 / len(numbers)

# Funcția principală pentru demonstrarea operațiilor
def main():
    print("=== Fibonacci ===")
    n = 10  # Un caz realist pentru testare
    try:
        print(f"A {n}-a valoare din seria Fibonacci este: {fibonacci(n)}")
    except (ValueError, TypeError) as e:
        print(f"Eroare Fibonacci: {e}")

    print("\n=== Aria Cercului ===")
    radius = 5  # Testare cu o rază validă
    try:
        print(f"Aria unui cerc cu raza {radius} este: {circle_area(radius)}")
    except (ValueError, TypeError) as e:
        print(f"Eroare Circle Area: {e}")

    print("\n=== Maxim din Listă ===")
    numbers = [3, 1, 4, 1, 5, 9]  # Caz realist pentru testare
    try:
        print(f"Valoarea maximă din lista {numbers} este: {find_max(numbers)}")
    except (ValueError, TypeError) as e:
        print(f"Eroare Find Max: {e}")

    print("\n=== Media Geometrică ===")
    numbers = [1, 2, 3, 4]  # Caz realist pentru testare
    try:
        print(f"Media geometrică a numerelor {numbers} este: {geometric_mean(numbers)}")
    except (ValueError, TypeError) as e:
        print(f"Eroare Geometric Mean: {e}")

if __name__ == "_main_":
    main()