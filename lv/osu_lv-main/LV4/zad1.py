import pandas as pd
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')

# A
y = data['CO2 Emissions (g/km)']
X = data[['Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)',
          'Fuel Consumption Comb (L/100km)', 'Engine Size (L)', 'Fuel Consumption Comb (mpg)', 'Cylinders']]

(X_train, X_test, y_train, y_test) = train_test_split(
    X, y, test_size=0.2, random_state=1)

# B
fuel_train = X_train['Fuel Consumption City (L/100km)']
fuel_test = X_test['Fuel Consumption City (L/100km)']

plt.scatter(fuel_train, y_train, c='green', s=2)
plt.scatter(fuel_test, y_test, c='orange', s=2)
plt.legend(['Training data', 'Test data'])
plt.show()

# C
sc = StandardScaler()
X_train_n = pd.DataFrame(sc.fit_transform(X_train))
X_test_n = pd.DataFrame(sc.transform(X_test))

plt.hist(X_train["Fuel Consumption City (L/100km)"], bins=15, color="green")
plt.title('Prije skaliranja')
plt.show()
plt.hist(X_train_n[0], bins=15, color="orange")
plt.title('Poslije skaliranja')
plt.show()

# D
linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)
for t in range(len(linearModel.singular_)):
    print("theta", t, ":", round(linearModel.singular_[t], 5))

# E
y_test_prediction = linearModel.predict(X_test_n)
plt.scatter(y_test, y_test_prediction, c='green', s=2)
plt.xlabel("Stvarna vrijednost")
plt.ylabel("Izracunata vrijednost")
plt.show()

# F
MAE = mean_absolute_error(y_test, y_test_prediction)
MAPE = mean_absolute_percentage_error(y_test, y_test_prediction)
MSE = mean_squared_error(y_test, y_test_prediction)
R2 = r2_score(y_test, y_test_prediction)

print("UZETE SVE NUMERIČKE VELIČINE:")
print("Srednja apsolutna pogreška iznosi", round(MAE, 2))
print("Srednja apsolutna postotna pogreška iznosi", round(MAPE, 2))
print("Srednja kvadratna pogreška iznosi", round(MSE, 2))
print("Koeficijent determinacije (R2) iznosi", round(R2, 2))

# G
X_smaller = data[[
    'Fuel Consumption City (L/100km)', 'Engine Size (L)', 'Cylinders']]

(X_train, X_test, y_train, y_test) = train_test_split(
    X_smaller, y, test_size=0.2, random_state=1)

X_train_n = pd.DataFrame(sc.fit_transform(X_train))
X_test_n = pd.DataFrame(sc.transform(X_test))

linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)

y_test_prediction = linearModel.predict(X_test_n)

MAE = mean_absolute_error(y_test, y_test_prediction)
MAPE = mean_absolute_percentage_error(y_test, y_test_prediction)
MSE = mean_squared_error(y_test, y_test_prediction)
R2 = r2_score(y_test, y_test_prediction)

print("UZETO 3 OD 6 NUMERIČKIH VELIČINA:")
print("Srednja apsolutna pogreška iznosi", round(MAE, 2))
print("Srednja apsolutna postotna pogreška iznosi", round(MAPE, 2))
print("Srednja kvadratna pogreška iznosi", round(MSE, 2))
print("Koeficijent determinacije (R2) iznosi", round(R2, 2))
