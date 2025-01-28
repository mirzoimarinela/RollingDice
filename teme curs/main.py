from data_processor import read_csv, filter_data, write_csv

# Citește datele din fișierul CSV
data = read_csv('people.csv')

# Demonstrarea conținutului citit din fișierul CSV
print("Datele citite din fișier:")
for row in data:
    print(row)

# Filtrează datele pentru orașul 'New York'
filtered_data = filter_data(data, 'City', 'New York')

# Demonstrarea datelor filtrate
print("\nDatele filtrate pentru orașul New York:")
for row in filtered_data:
    print(row)

# Scrie datele filtrate într-un nou fișier CSV
write_csv(filtered_data, 'filtered_people.csv')

# Confirmă că datele au fost scrise
print("\nDatele filtrate au fost scrise în fișierul 'filtered_people.csv'")
