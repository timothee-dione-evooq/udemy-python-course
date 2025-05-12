# Listes de noms et d'âges
names = ["Alice", "Bob", "Eve"]
ages = [30, 25, 22]

# Itérer sur les deux listes en parallèle avec zip
for name, age in zip(names, ages):
    print(f"{name} - {age}")