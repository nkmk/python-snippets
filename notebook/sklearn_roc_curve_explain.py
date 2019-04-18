from sklearn.metrics import roc_curve, recall_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1])
y_score = np.array([0.2, 0.3, 0.6, 0.8, 0.4, 0.5, 0.7, 0.9])

print(y_score >= 0.5)
# [False False  True  True False  True  True  True]

print((y_score >= 0.5).astype(int))
# [0 0 1 1 0 1 1 1]

def fpr_score(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).flatten()
    return fp / (tn + fp)

print(fpr_score(y_true, y_score >= 0.5))
# 0.5

print(recall_score(y_true, y_score >= 0.5))
# 0.75

th_min = min(y_score)
print(th_min)
# 0.2

print((y_score >= th_min).astype(int))
# [1 1 1 1 1 1 1 1]

print(fpr_score(y_true, y_score >= th_min))
# 1.0

print(recall_score(y_true, y_score >= th_min))
# 1.0

th_max = max(y_score) + 1
print(th_max)
# 1.9

print((y_score >= th_max).astype(int))
# [0 0 0 0 0 0 0 0]

print(fpr_score(y_true, y_score >= th_max))
# 0.0

print(recall_score(y_true, y_score >= th_max))
# 0.0

df = pd.DataFrame({'true': y_true, 'score': y_score})

df['TPR'] = df.apply(lambda row: recall_score(y_true, y_score >= row['score']), axis=1)
df['FPR'] = df.apply(lambda row: fpr_score(y_true, y_score >= row['score']), axis=1)

print(df)
#    true  score   TPR   FPR
# 0     0    0.2  1.00  1.00
# 1     0    0.3  1.00  0.75
# 2     0    0.6  0.50  0.50
# 3     0    0.8  0.25  0.25
# 4     1    0.4  1.00  0.50
# 5     1    0.5  0.75  0.50
# 6     1    0.7  0.50  0.25
# 7     1    0.9  0.25  0.00

print(df.sort_values('score', ascending=False))
#    true  score   TPR   FPR
# 7     1    0.9  0.25  0.00
# 3     0    0.8  0.25  0.25
# 6     1    0.7  0.50  0.25
# 2     0    0.6  0.50  0.50
# 5     1    0.5  0.75  0.50
# 4     1    0.4  1.00  0.50
# 1     0    0.3  1.00  0.75
# 0     0    0.2  1.00  1.00

fpr_all, tpr_all, th_all = roc_curve(y_true, y_score,
                                     drop_intermediate=False)

df_roc = pd.DataFrame({'th_all': th_all, 'tpr_all': tpr_all, 'fpr_all': fpr_all})

print(df_roc)
#    th_all  tpr_all  fpr_all
# 0     1.9     0.00     0.00
# 1     0.9     0.25     0.00
# 2     0.8     0.25     0.25
# 3     0.7     0.50     0.25
# 4     0.6     0.50     0.50
# 5     0.5     0.75     0.50
# 6     0.4     1.00     0.50
# 7     0.3     1.00     0.75
# 8     0.2     1.00     1.00

y_true_perfect = np.array([0, 0, 0, 0, 1, 1, 1, 1])
y_score_perfect = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])

print(y_true_perfect)
# [0 0 0 0 1 1 1 1]

print((y_score_perfect >= 0.5).astype(int))
# [0 0 0 0 1 1 1 1]

print(fpr_score(y_true_perfect, y_score_perfect >= 0.5))
# 0.0

print(recall_score(y_true_perfect, y_score_perfect >= 0.5))
# 1.0

roc_p = roc_curve(y_true_perfect, y_score_perfect, drop_intermediate=False)

plt.plot(roc_p[0], roc_p[1], marker='o')
plt.xlabel('FPR: False positive rate')
plt.ylabel('TPR: True positive rate')
plt.grid()
plt.savefig('data/dst/sklearn_roc_curve_perfect.png')
plt.close()

y_true_1 = np.array([0, 0, 0, 1, 0, 1, 1, 1])
y_score_1 = y_score_perfect

roc_1 = roc_curve(y_true_1, y_score_1, drop_intermediate=False)

y_true_2 = np.array([0, 0, 1, 1, 0, 0, 1, 1])
y_score_2 = y_score_perfect

roc_2 = roc_curve(y_true_2, y_score_2, drop_intermediate=False)

plt.plot(roc_p[0], roc_p[1], marker='s')
plt.plot(roc_1[0], roc_1[1], marker='o')
plt.plot(roc_2[0], roc_2[1], marker='x')
plt.xlabel('FPR: False positive rate')
plt.ylabel('TPR: True positive rate')
plt.grid()
plt.savefig('data/dst/sklearn_roc_curve_compare.png')
plt.close()

y_true_org = np.array([0, 0, 1, 1, 0, 0, 1, 1])
y_score_org = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])

roc_org = roc_curve(y_true_org, y_score_org, drop_intermediate=False)

y_score_scale = y_score_org / 2
print(y_score_scale)
# [0.05 0.1  0.15 0.2  0.25 0.3  0.35 0.4 ]

roc_scale = roc_curve(y_true_org, y_score_scale, drop_intermediate=False)

y_score_interval = np.array([0.01, 0.02, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96])

roc_interval = roc_curve(y_true_org, y_score_interval, drop_intermediate=False)

plt.plot(roc_org[0], roc_org[1], marker='s')
plt.plot(roc_scale[0], roc_scale[1], marker='o', linestyle='-.')
plt.plot(roc_interval[0], roc_interval[1], marker='x', linestyle=':')
plt.xlabel('FPR: False positive rate')
plt.ylabel('TPR: True positive rate')
plt.grid()
plt.savefig('data/dst/sklearn_roc_curve_same.png')
plt.close()

s = pd.Series(y_score_interval)

print(s)
# 0    0.01
# 1    0.02
# 2    0.91
# 3    0.92
# 4    0.93
# 5    0.94
# 6    0.95
# 7    0.96
# dtype: float64

print(s.rank())
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0
# 4    5.0
# 5    6.0
# 6    7.0
# 7    8.0
# dtype: float64

np.random.seed(0)
y_true_random = np.array([0] * 5000 + [1] * 5000)
y_score_random = np.random.rand(10000)

roc_random = roc_curve(y_true_random, y_score_random)

plt.plot(roc_random[0], roc_random[1])
plt.xlabel('FPR: False positive rate')
plt.ylabel('TPR: True positive rate')
plt.grid()
plt.savefig('data/dst/sklearn_roc_curve_random.png')
plt.close()
