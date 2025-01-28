# Funcție pentru conversie
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Exemplu de utilizare
celsius = float(input("Introduceți temperatura în grade Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C este echivalent cu {fahrenheit}°F.")