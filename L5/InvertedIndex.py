def inverted_index():
    documents = []

    # Citirea documentelor de la tastatură
    while True:
        doc = input("Introduceți un document (sau 'stop' pentru a opri): ")
        if doc.lower() == 'stop':
            break
        documents.append(doc)

    # Dicționarul pentru indexul inversat
    index = {}

    # Parcurgem fiecare document
    for doc_id, doc in enumerate(documents):
        words = doc.split()  # Despărțim documentul în cuvinte

        # Parcurgem fiecare cuvânt din document
        for word in words:
            word = word.lower()  # Folosim litere mici pentru a evita duplicarea (ex: "Cuvant" și "cuvant")

            # Dacă cuvântul nu este în dicționar, îl adăugăm
            if word not in index:
                index[word] = set()

            # Adăugăm indexul documentului în setul corespunzător cuvântului
            index[word].add(doc_id)

    return index


# Apelarea funcției
result = inverted_index()
print(result)