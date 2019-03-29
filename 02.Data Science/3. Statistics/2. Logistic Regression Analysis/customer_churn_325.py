#로지스틱 모델을 통해 이탈고객 예측하기

import numpy as np
import pandas as pd
import statsmodels.api as sm


churn = pd.read_csv('churn.csv', sep = ',', header = 0)
churn.columns = [heading.lower() for heading in \
                 churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']
dependent_variable = churn['churn01']
independent_variables = churn[['account_length','custserv_calls','total_charges']]
independent_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_constant).fit()

new_observations=churn.loc[churn.index.isin(range(len(churn))), independent_variables.columns]
new_observations_constant=sm.add_constant(new_observations,prepend=True)
y_predicted = logit_model.predict(new_observations_constant)
y_predicted_rounded=[round(score,0) for score in y_predicted]
logistic_predicted_value_list=[]
false_on=0
all_on=0
for predict_value in y_predicted_rounded:
    if predict_value == 0.0:
        logistic_predicted_value_list.append(False)

    else:
        logistic_predicted_value_list.append(True)
for i in logistic_predicted_value_list:
    i=str(i) + '.'
    if i== churn['churn'][all_on]:
        false_on += 1
    all_on += 1

print("정답률 %.2f%%"%((false_on/all_on)*100))