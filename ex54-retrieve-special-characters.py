import re
mot_de_passe = 'ePas5d7*dz4d2674ds'

# Expression régulière pour détecter un caractère spécial
caractere_special = re.search(r"[^\w]", mot_de_passe)

if len(mot_de_passe) >= 13 and caractere_special:
    print("Mot de passe sécurisé")
else:
    print("Mot de passe trop court ou ne contient pas de chiffre")