import tensorflow as tf
import numpy as np
from sklearn import datasets, model_selection, utils

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

width = 28
height = 28

n_in = width * height
n_out = 10

x = tf.placeholder(tf.float32, [None, n_in])
y_ = tf.placeholder(tf.float32, [None, n_out])

with tf.name_scope('reshape'):
    x_image = tf.reshape(x, [-1, height, width, 1])

with tf.name_scope('conv1'):
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

with tf.name_scope('pool1'):
    h_pool1 = max_pool_2x2(h_conv1)

with tf.name_scope('conv2'):
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

with tf.name_scope('pool2'):
    h_pool2 = max_pool_2x2(h_conv2)

with tf.name_scope('fc1'):
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

with tf.name_scope('dropout'):
    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

with tf.name_scope('fc2'):
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])
    y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

with tf.name_scope('loss'):
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y_,
                                                            logits=y_conv)
cross_entropy = tf.reduce_mean(cross_entropy)

with tf.name_scope('training'):
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

with tf.name_scope('accuracy'):
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    correct_prediction = tf.cast(correct_prediction, tf.float32)
accuracy = tf.reduce_mean(correct_prediction)

mnist = datasets.fetch_mldata('MNIST original', data_home='data/src/download')

X = mnist.data / 255
y = mnist.target
Y = np.identity(10)[y.astype(int)]

train_size = 60000
test_size = 10000

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X, Y, test_size=test_size, train_size=train_size)

batch_size = 100
batch_num = (int)(train_size // batch_size)

epochs = 10

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(epochs):
        X_, Y_ = utils.shuffle(X_train, Y_train)

        for i in range(batch_num):
            batch_X = X_train[i * batch_size: (i+1) * batch_size]
            batch_Y = Y_train[i * batch_size: (i+1) * batch_size]
            sess.run(train_step, feed_dict={x: batch_X, y_: batch_Y, keep_prob: 0.5})
            # if i % 10 == 0:
            #     loss = sess.run(cross_entropy, feed_dict={x: X_test, y_: Y_test, keep_prob: 1})
            #     acc = sess.run(accuracy, feed_dict={x: X_test, y_: Y_test, keep_prob: 1})
            #     print('step: {}, loss: {:.5f}, train_accuracy: {:.5f}'.format(i, loss, acc))
        loss = sess.run(cross_entropy, feed_dict={x: X_test, y_: Y_test, keep_prob: 1})
        acc = sess.run(accuracy, feed_dict={x: X_test, y_: Y_test, keep_prob: 1})
        print('epoch: {}, loss: {:.5f}, train_accuracy: {:.5f}'.format(epoch, loss, acc))

    acc = sess.run(accuracy, feed_dict={x: X_test, y_: Y_test, keep_prob: 1})
    print('test_accuracy: {:.5f}'.format(acc))
