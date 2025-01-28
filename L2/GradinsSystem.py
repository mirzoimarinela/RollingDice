def grading_system():
    try:
        score = float(input("Introdu punctajul (0 - 100): "))

        if score < 0 or score > 100:
            print("Eroare: Punctajul trebuie să fie între 0 și 100.")
        elif score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        if 0 <= score <= 100:
            print(f"Punctajul introdus este {score}, iar nota este: {grade}")
    except ValueError:
        print("Eroare: Te rog să introduci un număr valid.")


if _name_ == "_main_":
    grading_system()