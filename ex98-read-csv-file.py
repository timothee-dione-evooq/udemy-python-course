import csv

# Lire et afficher le contenu du fichier CSV.
with open("input.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(','.join(row))