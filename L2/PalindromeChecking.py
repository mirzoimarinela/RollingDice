def is_palindrome(s):
    # Eliminăm spațiile și convertim la litere mici pentru a ignora diferențele de caz
    s = s.replace(" ", "").lower()

    # Verificăm dacă șirul este egal cu inversul său
    return s == s[::-1]


# Citire de la utilizator
input_string = input("Introdu un cuvânt sau un șir pentru a verifica dacă este palindrom: ")

# Verificare și afișare rezultat
if is_palindrome(input_string):
    print("Este palindrom!")
else:
    print("Nu este palindrom.")