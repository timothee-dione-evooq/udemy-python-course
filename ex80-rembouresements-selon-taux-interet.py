montant_initial = 5000
années = 5
taux_interet = [0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]

montants_totaux = [
    montant_initial * (1 + taux) ** années for taux in taux_interet
]

print(montants_totaux)