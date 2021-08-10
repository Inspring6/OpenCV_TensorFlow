import tensorflow as tf

execution = tf.compat.v1.disable_eager_execution()
q = tf.compat.v1.FIFOQueue(1000, "float32")
counter = tf.Variable(0.0)
add_op = tf.compat.v1.assign_add(counter, tf.constant(1.0))
enqueueData_op = q.enqueue(counter)

sess = tf.compat.v1.Session()
qr = tf.compat.v1.train.QueueRunner(q, enqueue_ops=[add_op, enqueueData_op] * 2)
sess.run(tf.compat.v1.global_variables_initializer())

coord = tf.compat.v1.train.Coordinator()
enqueue_threads = qr.create_threads(sess, coord=coord, start=True)

for i in range(0, 10):
    print(sess.run(q.dequeue()))

coord.request_stop()
coord.join(enqueue_threads)
