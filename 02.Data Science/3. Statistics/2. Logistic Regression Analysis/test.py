#로지스틱 모델을 통해 이탈고객 예측하기

import numpy as np
import pandas as pd
import statsmodels.api as sm
from itertools import combinations


churn = pd.read_csv('churn.csv', sep = ',', header = 0)
churn.columns = [heading.lower() for heading in \
                 churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)


colums_list = ['Area_Code','VMail_Message',
               'Day_Mins','Day_Calls','Day_Charge','Eve_Mins','Eve_Calls','Eve_Charge','Night_Mins',
               'Night_Calls','Night_Charge','Intl_Mins','Intl_Calls','Intl_Charge']

dependent_variable = churn['churn01']

intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
count_all=0
all_time=[]
for num in range(1,18):
    combi_list = list(combinations(colums_list, num))
    for tuple_num in combi_list:
        count=0
        alllist=[]
        for lens_num in tuple_num:
            lens_num=lens_num.lower()
            if count==0 and lens_num=='intl_plan':
                churn['total_charges']=intl_dummies
            elif count!=0 and lens_num=='intl_plan':
                churn['total_charges']=churn['total_charges']+intl_dummies
            elif count==0 and lens_num=='vmail_plan':
                churn['total_charges']=vmail_dummies
            elif count!=0 and lens_num=='vmail_plan':
                churn['total_charges']=churn['total_charges']+vmail_dummies
            if count==0:
                churn['total_charges']=churn[lens_num]
            else:
                churn['total_charges']=churn['total_charges']+churn[lens_num]
            alllist.append(lens_num)
            count += 1

        independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
        independent_constant = sm.add_constant(independent_variables, prepend=True)
        logit_model = sm.Logit(dependent_variable, independent_constant).fit()

        new_observations = churn.loc[churn.index.isin(range(len(churn))), independent_variables.columns]
        new_observations_constant = sm.add_constant(new_observations, prepend=True)
        y_predicted = logit_model.predict(new_observations_constant)
        y_predicted_rounded = [round(score, 0) for score in y_predicted]
        logistic_predicted_value_list = []
        false_on = 0
        all_on = 0
        for predict_value in y_predicted_rounded:
            if predict_value == 0.0:
                logistic_predicted_value_list.append(False)
            else:
                logistic_predicted_value_list.append(True)

        for i in logistic_predicted_value_list:
            i = str(i) + '.'
            if i == churn['churn'][all_on]:
                false_on += 1
            all_on += 1
        print(alllist)
        print("정답률 %.2f%%" % ((false_on / all_on) * 100))
        all_time.append((false_on / all_on) * 100)
        count_all+=1


match_dic = sorted(all_time,reverse=True)
match_dic2 = sorted(all_time,reverse=False)

print(match_dic)
print('총 조합 갯수: %d'%count_all)
print("MAX 조합:",match_dic[0])
print("MAX2 조합:",match_dic2[0])
