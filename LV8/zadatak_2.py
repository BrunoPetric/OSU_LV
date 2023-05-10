import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import sklearn.metrics
from keras . models import load_model

model = load_model ("FCN/")
model . summary ()

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

history = model .fit ( x_train_s ,
y_train_s ,
batch_size = batch_size ,
epochs = epochs ,
validation_split = 0.1)
predictions = model . predict ( x_test_s )

predict_class = np.argmax(predictions, axis=1)

razlika = np.where()
