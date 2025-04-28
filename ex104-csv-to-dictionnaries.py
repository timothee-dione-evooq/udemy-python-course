import csv

# Lire et afficher le contenu du fichier CSV.
with open("input.csv", "r") as file:
    reader = csv.DictReader(file)
    print('Name,Age,Job')
    for row in reader:
        if int(row['Age']) > 24:
            name = row['Name']
            age = row['Age']
            job = row['Job']
            print(f'{name},{age},{job}')