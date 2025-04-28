import re
import string

# Créer une chaîne de caractères qui contient le texte.
texte = "La programmation en Python est à la fois simple et puissante, permettant de créer des applications complexes et variées."
words = re.split(' ',texte)
bigwords=[]

for word in words:
    if len(word) > 5:
        word = word.translate(str.maketrans('', '', string.punctuation))
        bigwords.append(word.lower())

bigwords.sort()
print(bigwords)