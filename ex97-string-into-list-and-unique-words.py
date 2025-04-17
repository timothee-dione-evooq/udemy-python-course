# Définir la chaîne de caractères initiale.
description = "Freelance, CDI, Freelance, Stage, CDD, CDD, CDI, CDI, Freelance, Stage, Stage, CDI"
words = description.split(', ')
n_unique_words = len(set(words))
print(n_unique_words)