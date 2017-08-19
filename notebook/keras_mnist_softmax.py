import numpy as np
from sklearn import datasets, model_selection
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
# Using TensorFlow backend.

mnist = datasets.fetch_mldata('MNIST original', data_home='data/src/download')

X = mnist.data / 255
y = mnist.target
Y = np.identity(10)[y.astype(int)]

train_size = 60000
test_size = 10000

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X, Y, test_size=test_size, train_size=train_size)

model = Sequential()
model.add(Dense(units=10, input_dim=784, activation='softmax'))
sgd = optimizers.SGD(lr=0.5)
model.compile(
    optimizer=sgd,
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

batch_size = 100
batch_num = (int)(train_size // batch_size)

epochs = 20

model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size)
# Epoch 1/20
# 60000/60000 [==============================] - 1s - loss: 0.3934 - acc: 0.8884     
# Epoch 2/20
# 60000/60000 [==============================] - 1s - loss: 0.3018 - acc: 0.9145     
# Epoch 3/20
# 60000/60000 [==============================] - 1s - loss: 0.2870 - acc: 0.9192     
# Epoch 4/20
# 60000/60000 [==============================] - 1s - loss: 0.2793 - acc: 0.9212     
# Epoch 5/20
# 60000/60000 [==============================] - 1s - loss: 0.2739 - acc: 0.9235     
# Epoch 6/20
# 60000/60000 [==============================] - 1s - loss: 0.2699 - acc: 0.9242     
# Epoch 7/20
# 60000/60000 [==============================] - 1s - loss: 0.2666 - acc: 0.9252     
# Epoch 8/20
# 60000/60000 [==============================] - 1s - loss: 0.2645 - acc: 0.9251     
# Epoch 9/20
# 60000/60000 [==============================] - 1s - loss: 0.2621 - acc: 0.9269     
# Epoch 10/20
# 60000/60000 [==============================] - 1s - loss: 0.2601 - acc: 0.9280     
# Epoch 11/20
# 60000/60000 [==============================] - 1s - loss: 0.2588 - acc: 0.9274     
# Epoch 12/20
# 60000/60000 [==============================] - 1s - loss: 0.2586 - acc: 0.9277     
# Epoch 13/20
# 60000/60000 [==============================] - 1s - loss: 0.2558 - acc: 0.9285     
# Epoch 14/20
# 60000/60000 [==============================] - 1s - loss: 0.2547 - acc: 0.9287     
# Epoch 15/20
# 60000/60000 [==============================] - 1s - loss: 0.2537 - acc: 0.9297     
# Epoch 16/20
# 60000/60000 [==============================] - 1s - loss: 0.2526 - acc: 0.9288     
# Epoch 17/20
# 60000/60000 [==============================] - 1s - loss: 0.2524 - acc: 0.9287     
# Epoch 18/20
# 60000/60000 [==============================] - 1s - loss: 0.2515 - acc: 0.9298     
# Epoch 19/20
# 60000/60000 [==============================] - 1s - loss: 0.2499 - acc: 0.9303     
# Epoch 20/20
# 60000/60000 [==============================] - 1s - loss: 0.2499 - acc: 0.9302     
# <keras.callbacks.History at 0x10d404d30>

score = model.evaluate(X_test, Y_test)
print(score)
# 10000/10000 [==============================] - 0s     
# [0.30260467473864555, 0.91790000000000005]
