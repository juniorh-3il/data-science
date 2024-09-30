# importations des librairies
import pandas as pd
from scipy.stats import ttest_1samp as ttest
from matplotlib import pyplot as plt
import statsmodels.api as sm

# importation des données
df = pd.read_excel("./DATA/Case-One-sample-t-test.xlsx")
data = df["Price_per_EQ"]

# affichage des 5 premières données
print(df.head())

ttest_result = ttest(data.values, popmean=6.21, alternative="greater")
print(f"{ttest_result.statistic = }")
print(f"{ttest_result.pvalue = }")
print(f"{ttest_result.df = }")

ttest_result = ttest(a=data.values, popmean=6.21, alternative="less")
print(f"{ttest_result.statistic = }")
print(f"{ttest_result.pvalue = }")
print(f"{ttest_result.df = }")

# affichage de l'histrogramme
plt.figure(figsize=(10, 5))
data.hist(bins=30)

# affichage du qq-plot
fig, ax = plt.subplots(figsize=(6,6))
sm.qqplot(data, line='s', ax=ax, fmt='b')
ax.set_title("Q-Q plot")
plt.show()