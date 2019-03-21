from sklearn import model_selection, svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd
# CSV 파일을 읽어 들이고 가공하기

data=pd.read_csv('./mnist/all_data.csv',header=None)


csv_label=data.loc[:,0]
cnt=0
for b in data:
    cnt+=1

for i in range(1,cnt):
    data[i]=data[i]/256



csv_data=data.loc[:,1:]

for i in csv_data:
    print(csv_data[i])

# print(csv_label)
# print(csv_data)
# clf = svm.SVC(gamma='auto')
# train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label,shuffle=None)
# clf.fit(train_data, train_label)
# predict = clf.predict(test_data)
# ac_score = metrics.accuracy_score(test_label, predict)
# cl_report = metrics.classification_report(test_label, predict)
# print("정답률: ", ac_score*100, '%')
# print('리포트: ', cl_report)
