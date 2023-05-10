import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import precision_score, recall_score, accuracy_score

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#A
plt.scatter(X_train[:, 0], X_train[:, 1], marker="o", c=y_train, s=15, cmap=mcolors.ListedColormap(["red", "blue"]))
plt.scatter(X_test[:, 0], X_test[:, 1], marker="x", c=y_test, s=25, cmap=mcolors.ListedColormap(["red", "blue"]))

#B
LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)

#C
theta0 = LogRegression_model.intercept_
coefs = LogRegression_model.coef_.T
a = -coefs[0]/coefs[1]
c = -theta0/coefs[1]
xymin, xymax = -4, 4
xd = np.array([xymin, xymax])
yd = a*xd + c
plt.plot(xd, yd, linestyle='--')
plt.show()

#D
y_test_p = LogRegression_model.predict(X_test)

cm = confusion_matrix(y_test, y_test_p)
print("Matrica zabune:", cm)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot()
plt.show()

print('Točnost:', round(accuracy_score(y_test, y_test_p), 2))
print('Preciznost:', round(precision_score(y_test, y_test_p), 2))
print('Odziv:', round(recall_score(y_test, y_test_p), 2))

#E
y_color = (y_test == y_test_p)
plt.scatter(X_test[:, 0], X_test[:, 1], marker="o", c=y_color, s=25, cmap=mcolors.ListedColormap(["red", "green"]))
plt.show()