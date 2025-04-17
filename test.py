import csv

# Lire les données depuis le fichier CSV
with open('people.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = sorted(reader, key=lambda row: int(row['Age']))
    print(data)
    for row in data:
        name = row['Name']
        age = row['Age']
        job = row['Job']
        print(f'{name},{age},{job}')