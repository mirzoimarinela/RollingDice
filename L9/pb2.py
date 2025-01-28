import math

class Shape:
    def area(self):
        """Metodă pentru calcularea ariei formei geometrice."""
        raise NotImplementedError("Subclasa trebuie să implementeze metoda area().")

class Circle(Shape):
    def __init__(self, radius):
        """Inițializează un cerc cu raza specificată."""
        self.radius = radius

    def area(self):
        """Calculează aria cercului."""
        return math.pi * self.radius ** 2

    def _str_(self):
        """Reprezentare textuală a cercului."""
        return f"Circle with radius {self.radius} has area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        """Inițializează un dreptunghi cu lățimea și înălțimea specificate."""
        self.width = width
        self.height = height

    def area(self):
        """Calculează aria dreptunghiului."""
        return self.width * self.height

    def _str_(self):
        """Reprezentare textuală a dreptunghiului."""
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area():.2f}"

# Exemplu de utilizare cu introducere de la tastatură:
if __name__ == "__main__":
    while True:
        print("\nAdaugă o formă geometrică:")
        tip = input("Tip (Circle/Rectangle): ").strip().lower()

        if tip == "circle":
            radius = float(input("Introdu raza cercului: "))
            cerc = Circle(radius)
            print(cerc)

        elif tip == "rectangle":
            width = float(input("Introdu lățimea dreptunghiului: "))
            height = float(input("Introdu înălțimea dreptunghiului: "))
            dreptunghi = Rectangle(width, height)
            print(dreptunghi)

        else:
            print("Tip invalid. Te rog să alegi Circle sau Rectangle.")

        continua = input("Dorești să adaugi altă formă? (da/nu): ").strip().lower()
        if continua != "da":
            print("Ieșire. La revedere!")
            break