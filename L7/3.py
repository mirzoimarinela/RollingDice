def filter_lines(input1_file, output1_file, keyword):
    try:
        # Deschidem fișierul de intrare în mod citire
        with open(input1_file, 'r') as infile:
            # Citim toate liniile din fișier
            lines = infile.readlines()

        # Deschidem fișierul de ieșire în mod scriere
        with open(output1_file, 'w') as outfile:
            # Pentru fiecare linie, verificăm dacă cuvântul cheie există
            for line in lines:
                if keyword in line:
                    # Scriem linia în fișierul de ieșire dacă cuvântul cheie este prezent
                    outfile.write(line)

        print(f"Fișierul a fost procesat și salvat în {ex_file}.")

    except FileNotFoundError:
        print(f"Fișierul {ex_file} nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {str(e)}")


# Exemplu de utilizare:
ex_file = input("Introduceți numele fișierului de intrare: ")
output1_file = input("Introduceți numele fișierului de ieșire: ")
keyword = input("Introduceți cuvântul cheie: ")

filter_lines(ex_file, output1_file, keyword)