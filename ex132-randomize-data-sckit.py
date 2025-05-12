from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Charger le jeu de données Iris.
iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Afficher la taille des ensembles
print("Taille de l'ensemble d'entraînement:", len(X_train))
print("Taille de l'ensemble de test:", len(X_test))
