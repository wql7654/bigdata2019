import tensorflow as tf
import numpy as np # linear algebra
from sklearn.model_selection import train_test_split
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

bmi = pd.read_csv("bmi.csv")


# 수집 데이터 형식 기술
# 데이터 요약: 손글씨 그림 이미지
# 고정 변수: 그림의 픽셀 정보
# 종속 변수: 0~9까지 숫자 판별


# 변수들을 설정한다.
X = tf.placeholder(tf.float32, [None, None]) # mnist 이미지데이터 형태는 28 * 28 = 784
Y = tf.placeholder(tf.float32, [None, None])  # 0-9 숫자분류 = > 10 classes

#Logistic Classifier (Linear Classifier)
W = tf.Variable(tf.zeros([2, 3]))
b = tf.Variable(tf.zeros([3]))
#matmul: 행렬 내적(곱)
logit_y = tf.matmul(X, W) + b
wig = bmi["weight"] # 최대 100kg라고 가정
hei = bmi["height"] # 최대 200cm라고 가정
X_data = pd.concat([wig,hei],axis=1)
# X_data=bmi[['height','weight']]
bmi["label"] = bmi["label"].map({"fat":0,"normal":1,"thin":2})
# bmi['label01'] = np.where(bmi['label']=='True.',1.,0.)
Y_data=bmi['label']


X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, test_size=0.3, random_state=1)


softmax_y = tf.nn.softmax(logit_y)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(softmax_y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(len(X_train)):
  # batch_xs, batch_ys = mnist.train.next_batch(100) #배치크기는 100
  sess.run(train_step, feed_dict={X: X_train[i: i + 1], Y: y_train[i: i + 1]})

# 결과 예측
correct_prediction = tf.equal(tf.argmax(softmax_y,1), tf.argmax(Y,1))

# 결과 검증
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("정확도 : ", sess.run(accuracy, feed_dict={X: X_test, Y: y_test}))

'''
#실행결과
Extracting MNIST_data/train-images-idx3-ubyte.gz
Extracting MNIST_data/train-labels-idx1-ubyte.gz
Extracting MNIST_data/t10k-images-idx3-ubyte.gz
Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
정확도 :  0.9092
'''