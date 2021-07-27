import tensorflow as tf

tf.compat.v1.disable_eager_execution()
sess = tf.compat.v1.Session()
hello = tf.constant("hello,tensorflow", dtype=tf.string)
print(sess.run(hello))
