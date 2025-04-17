prix_voitures = [
    {'Marque': 'Lamborghini', 'Modèle': 'Huracan', 'Prix': 203520},
    {'Marque': 'Lamborghini', 'Modèle': 'Urus', 'Prix': 205715},
    {'Marque': 'Porsche', 'Modèle': 'Cayman', 'Prix': 70635},
    {'Marque': 'Lamborghini', 'Modèle': 'Aventador', 'Prix': 210645},
    {'Marque': 'Porsche', 'Modèle': '911 GT3', 'Prix': 182167}
]

porshes = (list(filter(lambda x: x['Marque'] == 'Porsche', prix_voitures)))
print(porshes)