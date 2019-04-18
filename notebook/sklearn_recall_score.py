from sklearn.metrics import recall_score

y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]

print(recall_score(y_true, y_pred))
# 0.4
