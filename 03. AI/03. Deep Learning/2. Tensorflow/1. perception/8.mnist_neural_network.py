import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)

X=tf.placeholder(tf.float32,shape=[None,784])
Y=tf.placeholder(tf.float32,shape=[None,10])

W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.random_normal([10]))

logit_y=tf.matmul(X,W)+b
softmax_y=tf.nn.softmax(logit_y)
cross_entoropy=tf.reduce_mean(-tf.reduce_sum(Y*tf.log(softmax_y),reduction_indices=[1]))
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(cross_entoropy)

init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)
for i in range(500):
    batch_xs,batch_ys=mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={X:batch_xs,Y:batch_ys})
correct_prediction=tf.equal(tf.argmax(softmax_y,1), tf.argmax(Y,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print("정확도:",sess.run(accuracy,feed_dict={X:mnist.test.images,Y:mnist.test.labels}))
