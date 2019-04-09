import tensorflow as tf

x_train=[1,2,3,4]
y_train=[6,5,7,10]


W=tf.Variable(tf.random_normal([1]),name='weight')
b=tf.Variable(tf.random_normal([1]),name='bias')

hypothesis=x_train*W+b

cost=tf.reduce_mean(tf.square(hypothesis-y_train))

optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01)
train=optimizer.minimize(cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2000):
    sess.run(train)
    print(step,sess.run(cost),sess.run(W),sess.run(b))