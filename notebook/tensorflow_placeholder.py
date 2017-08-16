import tensorflow as tf

const = tf.constant(1)
holder = tf.placeholder(tf.int32)
add_op = const + holder

with tf.Session() as sess:
    result = sess.run(add_op, feed_dict={holder: 5})
    print(result)
    
    result = sess.run(add_op, feed_dict={holder: 10})
    print(result)
# 6
# 11

holder1 = tf.placeholder(tf.int32)
holder2 = tf.placeholder(tf.int32, [3])
mul_op = holder1 * holder2

with tf.Session() as sess:
    result = sess.run(mul_op, feed_dict={holder1: 2, holder2: [0, 1, 2]})
    print(result)
    
    result = sess.run(mul_op, feed_dict={holder1: 5, holder2: [0, 10, 20]})
    print(result)
# [0 2 4]
# [  0  50 100]

holder1 = tf.placeholder(tf.int32)
holder2 = tf.placeholder(tf.int32, [None])
mul_op = holder1 * holder2

with tf.Session() as sess:
    result = sess.run(mul_op, feed_dict={holder1: 2, holder2: [0, 1]})
    print(result)
    
    result = sess.run(mul_op, feed_dict={holder1: 5, holder2: [0, 1, 2, 3, 4]})
    print(result)
# [0 2]
# [ 0  5 10 15 20]
