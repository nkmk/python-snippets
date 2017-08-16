import tensorflow as tf

var = tf.Variable(10)
const = tf.constant(5)
calc_op = var * const
assign_op = tf.assign(var, calc_op)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    print(sess.run(var))
    
    sess.run(assign_op)
    print(sess.run(var))
    
    sess.run(assign_op)
    print(sess.run(var))
# 10
# 50
# 250

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    print(sess.run(var))
# 10
