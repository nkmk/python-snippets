from sklearn.metrics import confusion_matrix

y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]

cm = confusion_matrix(y_true, y_pred)

print(cm)
# [[1 4]
#  [3 2]]

print(type(cm))
# <class 'numpy.ndarray'>

print(cm.flatten())
# [1 4 3 2]

tn, fp, fn, tp = cm.flatten()

print(tn)
# 1

print(fp)
# 4

print(fn)
# 3

print(tp)
# 2

y_true_ab = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']
y_pred_ab = ['A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B']

print(confusion_matrix(y_true_ab, y_pred_ab))
# [[1 4]
#  [3 2]]

print(confusion_matrix(y_true_ab, y_pred_ab, labels=['B', 'A']))
# [[2 3]
#  [4 1]]

y_true_multi = [0, 0, 0, 1, 1, 1, 2, 2, 2]
y_pred_multi = [0, 1, 1, 1, 1, 2, 2, 2, 2]

print(confusion_matrix(y_true_multi, y_pred_multi))
# [[1 2 0]
#  [0 2 1]
#  [0 0 3]]

print(confusion_matrix(y_true_multi, y_pred_multi, labels=[2, 1]))
# [[3 0]
#  [1 2]]
