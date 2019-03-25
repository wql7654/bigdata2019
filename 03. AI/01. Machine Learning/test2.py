from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

read = pd.read_csv("data.csv")
read["weight"] = read["weight"]/80
read["height"] = read["height"]/200
xor_dat=read[['height','weight']]
xor_label=read['label']
clf = svm.SVC(gamma='auto')
train_data, test_data, train_label, test_label =train_test_split(xor_dat,xor_label)
clf.fit(train_data, train_label)
predict = clf.predict(test_data)
ac_score = metrics.accuracy_score(test_label, predict)
cl_report = metrics.classification_report(test_label, predict)
print(ac_score)
print(cl_report)