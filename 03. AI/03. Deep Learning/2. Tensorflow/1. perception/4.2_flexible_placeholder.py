import tensorflow as tf

a=tf.placeholder(tf.int32,[None])
b=tf.constant(30)

X2_op=a*b

sess=tf.Session()

r1=sess.run(X2_op,feed_dict={a:[1,2,3,4,5]})
print(r1)
r2=sess.run(X2_op,feed_dict={a:[10,20,30]})
print(r2)

sess.close()