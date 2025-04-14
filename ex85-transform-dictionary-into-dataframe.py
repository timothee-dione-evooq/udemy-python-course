# Importer la bibliothèque Pandas.
import pandas as pd

# Créer un dictionnaire.
dictionnaire = {
    'pays': ['France', 'Espagne', 'Allemagne', 'Italie'],
    'capitale': ['Paris', 'Madrid', 'Berlin', 'Rome'],
    'population': [67076000, 46934632, 83019200, 60390560]
}

df = pd.DataFrame(dictionnaire,
    index = [
        x for x in range(
            len(dictionnaire.get("pays"))
        )
    ]
)
print(df)