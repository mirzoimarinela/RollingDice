def reverse_words():
    # Citirea propoziției de la tastatură
    sentence = input("Introduceți propoziția: ")

    # Îndepărtăm spațiile suplimentare și împărțim propoziția în cuvinte
    words = sentence.strip().split()

    # Inversăm ordinea cuvintelor
    reversed_sentence = ' '.join(reversed(words))

    return reversed_sentence


# Apelarea funcției
result = reverse_words()
print("Propoziția inversată este:", result)