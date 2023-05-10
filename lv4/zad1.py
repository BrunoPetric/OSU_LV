import sklearn . linear_model as lm
import pandas as pd
from sklearn . model_selection import train_test_split
import matplotlib . pyplot as plt
from sklearn . preprocessing import MinMaxScaler
import sklearn . linear_model as lm
from sklearn . metrics import mean_absolute_error
from sklearn import metrics
import math

data = pd.read_csv('data_C02_emission.csv')

input_variables = ['Fuel Consumption City (L/100km)',
                   'Fuel Consumption Hwy (L/100km)',
                   'Fuel Consumption Comb (L/100km)',
                   'Fuel Consumption Comb (mpg)',
                   'Engine Size (L)',
                   'Cylinders']

output_variable = ['CO2 Emissions (g/km)']
x = data[input_variables].to_numpy()
y = data[output_variable].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)

plt.scatter(X_train[:, 1], y_train)
plt.scatter(X_test[:, 1], y_test)
plt.show()

sc = MinMaxScaler()
X_train_n = sc . fit_transform(X_train)
X_test_n = sc . transform(X_test)


plt.hist(X_train[:, 1])
plt.show()
plt.hist(X_train_n[:, 1])
plt.show()

linearModel = lm . LinearRegression()
linearModel . fit(X_train_n, y_train)
print(linearModel.coef_)

y_test_p = linearModel . predict(X_test_n)

plt.scatter(X_test[:, 1], y_test)
plt.scatter(X_test[:, 1], y_test_p)
plt.show()

print('mean squared error: ', metrics.mean_squared_error(y_test, y_test_p))
print('root mean squared error: ', math.sqrt(metrics.mean_squared_error(y_test, y_test_p)))
print('mean absolute error: ', mean_absolute_error(y_test, y_test_p))
print('mean absolute percentage_error: ',
      metrics.mean_absolute_percentage_error(y_test, y_test_p))
print('r2 score: ', metrics.r2_score(y_test, y_test_p))
