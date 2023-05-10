from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn . linear_model as lm

data = pd.read_csv('data_C02_emission.csv')

data = data.drop(["Make", "Model"], axis = 1)

#Ulazne varijable

input_variables = ['Fuel Consumption City (L/100km)',
                   'Fuel Consumption Hwy (L/100km)',
                   'Fuel Consumption Comb (L/100km)',
                   'Fuel Consumption Comb (mpg)',
                   'Cylinders']

# Zadatak pod a)


#Izlazna varijabla
output_variable = ['CO2 Emissions (g/km)']

#Pretvaranje u numpy polje
x = data[input_variables].to_numpy()
y = data[output_variable].to_numpy()

#Splitanje na training i test podatke
X_train, X_test = train_test_split(x, test_size = 0.2, random_state =1)
y_train, y_test = train_test_split(y, test_size = 0.2, random_state =1)

# Zadatak pod b)

#Za svaki ulaz i izlaz crtanje grafa 

for i in range(len(input_variables)):
    train_data_x = X_train[:, i]
    train_data_y = y_train
    test_data_x = X_test[:,i]
    test_data_y = y_test
    plt.scatter(train_data_x,train_data_y, color = "blue",label = "Train")
    plt.scatter(test_data_x,test_data_y, color = "red",label = "Train")
    plt.xlabel("Input varijabla")
    plt.ylabel("C02 Emission")
    plt.show()


# Zadatak pod c)

#Definiranje scalera (MinMax ima i Standard)
sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)

for i in range(len(input_variables)):
    train_data_x = X_train[:, i]
    scaled_train_X = X_train_n[:,i]
    plt.hist(train_data_x, bins = 20)
    plt.show()

    plt.hist(scaled_train_X, bins = 20)
    plt.show

# Zadatak pod d)

#Pravljenje modela i treniranje na skuou za trening

linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)
print("Intercept", linearModel.intercept_)
print(linearModel.coef_)

# Zadatak pod e)

#Model predikta y na osnovu x testova

y_pred_test = linearModel.predict(X_test_n)
fig, ax = plt.subplots(1, 2, sharex='col', sharey='row')
ax[0].scatter(X_test_n[:, 0], y_test)
ax[1].scatter(X_test_n[:, 0], y_pred_test)
plt.show()

# Zadatak pod f)

RMSE = mean_squared_error(y_test, y_pred_test squared=False)
MAE = mean_absolute_error(y_test, y_pred_test)
MAPE = mean_absolute_percentage_error(y_test, y_pred_test)
R2 = r2_score(y_test, y_pred_test)

# Zadatak pod g)

print("RMSE", RMSE)
print("MAE", MAE)
print("MAPE", MAPE)
print("R2", R2)