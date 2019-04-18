from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]

cm = confusion_matrix(y_true, y_pred)

print(cm)
# [[1 4]
#  [3 2]]

sns.heatmap(cm)
plt.savefig('data/dst/sklearn_confusion_matrix.png')
plt.close()

sns.heatmap(cm, annot=True, cmap='Blues')
plt.savefig('data/dst/sklearn_confusion_matrix_annot_blues.png')
plt.close()
