import tensorflow as tf

a=tf.placeholder(tf.int32,[3])
b=tf.constant(3)

X2_op=a*b

sess=tf.Session()

r1=sess.run(X2_op,feed_dict={a:[12,2,3]})
print(r1)
r2=sess.run(X2_op,feed_dict={a:[10,20,30]})
print(r2)

sess.close()