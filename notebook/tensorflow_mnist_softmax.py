import tensorflow as tf
import numpy as np
from sklearn import datasets, model_selection, utils

mnist = datasets.fetch_mldata('MNIST original', data_home='data/src/download')

X = mnist.data / 255
y = mnist.target
Y = np.identity(10)[y.astype(int)]

train_size = 60000
test_size = 10000

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X, Y, test_size=test_size, train_size=train_size)

n_in = 784
n_out = 10

x = tf.placeholder(tf.float32, [None, n_in])
y_ = tf.placeholder(tf.float32, [None, n_out])

W = tf.Variable(tf.zeros([n_in, n_out]))
b = tf.Variable(tf.zeros([n_out]))
y = tf.matmul(x, W) + b

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

batch_size = 100
batch_num = (int)(train_size // batch_size)

epochs = 20

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(epochs):
        X_, Y_ = utils.shuffle(X_train, Y_train)

        for i in range(batch_num):
            batch_X = X_train[i * batch_size: (i+1) * batch_size]
            batch_Y = Y_train[i * batch_size: (i+1) * batch_size]
            sess.run(train_step, feed_dict={x: batch_X, y_: batch_Y})
        
        loss, acc = sess.run([cross_entropy, accuracy], feed_dict={x: X_test, y_: Y_test})
        print('epoch: {:2}, loss: {:.5f}, accuracy: {:.5f}'.format(epoch, loss, acc))

    acc = sess.run(accuracy, feed_dict={x: X_test, y_: Y_test})
    print('Final accuracy: {:.5f}'.format(acc))
# epoch:  0, loss: 0.31313, accuracy: 0.91310
# epoch:  1, loss: 0.29504, accuracy: 0.91840
# epoch:  2, loss: 0.28769, accuracy: 0.92080
# epoch:  3, loss: 0.28376, accuracy: 0.92210
# epoch:  4, loss: 0.28138, accuracy: 0.92240
# epoch:  5, loss: 0.27983, accuracy: 0.92290
# epoch:  6, loss: 0.27879, accuracy: 0.92340
# epoch:  7, loss: 0.27808, accuracy: 0.92510
# epoch:  8, loss: 0.27758, accuracy: 0.92560
# epoch:  9, loss: 0.27724, accuracy: 0.92610
# epoch: 10, loss: 0.27701, accuracy: 0.92650
# epoch: 11, loss: 0.27687, accuracy: 0.92710
# epoch: 12, loss: 0.27679, accuracy: 0.92700
# epoch: 13, loss: 0.27677, accuracy: 0.92730
# epoch: 14, loss: 0.27678, accuracy: 0.92710
# epoch: 15, loss: 0.27683, accuracy: 0.92690
# epoch: 16, loss: 0.27690, accuracy: 0.92720
# epoch: 17, loss: 0.27699, accuracy: 0.92710
# epoch: 18, loss: 0.27710, accuracy: 0.92720
# epoch: 19, loss: 0.27723, accuracy: 0.92710
# Final accuracy: 0.92710
