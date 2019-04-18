from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]

print(precision_score(y_true, y_pred))
# 0.3333333333333333

print(precision_score(y_true, y_pred, pos_label=0))
# 0.25

print(precision_score(y_true, y_pred, average=None))
# [0.25       0.33333333]

print(precision_score(y_true, y_pred, average='macro'))
# 0.29166666666666663

print(precision_score(y_true, y_pred, average='micro'))
# 0.3

print(confusion_matrix(y_true, y_pred))
# [[1 4]
#  [3 2]]

print(confusion_matrix(y_true, y_pred, labels=[1, 0]))
# [[2 3]
#  [4 1]]

print(precision_score(y_true, y_pred, average='weighted'))
# 0.29166666666666663

y_true_2 = [0, 1, 1, 1, 1]
y_pred_2 = [0, 0, 0, 0, 1]

print(confusion_matrix(y_true_2, y_pred_2))
# [[1 0]
#  [3 1]]

print(confusion_matrix(y_true_2, y_pred_2, labels=[1, 0]))
# [[1 3]
#  [0 1]]

print(precision_score(y_true_2, y_pred_2))
# 1.0

print(precision_score(y_true_2, y_pred_2, pos_label=0))
# 0.25

print(precision_score(y_true_2, y_pred_2, average='macro'))
# 0.625

print(precision_score(y_true_2, y_pred_2, average='micro'))
# 0.4

print(precision_score(y_true_2, y_pred_2, average='weighted'))
# 0.85

y_true_ab = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']
y_pred_ab = ['A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B']

# print(precision_score(y_true_ab, y_pred_ab))
# ValueError: pos_label=1 is not a valid label: array(['A', 'B'], dtype='<U1')

print(precision_score(y_true_ab, y_pred_ab, pos_label='A'))
# 0.25
