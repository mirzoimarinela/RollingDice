def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

# Exemplu de utilizare
if _name_ == "_main_":
    num = int(input("Introduceți un număr pentru a calcula factorialul: "))
    if num < 0:
        print("Factorialul nu este definit pentru numere negative.")
    else:
        print(f"Factorialul lui {num} este {calculate_factorial(num)}.")