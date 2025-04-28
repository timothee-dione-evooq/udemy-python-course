import csv
from collections import Counter

counter = Counter()
# Lire et afficher le contenu du fichier CSV.
with open("animals.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row:
            animal_type = row[0].strip()  # récupérer le type d'animal
            counter[animal_type] += 1
    print(counter)