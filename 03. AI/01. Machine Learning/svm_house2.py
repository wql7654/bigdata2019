import pandas as pd
from sklearn import svm,metrics
from itertools import combinations
import operator
import numpy as np
from sklearn.model_selection import train_test_split


house = pd.read_csv('Housing.csv', sep=',',header=0)
house.columns = house.columns.str.replace(' ','_')


house['driveway1'] = np.where(house['driveway'] == 'yes', 1., 0.)
house['recroom1'] = np.where(house['recroom'] == 'yes', 1., 0.)
house['fullbase1'] = np.where(house['fullbase'] == 'yes', 1., 0.)
house['gashw1'] = np.where(house['gashw'] == 'yes', 1., 0.)
house['airco1'] = np.where(house['airco'] == 'yes', 1., 0.)
house['prefarea1'] = np.where(house['prefarea'] == 'yes', 1., 0.)

formula=['lotsize','bedrooms','bathrms','stories','driveway1','recroom1','fullbase1','gashw1','airco1','garagepl','prefarea1']
formula2=['lotsize','bedrooms','stories','garagepl']
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

for i in range(0,1000):
    wine_df = pd.DataFrame(house)
    xor_dat=house[formula2]
    xor_label=wine_df.iloc[:,1]
    train_data, test_data, train_label, test_label = train_test_split(xor_dat, xor_label, shuffle=True,test_size=0.25)
        # 데이터 학습시키고 예측하기
    clf = svm.SVC(gamma='auto')
    clf.fit(train_data, train_label)
    pre = clf.predict(test_data)
    # 정답률 구하기
    ac_score = metrics.accuracy_score(test_label, pre)

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


    print('전체 데이터 수: %d' %len(house))
    print('학습 전용 데이터 수: %d' %len(train_data))
    print('테스트 데이터 수: %d' %(len(test_data)))

    print('>> 정답률: %.2f %%'%(ac_score*100))
    print('>> match count=',match_count0)

    print('>> 정답률: %.2f %%'%(match_count0/len(pre)*100))
    print('>> match count=',match_count)
    print('>> 정답률: %.2f %%'%(match_count/len(pre)*100))
    print('>> match count=', match_count1)
    print('>> 정답률: %.2f %%' % (match_count1 / len(pre) * 100))
    print('>> match count=', match_count2)
    print('>> 정답률: %.2f %%' % (match_count2 / len(pre) * 100))

    match_dic1[i] = (ac_score * 100)
    match_dic0[i] = match_count0 / len(pre) * 100
    match_dic[i] = match_count / len(pre) * 100
    match_dic2[i] = match_count1 / len(pre) * 100
    match_dic3[i] = match_count2 / len(pre) * 100
    # match_dic['%s' % list_data] = '.2f %%%' % (
    #             match_count / len(y_predicted_rounded) * 100)
    # match_dic2['%s' %list_data] = '%.2f %%' % (
    #             match_count1 / len(y_predicted_rounded) * 100)
    # match_dic3['%s' % list_data] = '%.2f %%' % (
    #             match_count2 / len(y_predicted_rounded) * 100)

# 최대값 찾기
match_dic0 = sorted(match_dic0.items(), key=operator.itemgetter(1), reverse=True)
match_dic1 = sorted(match_dic1.items(), key=operator.itemgetter(1), reverse=True)
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)
match_dic2 = sorted(match_dic2.items(), key=operator.itemgetter(1), reverse=True)
match_dic3 = sorted(match_dic3.items(), key=operator.itemgetter(1), reverse=True)
# print(match_dic)+
print('총 조합 갯수: %d' % len(match_dic1))
a=0
b=0
c=0
d=0
e=0
for ics in range(len(match_dic)):
    a +=float(match_dic1[ics][1])
    b += float(match_dic0[ics][1])
    c += float(match_dic1[ics][1])
    d += float(match_dic2[ics][1])
    e += float(match_dic3[ics][1])

print("metrics MAX 조합:", match_dic1[0],match_dic1[len(match_dic1)-1])
print(a/len(match_dic1))
print("0% MAX 조합:", match_dic0[0],match_dic0[len(match_dic0)-1])
print(b/len(match_dic0))
print("5%MAX 조합:", match_dic[0],match_dic[len(match_dic)-1])
print(c/len(match_dic))
print("10%MAX 조합:", match_dic2[0],match_dic2[len(match_dic2)-1])
print(d/len(match_dic2))
print("20%MAX 조합:", match_dic3[0], match_dic3[len(match_dic3)-1])
print(e/len(match_dic3))

