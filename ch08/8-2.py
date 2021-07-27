import tensorflow as tf

tf.compat.v1.disable_eager_execution()

input1 = tf.compat.v1.placeholder(tf.int32)
input2 = tf.compat.v1.placeholder(tf.int32)

output = tf.add(input1, input2)

sess = tf.compat.v1.Session()
print(sess.run(output, feed_dict={input1: [1], input2: [2]}))
