import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
# import statsmodels.formula.api as smf
from statsmodels.formula.api import ols,glm

wine= pd.read_csv('winequality-both.csv', sep=',',header=0)
wine.columns = wine.columns.str.replace(" ",'_')

# print(wine.head(100))
# print(wine.head(25))
# print("="*80+"\n")

my_formula = 'quality ~ alcohol + chlorides + citric_acid + citric_acid + density + fixed_acidity + ' \
             'free_sulfur_dioxide + pH +residual_sugar +sulphates + total_sulfur_dioxide + volatile_acidity'
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality','type','in_sample'])]
independent_variables_standardized = (independent_variables-independent_variables.mean())/independent_variables.std()

wine_standardized = pd.concat([dependent_variable,independent_variables_standardized],axis=1)
print(wine_standardized)
lm_standardised = ols(my_formula, data= wine_standardized).fit()
print(lm_standardised.summary())

