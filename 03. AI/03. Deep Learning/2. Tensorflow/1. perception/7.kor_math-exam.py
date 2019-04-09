import tensorflow as tf

X1=tf.placeholder(tf.float32,shape=[None])
X2=tf.placeholder(tf.float32,shape=[None])
Y=tf.placeholder(tf.float32,shape=[None])


W1=tf.Variable(tf.random_normal([1]),name='weight1')
W2=tf.Variable(tf.random_normal([1]),name='weight2')
b=tf.Variable(tf.random_normal([1]),name='bias')

hypothesis=X1*W1+X2*W2+b

cost=tf.reduce_mean(tf.square(hypothesis-Y))

optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01)
train=optimizer.minimize(cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(5001):
    cost_val,W_val1,W_val2,b_val,_=sess.run([cost,W1,W2,b,train],feed_dict={X1:[5,7],X2:[5,7],Y:[101,141]})
    if step%500==0:
        print(step,cost_val,W_val1,W_val2,b_val)
print("예측Y:",sess.run(hypothesis,feed_dict={X1:[8],X2:[8]}))