from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

y_true = [0, 0, 0, 0, 1, 1, 1, 1]
y_score = [0.2, 0.3, 0.6, 0.8, 0.4, 0.5, 0.7, 0.9]

roc = roc_curve(y_true, y_score)

print(type(roc))
# <class 'tuple'>

print(len(roc))
# 3

fpr, tpr, thresholds = roc_curve(y_true, y_score)

print(fpr)
# [0.   0.   0.25 0.25 0.5  0.5  1.  ]

print(tpr)
# [0.   0.25 0.25 0.5  0.5  1.   1.  ]

print(thresholds)
# [1.9 0.9 0.8 0.7 0.6 0.4 0.2]

plt.plot(fpr, tpr, marker='o')
plt.xlabel('FPR: False positive rate')
plt.ylabel('TPR: True positive rate')
plt.grid()
plt.savefig('data/dst/sklearn_roc_curve.png')
plt.close()

fpr_all, tpr_all, thresholds_all = roc_curve(y_true, y_score,
                                             drop_intermediate=False)

print(fpr_all)
# [0.   0.   0.25 0.25 0.5  0.5  0.5  0.75 1.  ]

print(tpr_all)
# [0.   0.25 0.25 0.5  0.5  0.75 1.   1.   1.  ]

print(thresholds_all)
# [1.9 0.9 0.8 0.7 0.6 0.5 0.4 0.3 0.2]

plt.plot(fpr_all, tpr_all, marker='o')
plt.xlabel('FPR: False positive rate')
plt.ylabel('TPR: True positive rate')
plt.grid()
plt.savefig('data/dst/sklearn_roc_curve_all.png')
plt.close()
