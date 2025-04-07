ages = (('Noémie', 42), ('Lucas', 25), ('Paul', 31), ('Julien', 26), ('Lucie', 22), ('Antoine', 30), ('Matthieu', 29), ('Nicolas', 36))

def check_age(person):
    return person[1]

ages_croissants = sorted(ages, key=check_age)
print(f'Les âges par ordre croissant: {ages_croissants}')
ages_decroissants = sorted(ages, key=check_age, reverse=True)
print(f'Les âges par ordre décroissant: {ages_decroissants}')