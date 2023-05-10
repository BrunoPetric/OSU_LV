from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# inicijalizacija i ucenje KNN modela
KNN_model = KNeighborsClassifier(n_neighbors=5)
KNN_model.fit(X_train, y_train)

# inicijalizacija i ucenje SVM modela
SVM_model = svm.SVC(kernel='rbf', gamma=1, C=0.1)
SVM_model.fit(X_train, y_train)

# predikcija na skupu podataka za testiranje
y_test_p_KNN = KNN_model.predict(X_test)
y_test_p_SVM = SVM_model.predict(X_test)

SVM_model.fit(X_train, y_train)
# predikcija na skupu podataka za testiranje
y_test_p = SVM_model.predict(X_test)

print(y_test)
print(y_test_p)

print('Precision: %.3f' % precision_score(y_test, y_test_p))
print('Recall: %.3f' % recall_score(y_test, y_test_p))
print('F1: %.3f' % f1_score(y_test, y_test_p))
print('Accuracy: %.3f' % accuracy_score(y_test, y_test_p))

#pr2
model = svm.SVC(kernel='linear', C=1, random_state=42)
scores = cross_val_score(model, X_train, y_train, cv=5)
print(scores)