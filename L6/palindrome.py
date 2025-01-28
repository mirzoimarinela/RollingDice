def is_palindrome(text):
    # Eliminăm spațiile și facem toate literele mici
    cleaned_text = text.replace(" ", "").lower()

    # Verificăm dacă șirul este egal cu inversul său
    return cleaned_text == cleaned_text[::-1]


# Apelarea funcției
text = input("Introduceți textul: ")
result = is_palindrome(text)
print("Este palindrom:", result)