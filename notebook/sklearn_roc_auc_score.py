from sklearn.metrics import roc_auc_score
import numpy as np

y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1])
y_score = np.array([0.2, 0.3, 0.6, 0.8, 0.4, 0.5, 0.7, 0.9])

print(roc_auc_score(y_true, y_score))
# 0.6875

y_true_perfect = np.array([0, 0, 0, 0, 1, 1, 1, 1])
y_score_perfect = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])

print(roc_auc_score(y_true_perfect, y_score_perfect))
# 1.0

np.random.seed(0)
y_true_random = np.array([0] * 5000 + [1] * 5000)
y_score_random = np.random.rand(10000)

print(roc_auc_score(y_true_random, y_score_random))
# 0.49895535999999996

y_score_inv = 1 - y_score
print(y_score_inv)
# [0.8 0.7 0.4 0.2 0.6 0.5 0.3 0.1]

print(roc_auc_score(y_true, y_score_inv))
# 0.3125

y_score_perfect_inv = 1 - y_score_perfect
print(y_score_perfect_inv)
# [0.9 0.8 0.7 0.6 0.5 0.4 0.3 0.2]

print(roc_auc_score(y_true_perfect, y_score_perfect_inv))
# 0.0
