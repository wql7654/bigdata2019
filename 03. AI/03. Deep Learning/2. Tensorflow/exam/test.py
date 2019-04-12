import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

#키, 몸무게, 레이블이 적힌 csv 파일 읽어들이기
#pandas를 사용하므로 간단하게 CSV 파일을 읽는것이 가능
csv = pd.read_csv("bmi.csv")

#데이터 정규화
#데이터를 0이상, 1미만으로 지정하는데 키의 최대값은 200cm, 몸무게의 최대값은 80kg로 정규화
csv["height"] = csv["height"]/200.0
csv["weight"] = csv["weight"]/100.0

#레이블을 배열로 변환하기
#저체중, 정상 비만의 레이블을 [1,0,0],[0,1,0],[0,0,1] 형태로 변환합니다.
bclass = {"thin":[1.0,0,0],"normal":[0,1.0,0],"fat":[0,0,1.0]}
csv["label"] = csv["label"].map(bclass)

#테스트를 위한 데이터 분류(트레이닝 데이터 추출)
X_data = csv[["weight","height"]]
Y_data = csv["label"]
X_train, test_pat, y_train, test_ans = train_test_split(X_data, Y_data, test_size=0.3, random_state=1)

#플레이스홀더 선언하기
x  = tf.placeholder(tf.float32, [None,2]) # 키와 몸무게 데이터 넣기
y_ = tf.placeholder(tf.float32, [None,3]) # 레이블 넣기

#변수 선언하기
W = tf.Variable(tf.zeros([2,3])) # 가중치
b = tf.Variable(tf.zeros([3])) #바이어스
#소프트맥스 회귀 정의하기
y = tf.nn.softmax(tf.matmul(x,W)+b)

#모델 훈련하기
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),reduction_indices=[1]))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(cross_entropy)

#정답률 구하기(결과예측)
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#세션 시작하기
sess = tf.Session()
sess.run(tf.global_variables_initializer()) # 변수 초기화 하기


#학습시키기
#100개씩 3000번 학습시킵니다.
for step in range(3001):
    i = (step*100) % 14000
    rows = X_train[1+i:1+i+100]
    rows2 = y_train[1+i:1+i+100]
    rows3 = test_pat[1+i:1+i+100]
    rows4 = test_ans[1+i:1+i+100]
    x_pat = rows[["weight","height"]]
    x_pat=x_pat.values.tolist()
    y_ans=rows2.values.tolist()

    x_test2 = rows3[["weight","height"]]
    x_test=x_test2.values.tolist()
    y_test=rows4.values.tolist()
    c=[]

    fd = {x:x_pat,y_:y_ans}
    sess.run(train, feed_dict=fd)
    #정답률확인(결과 검증)
    if step ==3000 :
        cre = sess.run(cross_entropy,feed_dict=fd)
        acc = sess.run(accuracy,feed_dict={x:x_test, y_:y_test})
        print("step", step, "cross_entropy=",cre, "평균=", acc*100,'%')

