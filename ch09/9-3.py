import tensorflow as tf
import numpy as np

tf.compat.v1.disable_eager_execution()

xs = np.random.randint(46, 99, 100)  # (low, high=None, size=None, dtype='l')
ys = 1.7 * xs

x = tf.compat.v1.placeholder(tf.float32)
y = tf.compat.v1.placeholder(tf.float32)

w = tf.Variable(0.1)
b = tf.Variable(0.1)

y_ = tf.multiply(w, x) + b
cost = tf.reduce_sum(tf.pow((y - y_), 2))
train_step = tf.compat.v1.train.GradientDescentOptimizer(0.02).minimize(cost)

init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)
for _ in range(100):
    sess.run(train_step, feed_dict={x: xs, y: ys})
print(w.eval(sess))
print(b.eval(sess))
