def reverse_lines(input_file, output_file):
    try:
        # Deschidem fișierul de intrare în mod citire
        with open(input_file, 'r') as infile:
            # Citim toate liniile din fișier
            lines = infile.readlines()

        # Deschidem fișierul de ieșire în mod scriere
        with open(output_file, 'w') as outfile:
            # Pentru fiecare linie, inversăm caracterele și o scriem în fișierul de ieșire
            for line in lines:
                reversed_line = line[::-1]  # Inversăm linia
                outfile.write(reversed_line)  # Scriem linia inversată în fișier

        print(f"Fișierul a fost procesat și salvat în {output_file}.")

    except FileNotFoundError:
        print(f"Fișierul {input_file} nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {str(e)}")


# Exemplu de utilizare:
input_file = input("Introduceți numele fișierului de intrare: ")
output_file = input("Introduceți numele fișierului de ieșire: ")

reverse_lines(input_file, output_file)