import pandas as pd
from sklearn import svm,metrics
from itertools import combinations
import operator


colums_list2 = ['alcohol','chlorides','citric_acid','density','fixed_acidity','free_sulfur_dioxide','pH',
               'residual_sugar','sulphates','total_sulfur_dioxide','volatile_acidity']

colums_list=[1,2,3,4,5,6,7,8,9,10,11,12]
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

match_dic={}
# print(wine)

for num in range(1,len(colums_list2)):
    combi_list = list(combinations(colums_list2,num))
    for tup in combi_list:

        wine_df = pd.DataFrame(wine)
        xor_dat=wine[list(tup)]
        xor_label=wine_df.iloc[:,12]



        clf = svm.SVC(gamma='auto')
        clf.fit(xor_dat,xor_label)
        pre=clf.predict(xor_dat)
        ac_score=metrics.accuracy_score(xor_label,pre)
        print("정답률=",ac_score)
        match_dic[tup]=ac_score

match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
print(match_dic)
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합:",match_dic[0])

