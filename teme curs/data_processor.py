import csv

def read_csv(file_name):
    """Citește un fișier CSV și returnează conținutul ca o listă de dicționare."""
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def filter_data(data, key, value):
    """Filtrează lista de dicționare pe baza unei perechi cheie-valoare."""
    return [row for row in data if row[key] == value]

def write_csv(data, file_name):
    """Scrie datele filtrate într-un fișier CSV."""
    if data:
        fieldnames = data[0].keys()
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
