from sklearn.metrics import precision_score

y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]

print(precision_score(y_true, y_pred))
# 0.3333333333333333
