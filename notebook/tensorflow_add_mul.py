import tensorflow as tf

const1 = tf.constant(5)
const2 = tf.constant(10)

add_op = tf.add(const1, const2)
mul_op = tf.multiply(add_op, const2)

print(add_op)
print(mul_op)
# Tensor("Add:0", shape=(), dtype=int32)
# Tensor("Mul:0", shape=(), dtype=int32)

with tf.Session() as sess:
    add_result, mul_result = sess.run([add_op, mul_op])
    print(add_result)
    print(mul_result)
# 15
# 150

add_op_2 = const1 + const2
mul_op_2 = add_op_2 * const2

with tf.Session() as sess:
    add_op_2_result, mul_op_2_result = sess.run([add_op_2, mul_op_2])
    print(add_op_2_result)
    print(mul_op_2_result)
# 15
# 150
