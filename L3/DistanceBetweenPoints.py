import math

def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)

# Exemplu de utilizare
if __name__ == "__main__":
    x1, y1 = map(float, input("Introduceți coordonatele punctului 1 (x1, y1): ").split())
    x2, y2 = map(float, input("Introduceți coordonatele punctului 2 (x2, y2): ").split())
    print(f"Distanța dintre punctele ({x1}, {y1}) și ({x2}, {y2}) este {distance_2d(x1, y1, x2, y2):.2f}")
