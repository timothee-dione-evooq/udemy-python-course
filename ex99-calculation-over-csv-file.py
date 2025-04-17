import csv
import statistics

# Lire les âges à partir du fichier CSV et calculer la moyenne.
ages = []
with open("input.csv", "r") as file:
    reader = csv.reader(file)
    # Ignorer la première ligne (l'en-tête)
    next(reader)
    for row in reader:
        ages.append(int(row[1]))
ages_moyens =  statistics.mean(ages)
print(f'Age moyen: {ages_moyens}')