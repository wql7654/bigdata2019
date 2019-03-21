import pandas as pd
from sklearn import svm,metrics
from itertools import combinations
import operator
import numpy as np


house = pd.read_csv('Housing.csv', sep=',',header=0)
house.columns = house.columns.str.replace(' ','_')


house['driveway1'] = np.where(house['driveway'] == 'yes', 1., 0.)
house['recroom1'] = np.where(house['recroom'] == 'yes', 1., 0.)
house['fullbase1'] = np.where(house['fullbase'] == 'yes', 1., 0.)
house['gashw1'] = np.where(house['gashw'] == 'yes', 1., 0.)
house['airco1'] = np.where(house['airco'] == 'yes', 1., 0.)
house['prefarea1'] = np.where(house['prefarea'] == 'yes', 1., 0.)

formula=['lotsize','bedrooms','bathrms','stories','driveway1','recroom1','fullbase1','gashw1','airco1','garagepl','prefarea1']

match_dic0={}
match_dic1={}
match_dic={}
match_dic2={}
match_dic3={}
# print(wine)
err_cnt0=0.0
err_cnt=0.05
err_cnt2=0.1
err_cnt3=0.2
for num in range(1,len(formula)):
    combi_list = list(combinations(formula,num))
    for tup in combi_list:

        wine_df = pd.DataFrame(house)
        xor_dat=house[list(tup)]

        xor_label=wine_df.iloc[:,1]
        clf = svm.SVC(gamma='auto')
        clf.fit(xor_dat,xor_label)
        pre=clf.predict(xor_dat)
        ac_score=metrics.accuracy_score(xor_label,pre)

        match_count0 = 0
        match_count=0
        match_count1 = 0
        match_count2 = 0
        for index in range(len(pre)):
            if pre[index]==xor_label[index]:
                match_count0+=1
            if pre[index] < (xor_label[index]*err_cnt)+xor_label[index] \
                and pre[index] > xor_label[index]-(xor_label[index]*err_cnt):
                match_count+=1
            if pre[index] < (xor_label[index]*err_cnt2)+xor_label[index] \
                and pre[index] > xor_label[index]-(xor_label[index]*err_cnt2):
                match_count1+=1
            if pre[index] < (xor_label[index]*err_cnt3)+xor_label[index] \
                and pre[index] >xor_label[index]-(xor_label[index]*err_cnt3):
                match_count2+=1

        print('\n>> ',tup)
        print('>> 정답률: %.2f %%'%(ac_score*100))
        print('>> match count=',match_count0)

        print('>> 정답률: %.2f %%'%(match_count0/len(pre)*100))
        print('>> match count=',match_count)
        print('>> 정답률: %.2f %%'%(match_count/len(pre)*100))
        print('>> match count=', match_count1)
        print('>> 정답률: %.2f %%' % (match_count1 / len(pre) * 100))
        print('>> match count=', match_count2)
        print('>> 정답률: %.2f %%' % (match_count2 / len(pre) * 100))

        match_dic1[tup]=(ac_score*100)
        match_dic0[tup] = match_count0 / len(pre) * 100
        match_dic[tup] = match_count / len(pre) * 100
        match_dic2[tup] = match_count1 / len(pre) * 100
        match_dic3[tup] = match_count2 / len(pre) * 100
        # match_dic['%s' % list_data] = '.2f %%%' % (
        #             match_count / len(y_predicted_rounded) * 100)
        # match_dic2['%s' %list_data] = '%.2f %%' % (
        #             match_count1 / len(y_predicted_rounded) * 100)
        # match_dic3['%s' % list_data] = '%.2f %%' % (
        #             match_count2 / len(y_predicted_rounded) * 100)



# 최대값 찾기
match_dic0 = sorted(match_dic0.items(), key=operator.itemgetter(1),reverse=True)
match_dic1 = sorted(match_dic1.items(), key=operator.itemgetter(1),reverse=True)
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
match_dic2 = sorted(match_dic2.items(), key=operator.itemgetter(1),reverse=True)
match_dic3 = sorted(match_dic3.items(), key=operator.itemgetter(1),reverse=True)
# print(match_dic)+
print('총 조합 갯수: %d'%len(match_dic1))
print("metrics MAX 조합:",match_dic1[0])
print("0% MAX 조합:",match_dic0[0])
print("5%MAX 조합:",match_dic[0])
print("10%MAX 조합:",match_dic2[0])
print("20%MAX 조합:",match_dic3[0])
