import pandas as pd
import numpy as np
from statsmodels.formula.api import ols,glm
from itertools import combinations
import operator
import re

import statsmodels.api as sm

house = pd.read_csv('Housing.csv', sep=',',header=0)
house.columns = house.columns.str.replace(' ','_')


house['driveway1'] = np.where(house['driveway'] == 'yes', 1., 0.)
house['recroom1'] = np.where(house['recroom'] == 'yes', 1., 0.)
house['fullbase1'] = np.where(house['fullbase'] == 'yes', 1., 0.)
house['gashw1'] = np.where(house['gashw'] == 'yes', 1., 0.)
house['airco1'] = np.where(house['airco'] == 'yes', 1., 0.)
house['prefarea1'] = np.where(house['prefarea'] == 'yes', 1., 0.)

formula=['lotsize','bedrooms','bathrms','stories','driveway1','recroom1','fullbase1','gashw1','airco1','garagepl','prefarea1']

match_dic={}
match_dic2={}
match_dic3={}


err_cnt=0.05
err_cnt2=0.1
err_cnt3=0.2

my_formula='price~ lotsize+	bedrooms+bathrms+stories+driveway1+recroom1+fullbase1+gashw1+airco1+garagepl+prefarea1'
lm = ols(my_formula, data=house).fit()
print("Debug lm.summary()")
print(lm.summary())

for all_house in formula:
    alls = re.compile('''%s\s*(\d+[.]\d+e?[+]?\d?\d?).*'''%all_house)
    alllines = alls.findall(str(lm.summary()), re.MULTILINE | re.DOTALL | re.VERBOSE)
    print(all_house)
    print(alllines)
all = re.compile('''Observations:\s+(\d+)\s+.''')
all2= re.compile('''Residuals:\s+(\d+)\s+.''')
all3= re.compile('''e\s+R-squared:\s+(\d*.\d*)\s+.''')
allline = all.findall(str(lm.summary()), re.MULTILINE | re.DOTALL | re.VERBOSE)
allline2 = all2.findall(str(lm.summary()), re.MULTILINE | re.DOTALL | re.VERBOSE)
allline3 = all3.findall(str(lm.summary()), re.MULTILINE | re.DOTALL | re.VERBOSE)
print(allline)
print(allline2)
print(allline3)


for num in range(1,12):

    combi_list = list(combinations(formula,num))
    for tup in combi_list:
        my_formula = 'price ~ '
        list_data=[]
        for data in tup:
            my_formula+='%s + '%data
            list_data.append(data)
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=house).fit()
        dependent_variable = house['price']
        independent_variables = house[list(tup)] # formula 에 들어간 columns만 골라서 고정 변수로 줌
        y_predicted = lm.predict(independent_variables)
        y_predicted_rounded=y_predicted

        match_count=0
        match_count1=0
        match_count2=0
        match_count0=0

        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] < (dependent_variable.values[index]*err_cnt)+dependent_variable.values[index] \
                and y_predicted_rounded[index] > dependent_variable.values[index]-(dependent_variable.values[index]*err_cnt):
                match_count+=1
            if y_predicted_rounded[index] < (dependent_variable.values[index]*err_cnt2)+dependent_variable.values[index] \
                and y_predicted_rounded[index] > dependent_variable.values[index]-(dependent_variable.values[index]*err_cnt2):
                match_count1+=1
            if y_predicted_rounded[index] < (dependent_variable.values[index]*err_cnt3)+dependent_variable.values[index] \
                and y_predicted_rounded[index] > dependent_variable.values[index]-(dependent_variable.values[index]*err_cnt3):
                match_count2+=1
            if y_predicted_rounded[index]==dependent_variable[index]:
                match_count0+=1

        print('\n>> ',list_data)
        print('>> match count=',match_count0)
        print('>> 정답률: %.2f %%'%(match_count0/len(y_predicted_rounded)*100))
        print('>> match count=',match_count)
        print('>> 정답률: %.2f %%'%(match_count/len(y_predicted_rounded)*100))
        print('>> match count=', match_count1)
        print('>> 정답률: %.2f %%' % (match_count1 / len(y_predicted_rounded) * 100))
        print('>> match count=', match_count2)
        print('>> 정답률: %.2f %%' % (match_count2 / len(y_predicted_rounded) * 100))

        match_dic['%s' % list_data] = match_count / len(y_predicted_rounded) * 100
        match_dic2['%s' % list_data] = match_count1 / len(y_predicted_rounded) * 100
        match_dic3['%s' % list_data] = match_count2 / len(y_predicted_rounded) * 100
        # match_dic['%s' % list_data] = '.2f %%%' % (
        #             match_count / len(y_predicted_rounded) * 100)
        # match_dic2['%s' %list_data] = '%.2f %%' % (
        #             match_count1 / len(y_predicted_rounded) * 100)
        # match_dic3['%s' % list_data] = '%.2f %%' % (
        #             match_count2 / len(y_predicted_rounded) * 100)



# 최대값 찾기
print(match_dic)
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
match_dic2 = sorted(match_dic2.items(), key=operator.itemgetter(1),reverse=True)
match_dic3 = sorted(match_dic3.items(), key=operator.itemgetter(1),reverse=True)
# print(match_dic)+
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합:",match_dic[0])
# print(match_dic2)
print('총 조합 갯수: %d'%len(match_dic2))
print("MAX 조합:",match_dic2[0])
# print(match_dic3)
print('총 조합 갯수: %d'%len(match_dic3))
print("MAX 조합:",match_dic3[0])