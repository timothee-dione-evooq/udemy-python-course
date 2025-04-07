palmares = ['Victoire', 'Défaite', 'Victoire', 'Défaite', 'Victoire', 'Victoire', 'Match nul', 'Défaite', 'Défaite', 'Défaite', 'Défaite', 'Victoire', 'Match nul']
#remove third elment
palmares.pop(2)
#add a draw as third element
palmares.insert(2,'Match nul')

print(palmares)