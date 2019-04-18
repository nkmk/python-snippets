from sklearn.metrics import accuracy_score

y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]

print(accuracy_score(y_true, y_pred))
# 0.3
