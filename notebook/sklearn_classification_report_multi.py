from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report

y_true_multi = [0, 0, 0, 1, 1, 1, 2, 2, 2]
y_pred_multi = [0, 1, 1, 1, 1, 2, 2, 2, 2]

print(confusion_matrix(y_true_multi, y_pred_multi))
# [[1 2 0]
#  [0 2 1]
#  [0 0 3]]

# print(precision_score(y_true_multi, y_pred_multi))
# ValueError: Target is multiclass but average='binary'. Please choose another average setting.

print(precision_score(y_true_multi, y_pred_multi, average=None))
# [1.   0.5  0.75]

print(precision_score(y_true_multi, y_pred_multi, average='macro'))
# 0.75

print(precision_score(y_true_multi, y_pred_multi, average='micro'))
# 0.6666666666666666

print(precision_score(y_true_multi, y_pred_multi, average='weighted'))
# 0.75

print(classification_report(y_true_multi, y_pred_multi))
#               precision    recall  f1-score   support
# 
#            0       1.00      0.33      0.50         3
#            1       0.50      0.67      0.57         3
#            2       0.75      1.00      0.86         3
# 
#    micro avg       0.67      0.67      0.67         9
#    macro avg       0.75      0.67      0.64         9
# weighted avg       0.75      0.67      0.64         9
# 
