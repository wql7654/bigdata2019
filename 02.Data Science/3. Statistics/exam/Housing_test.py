import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import statsmodels.api as sm
# import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm
import math
import matplotlib.pyplot as plt

Housing = pd.read_csv('Housing.csv', sep = ',', header = 0)

Housing.columns = [heading.lower() for heading in \
                   Housing.columns]

Housing['driveway01'] = np.where(Housing['driveway'] == 'yes', 1., 0.)
Housing['recroom01'] = np.where(Housing['recroom'] == 'yes', 1., 0.)
Housing['fullbase01'] = np.where(Housing['fullbase'] == 'yes', 1., 0.)
Housing['gashw01'] = np.where(Housing['gashw'] == 'yes', 1., 0.)
Housing['airco01'] = np.where(Housing['airco'] == 'yes', 1., 0.)
Housing['prefarea01'] = np.where(Housing['prefarea'] == 'yes', 1., 0.)

dependent_variable = Housing['price']
independent_variables = Housing[Housing.columns.difference(['price', 'driveway', 'recroom','fullbase', \
                                                            'gashw', 'airco', 'prefarea'])]

my_formula = 'price ~ lotsize + bedrooms + bathrms + stories + driveway01 + recroom01 + ' \
             'fullbase01 + gashw01 + airco01 + garagepl + prefarea01'
lm = ols(my_formula, data=Housing).fit_regularized()

# 표준화
independent_variables_standardized = (independent_variables-independent_variables.mean())/independent_variables.std()
Housing_standardized = pd.concat([dependent_variable,independent_variables_standardized],axis=1)
lm_standardised = ols(my_formula, data= Housing_standardized).fit()
print("\nCoefficients:\n%s" %lm_standardised.params)
print(lm_standardised.summary())
print(sm.stats.anova_lm(lm_standardised))



# 실제값
Housing_price = [Housing['price'][i] for i in range(10)]

# 예측값
new_observations = Housing.ix[Housing.index.isin(range(10)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score,2) for score in y_predicted]

correct = 0
incorrect = 0
print('\n빅데이터 분석')
for i in range(10):
    print('%d번째 샘플링 데이터 예측 결과: %.2f, 실제 가격: %.1f ' %(i, y_predicted_rounded[i], Housing_price[i]), end='')
    confidence_interval = [Housing_price[i]*0.8, Housing_price[i]*1.2]
    if y_predicted_rounded[i] >= confidence_interval[0] and y_predicted_rounded[i] <= confidence_interval[1] :
        print('=> 정답')
        correct += 1
    else:
        print('=> 오답')
        incorrect += 1

print('\n<분석 결과 요약>')
print('관측계수: %d' % len(y_predicted_rounded))
print("예측값 정답 허용 범위: 실제값의 +- 20.0%")
print("정답률: %d / %d = %.1f" %(correct, len(y_predicted_rounded),correct/len(y_predicted_rounded)*100), end='')
print('%')