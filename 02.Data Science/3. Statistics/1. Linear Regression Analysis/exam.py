# import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import statsmodels.api as sm
# import statsmodels.formula.api as smf
from statsmodels.formula.api import ols,glm

print("7.2.7 예측하기")
wine = pd.read_csv('winequality-both.csv', sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

q1='fixed acidity'
q2='volatile acidity'
q3='citric acid'
q4='residual sugar'
q5='chlorides'
q6='free sulfur dioxide'
q7='total sulfur dioxide'
q8='density'
q9='pH'
q10='sulphates'
q11='alcohol'
q12='quality'


my_formula = 'quality ~ alcohol +  chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             ' pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula,data=wine).fit()



dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality','type','in_sample'])]

# print(len(wine))
new_observations = wine.loc[wine.index.isin(range(len(wine))), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score,2) for score in y_predicted]
print(y_predicted_rounded)


ok = 0; total = 0
for idx in y_predicted_rounded:
    p = idx
    if int(p) == 5:
        ok += 1
    total += 1
print("정답률:", ok, "/", total, "=", ok/total)

