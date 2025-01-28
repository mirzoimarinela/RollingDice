def count_words_in_file():
    file_name = input("Introduceți numele fișierului: ")

    try:
        # Deschidem fișierul în mod citire
        with open(file_name, 'r') as file:
            # Citim conținutul fișierului
            content = file.read()

            # Împărțim conținutul în cuvinte
            words = content.split()

            # Returnăm numărul de cuvinte
            return len(words)

    except FileNotFoundError:
        return f"Fișierul {file_name} nu a fost găsit."
    except Exception as e:
        return f"A apărut o eroare: {str(e)}"


# Apelarea funcției
result = count_words_in_file()
print("Numărul total de cuvinte este:", result)