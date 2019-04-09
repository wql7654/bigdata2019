import tensorflow as tf
import matplotlib.pyplot as plt

x=[1,2,3]
y=[1,2,3]

w=tf.placeholder(tf.float32)

hypothesis=x*w
cost=tf.reduce_mean(tf.square(hypothesis-y))

with tf.Session() as sess:
    W_val=[]
    cost_val=[]

    for i in range(-30,50):
        feed_W=i*0.1

        curr_cost,curr_W=sess.run([cost,w],feed_dict={w:feed_W})
        if curr_cost == 0:
            print(i)
        W_val.append(curr_W)
        cost_val.append(curr_cost)
    plt.plot(W_val,cost_val)
    plt.show()