from sklearn.metrics import classification_report
import pandas as pd
import pprint

y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]

print(classification_report(y_true, y_pred))
#               precision    recall  f1-score   support
# 
#            0       0.25      0.20      0.22         5
#            1       0.33      0.40      0.36         5
# 
#    micro avg       0.30      0.30      0.30        10
#    macro avg       0.29      0.30      0.29        10
# weighted avg       0.29      0.30      0.29        10
# 

print(type(classification_report(y_true, y_pred)))
# <class 'str'>

print(classification_report(y_true, y_pred,
                            target_names=['class_0', 'class_1']))
#               precision    recall  f1-score   support
# 
#      class_0       0.25      0.20      0.22         5
#      class_1       0.33      0.40      0.36         5
# 
#    micro avg       0.30      0.30      0.30        10
#    macro avg       0.29      0.30      0.29        10
# weighted avg       0.29      0.30      0.29        10
# 

d = classification_report(y_true, y_pred, output_dict=True)

pprint.pprint(d)
# {'0': {'f1-score': 0.22222222222222224,
#        'precision': 0.25,
#        'recall': 0.2,
#        'support': 5},
#  '1': {'f1-score': 0.3636363636363636,
#        'precision': 0.3333333333333333,
#        'recall': 0.4,
#        'support': 5},
#  'macro avg': {'f1-score': 0.29292929292929293,
#                'precision': 0.29166666666666663,
#                'recall': 0.30000000000000004,
#                'support': 10},
#  'micro avg': {'f1-score': 0.3, 'precision': 0.3, 'recall': 0.3, 'support': 10},
#  'weighted avg': {'f1-score': 0.29292929292929293,
#                   'precision': 0.29166666666666663,
#                   'recall': 0.3,
#                   'support': 10}}

print(d['0'])
# {'precision': 0.25, 'recall': 0.2, 'f1-score': 0.22222222222222224, 'support': 5}

print(d['0']['precision'])
# 0.25

print(type(d['0']['precision']))
# <class 'float'>

df = pd.DataFrame(d)

print(df)
#                   0         1  micro avg  macro avg  weighted avg
# f1-score   0.222222  0.363636        0.3   0.292929      0.292929
# precision  0.250000  0.333333        0.3   0.291667      0.291667
# recall     0.200000  0.400000        0.3   0.300000      0.300000
# support    5.000000  5.000000       10.0  10.000000     10.000000

print(df.iloc[:, :-3])
#                   0         1
# f1-score   0.222222  0.363636
# precision  0.250000  0.333333
# recall     0.200000  0.400000
# support    5.000000  5.000000

print(df.iloc[:, -3:])
#            micro avg  macro avg  weighted avg
# f1-score         0.3   0.292929      0.292929
# precision        0.3   0.291667      0.291667
# recall           0.3   0.300000      0.300000
# support         10.0  10.000000     10.000000
