valeurs = [24, 95, 49, 56, 28, 96, 73, 48, 30, 51]

nouvelle_liste = ["Proche de 100" if x > 50 else "Proche de 0" for x in valeurs]
print(nouvelle_liste)