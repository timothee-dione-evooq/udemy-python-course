from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# Charger le jeu de données Iris.
iris = load_iris()

# Créer le classificateur K-Nearest Neighbors avec k=3.
knn = KNeighborsClassifier(n_neighbors=3)

# Utiliser la validation croisée avec 5 plis pour évaluer le modèle.
scores = cross_val_score(knn, iris.data, iris.target, cv=5)

# Calculer et afficher la précision moyenne.
average_score = scores.mean()
print(f"Précision moyenne avec la validation croisée: {average_score}")
