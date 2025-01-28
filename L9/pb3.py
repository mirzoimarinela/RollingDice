class Employee:
    def __init__(self, name, salary):
        """Inițializează un nou obiect Employee cu nume și salariu."""
        self.name = name
        self.salary = salary

    def get_details(self):
        """Returnează detalii despre angajat."""
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def _init_(self, name, salary, department):
        """Inițializează un nou obiect Manager cu nume, salariu și departament."""
        super()._init_(name, salary)
        self.department = department

    def get_details(self):
        """Returnează detalii despre manager, incluzând departamentul."""
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"

# Exemplu de utilizare cu introducere de la tastatură:
if __name__ == "__main__":
    while True:
        print("\nAdaugă un angajat sau manager:")
        tip = input("Tip (Employee/Manager): ").strip().lower()

        if tip == "employee":
            name = input("Introdu numele angajatului: ")
            salary = float(input("Introdu salariul angajatului: "))
            emp = Employee(name, salary)
            print(emp.get_details())

        elif tip == "manager":
            name = input("Introdu numele managerului: ")
            salary = float(input("Introdu salariul managerului: "))
            department = input("Introdu departamentul managerului: ")
            mgr = Manager(name, salary, department)
            print(mgr.get_details())

        else:
            print("Tip invalid. Te rog să alegi Employee sau Manager.")

        continua = input("Dorești să adaugi altă persoană? (da/nu): ").strip().lower()
        if continua != "da":
            print("Ieșire. La revedere!")
            break