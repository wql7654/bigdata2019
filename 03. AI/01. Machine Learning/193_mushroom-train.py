import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from datetime import datetime
import time
# 데이터 읽어들이기
mr = pd.read_csv('mushroom.csv', header = None)
start = datetime.fromtimestamp(time.time())
# 데이터 내부의 기호를 숫자로 변환하기
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    label.append(row.loc[0])
    row_data = []
    for v in row.loc[1:]:
        row_data.append(ord(v))
    data.append(row_data)
# 학습 전용과 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test = train_test_split(data, label)
# 데이터 학습시기키
clf = svm.SVC(gamma='auto')
# clf = RandomForestClassifier(n_estimators=10)
clf.fit(data_train, label_train)
# 데이터 예측하기
predict = clf.predict(data_test)
# 결과 테스트하기
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
end = datetime.fromtimestamp(time.time())
print("정답률: ", ac_score)
print('리포트: \n', cl_report)
print(start)
print(end)
print(end-start)