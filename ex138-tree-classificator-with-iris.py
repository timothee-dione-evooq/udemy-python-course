from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Charger le jeu de données Iris.
iris = load_iris()

# Diviser le jeu de données en ensembles d'entraînement et de test.
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# Créer et entraîner le classificateur d'arbre de décision.
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Prédire les étiquettes sur l'ensemble de test.
y_pred = clf.predict(X_test)