# import libraries
import pandas as pd
import numpy as np
import math
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
# from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import classification_report
from sklearn import svm
import csv
#import Data from file CSV
filename = "train.csv"
filename2 = "test.csv"
filename3 = "gender_submission.csv"
data = pd.read_csv(filename)
data2 = pd.read_csv(filename2)
data3 = pd.read_csv(filename3)

# convert Char data into numeric values by using for loop
def Sex_array(x,y):
    for i in range(y):
        if x[i] == "male":
            x[i] = 1
        else :
            x[i] = 0
    return x

def Embarked_array(x,y):
    for i in range(y):
        if x[i] == "S":
            x[i] = 1
        elif x[i] == "C":
            x[i] = 2
        else :
            x[i] = 3
    return x

#define features of the train data
X1 = data.Pclass
X2 = np.array(data.Sex)
X2 = Sex_array(X2,len(X2))
X3 = data.Age
X4 = data.SibSp
X5 = data.Parch
X6 = data.Fare
X7 = np.array(data.Embarked)
X7 = Embarked_array(X7,len(X7))
data1 = [X1,X2,X3,X4,X5,X6,X7]
X = np.array(data1)
X = np.transpose(X)
Y = data.Survived
X8 = data.PassengerId

#define features of the test data
X_1 = data2.Pclass
X_2 = np.array(data2.Sex)
X_2 = Sex_array(X_2,len(X_2))
X_3 = data2.Age
X_4 = data2.SibSp
X_5 = data2.Parch
X_6 = data2.Fare
X_7 = np.array(data2.Embarked)
X_7 = Embarked_array(X_7,len(X_7))
data4 = [X_1,X_2,X_3,X_4,X_5,X_6,X_7]
x = np.array(data4)
X_validation = np.transpose(x)
Y_validation = data3.Survived
X_8 = data2.PassengerId

#applying linear SVM and find out the accuracy
clf = svm.SVC(kernel = 'linear')
clf.fit(X,Y)
predicted = clf.predict(X_validation)
report = classification_report(Y_validation, predicted)
accuracy = clf.score(X_validation,Y_validation)
print(accuracy*100)
print(report)
preds = clf.predict(X_validation)
Y_validation = np.array(Y_validation)

df = pd.DataFrame({"Survived":preds,"PassengerId":X_8})
df.to_csv('nikhil2.csv',index = False)
print(df)