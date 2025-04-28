# Importer la bibliothèque SciPy et NumPy
from scipy.stats import norm
import numpy as np

# Fixer la graine aléatoire pour avoir des résultats reproductibles
np.random.seed(42)  # Ne pas toucher à cette ligne de code

# Définir les paramètres de la distribution
moyenne = 50
ecart_type = 10

# Générer 6 nombres aléatoires suivant une distribution normale
nombres_aleatoires = norm.rvs(loc=moyenne, scale=ecart_type, size=6)

# Afficher les 6 nombres générés
print(nombres_aleatoires)