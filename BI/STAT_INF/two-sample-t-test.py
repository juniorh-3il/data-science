# Two-sample t-test

import pandas as pd
from scipy import stats
from scipy.stats import shapiro, levene

df = pd.read_excel("./DATA/Case-Two-sample-t-test.xlsx")

data_o = df[df["Display Type"] =="Old_display_type"]["Sales Volume"].values # données de l'ancienne disposition
data_n = df[df["Display Type"] =="New_display_type"]["Sales Volume"].values # données de la nouvelle disposition

print("Old display: " + str(shapiro(data_o)))
print("New display: " + str(shapiro(data_n)))

print(stats.levene(data_o, data_n, center='mean'))

print(stats.ttest_ind(data_n, data_o, equal_var=True, alternative = "greater"))