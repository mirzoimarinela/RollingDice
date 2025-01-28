def count_word_occurrences(sentence):
    # Normalizează textul la litere mici și elimină punctuația
    import re
    sentence = re.sub(r'[^\w\s]', '', sentence.lower())

    # Împarte propoziția în cuvinte
    words = sentence.split()

    # Creează un dicționar pentru a număra aparițiile fiecărui cuvânt
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


# Exemplu de utilizare
if _name_ == "_main_":
    sentence = input("Introduceți o propoziție: ")
    word_count = count_word_occurrences(sentence)

    print("\nAparițiile fiecărui cuvânt:")
    for word, count in word_count.items():
        print(f"'{word}': {count} ori")