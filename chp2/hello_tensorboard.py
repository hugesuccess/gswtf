import tensorflow as tf

a = tf.placeholder("int32")
b = tf.placeholder("int32")
y = tf.mul(a, b)

sess = tf.Session()
op = sess.run(y, feed_dict={a:2 b: 5})

print(op)
