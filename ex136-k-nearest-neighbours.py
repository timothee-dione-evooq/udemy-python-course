from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Charger le jeu de données Iris.
iris = load_iris()

# Diviser le jeu de données en ensembles d'entraînement et de test.
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Créer le classificateur KNN avec k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Entraîner le classificateur
knn.fit(X_train, y_train)

# Prédire sur l'ensemble de test
y_pred = knn.predict(X_test)

# Calculer la précision
accuracy = accuracy_score(y_test, y_pred)

# Afficher la précision
print("Précision sur l'ensemble de test:", accuracy)<<.