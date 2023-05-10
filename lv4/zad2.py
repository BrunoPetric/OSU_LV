import sklearn . linear_model as lm
import pandas as pd
from sklearn . model_selection import train_test_split
import matplotlib . pyplot as plt
from sklearn . preprocessing import MinMaxScaler
import sklearn . linear_model as lm
from sklearn . metrics import mean_absolute_error
from sklearn import metrics
from sklearn . preprocessing import OneHotEncoder
import math
import numpy
data = pd.read_csv('data_C02_emission.csv')

ohe = OneHotEncoder()
X_encoded = ohe . fit_transform(data[['Fuel Type']]) . toarray()

input_variables = ['Fuel Consumption City (L/100km)',
                   'Fuel Consumption Hwy (L/100km)',
                   'Fuel Consumption Comb (L/100km)',
                   'Fuel Consumption Comb (mpg)',
                   'Engine Size (L)',
                   'Cylinders',
                   'Fuel Type']

output_variable = ['CO2 Emissions (g/km)']
data['Fuel Type'] = X_encoded
x = data[input_variables].to_numpy()
y = data[output_variable].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)


linearModel = lm . LinearRegression()
linearModel . fit(X_train, y_train)
print(linearModel.coef_)

y_test_p = linearModel . predict(X_test)

plt.scatter(X_test[:, 1], y_test)
plt.scatter(X_test[:, 1], y_test_p)
plt.show()

print('mean squared error: ', metrics.mean_squared_error(y_test, y_test_p))
print('root mean squared error: ', math.sqrt(
    metrics.mean_squared_error(y_test, y_test_p)))
print('mean absolute error: ', mean_absolute_error(y_test, y_test_p))
print('mean absolute percentage_error: ',
      metrics.mean_absolute_percentage_error(y_test, y_test_p))
print('r2 score: ', metrics.r2_score(y_test, y_test_p))
print('Maximalna pogreska: ', metrics.max_error(y_test, y_test_p))
error = abs(y_test_p - y_test)
id = numpy.argmax(error)
print('najvecu pogresku ima: ', data.loc[id]['Model'])
