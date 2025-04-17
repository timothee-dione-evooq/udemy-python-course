# Importer la bibliothèque Pandas.
import pandas as pd

# Créer un DataFrame.
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva', 'Fred'],
        'Age': [25, 30, 22, 28, 35, 26],
        'Gender': ['F', 'M', 'M', 'F', 'F', 'M'],
        'City': ['San Diego', 'Chicago', 'New York', 'San Diego', 'Chicago', 'New York']}
df = pd.DataFrame(data)
#grouped_df = df.groupby("Gender")
#for gender, group in grouped_df:
    #print(f"\nGender: {gender}")
    #print(group)
 #   age = group["Age"].mean()
  #  print(f"{gender} {age}")


grouped_df = df.groupby("Gender")["Age"].mean()
print(grouped_df)