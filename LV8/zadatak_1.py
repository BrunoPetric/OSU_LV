import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import sklearn.metrics
from keras . models import load_model

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa
imgplot = plt.imshow(x_train[0])
plt.title(y_train[0])
plt.show()
imgplot = plt.imshow(x_train[20])
plt.title(y_train[20])
plt.show()
imgplot = plt.imshow(x_train[50])
plt.title(y_train[50])
plt.show()


# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)

x_train_s = x_train_s.reshape(60000,784)
x_test_s = x_test_s.reshape(10000,784)
# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu

model = keras . Sequential ()
model .add ( layers . Input ( shape =(784, )))
model .add ( layers . Dense (100, activation ="relu"))
model .add ( layers . Dense (50, activation ="relu"))
model .add ( layers . Dense (10, activation ="softmax"))
model . summary ()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

model . compile ( loss ="categorical_crossentropy" ,
optimizer ="adam",
metrics =["accuracy" ,])
batch_size = 32
epochs = 10


# TODO: provedi ucenje mreze
history = model .fit ( x_train_s ,
y_train_s ,
batch_size = batch_size ,
epochs = epochs ,
validation_split = 0.1)
predictions = model . predict ( x_test_s )

predict_class = np.argmax(predictions, axis=1)

# TODO: Prikazi test accuracy i matricu zabune
score = model . evaluate ( x_test_s , y_test_s , verbose =0)
print(score)
confusion_matrix = sklearn.metrics.confusion_matrix(y_test, predict_class)
cm_display = sklearn.metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)
cm_display.plot()
plt.show()
# TODO: spremi model
model . save ("FCN/")
