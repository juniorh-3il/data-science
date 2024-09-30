# importations des librairies
import pandas as pd

# importation des données
df = pd.read_excel("./DATA/Case-Chi-square-test-of-independence.xlsx")

# affichage des 5 premières données
print(df.head())

# génération d'un tableau de contingence
crosstab = pd.crosstab(df["Uniqueness"], df["Purchase Likelihood"])

# affichafge du tableau de contingence
print(crosstab)