# importations des librairies
import pandas as pd
from scipy.stats import chi2_contingency as c2c

# importation des données
df = pd.read_excel("./DATA/Case-Chi-square-test-of-independence.xlsx")

# affichage des 5 premières données
print(df.head())

# génération d'un tableau de contingence
crosstab = pd.crosstab(df["Uniqueness"], df["Purchase Likelihood"])

# affichage du tableau de contingence
print(crosstab)

# calcul et afficage de la statistique du test, de p, du degré de liberté et les fréquences attendues
stat, p, dof, expected = c2c(crosstab)
print(f"{stat = }")
print(f"{p = }")
print(f"{dof = }")
print(f"{expected = }")