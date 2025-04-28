# Créer un dictionnaire qui contient les prix des produits.
prix_produits = {'ordinateur': 1200, 'téléphone': 800, 'tablette': 600, 'casque': 300, 'souris': 50}

seuil = 500

produits_filtrés = {produit: prix for produit, prix in prix_produits.items() if prix > seuil}

print(produits_filtrés)