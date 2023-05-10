import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn . metrics import accuracy_score, precision_score, recall_score
from sklearn . metrics import confusion_matrix , ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from matplotlib import colors

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

plt.scatter(X_train[:,0], X_train[:,1], c=y_train, s=10 )
plt.scatter(X_test[:,0], X_test[:,1],c=y_test, marker='x', s=10)
plt.show()

# inicijalizacija i ucenje modela logisticke regresije
LogRegression_model = LogisticRegression ()
LogRegression_model . fit ( X_train , y_train )
# predikcija na skupu podataka za testiranje
y_test_p = LogRegression_model . predict ( X_test )

# Retrieve the model parameters.
b = LogRegression_model.intercept_[0]
w1, w2 = LogRegression_model.coef_.T
# Calculate the intercept and gradient of the decision boundary.
c = -b/w2
m = -w1/w2
# Plot the data and the classification with the decision boundary.
xmin, xmax = -3, 3
ymin, ymax = -3, 3
xd = np.array([xmin, xmax])
yd = m*xd + c
plt.plot(xd, yd, 'k', lw=1, ls='--')
plt.scatter(X_train[:,0], X_train[:,1], c=y_train, s=10 )
plt.show()

# tocnost
print (" Tocnost : " , accuracy_score (y_test , y_test_p ))
print (" Preciznost : " , precision_score (y_test , y_test_p ))
print (" Odziv : " , recall_score (y_test , y_test_p ))
# matrica zabune
cm = confusion_matrix ( y_test , y_test_p )
print (" Matrica zabune : " , cm)
disp = ConfusionMatrixDisplay ( confusion_matrix (y_test , y_test_p ))
disp . plot ()
plt . show ()
# report
print ( classification_report (y_test , y_test_p ))
cmap = colors.ListedColormap(['black', 'green'])
plt.scatter(X_test[:,0], X_test[:,1], c=y_test==y_test_p, s=10, cmap=cmap)
plt.show()