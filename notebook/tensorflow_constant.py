import tensorflow as tf

const1 = tf.constant(5)
const2 = tf.constant(10)

print(const1)
print(const2)
# Tensor("Const:0", shape=(), dtype=int32)
# Tensor("Const_1:0", shape=(), dtype=int32)

with tf.Session() as sess:
    const1_result, const2_result = sess.run([const1, const2])
    print(const1_result)
    print(const2_result)
# 5
# 10
