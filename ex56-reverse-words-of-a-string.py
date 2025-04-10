texte = "Apprendre Python est très amusant"
mots = texte.split()
phrase=""
for i in reversed(range(len(mots))):
    phrase = phrase + mots[i]
    if i > 0:
        phrase = phrase + " "
print(phrase)