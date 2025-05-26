from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class Regressor:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        mean_error = mean_squared_error(y_test, predictions)
        print(f"Mean squared error: {mean_error}")

# Génération du jeu de données
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)
# Division des données (80% entraînement, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Utilisation de la classe
clf = Regressor()
clf.train(X_train, y_train)
clf.test(X_test, y_test)
