import pandas as pd
import matplotlib . pyplot as plt
import numpy as np

# A dio zadatka

data = pd.read_csv('data_C02_emission.csv')

#Dropanje duplikata i nepostojećih vrijednosti
data.dropna(axis=0)
data.drop_duplicates()

#Resetiranje indexa 

data = data.reset_index(drop=True)

#Pretvaranje [stupaca] u svakom retku u type category
for col in ['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']:
    data[col] = data[col].astype('category')

print(len(data))
print(data.info())
print("\n")
print("\n")

# B dio zadatka

#Sortiranje date po [ovom stupcu] i u padajucem nizu
data_by_fc_city = data.sort_values(
    by=['Fuel Consumption City (L/100km)'], ascending=False)
print(data_by_fc_city[['Make', 'Model',
      'Fuel Consumption City (L/100km)']].head(3))
print(data_by_fc_city[['Make', 'Model',
      'Fuel Consumption City (L/100km)']].tail(3))

print("\n")
print("\n")

# C dio zadatka

#Iz date uzeti [retke di je engine size veci od 2.5 i manji od 3.5]
data_by_motor_size = data[(data['Engine Size (L)'] > 2.5)
                          & (data['Engine Size (L)'] < 3.5)]
print(len(data_by_motor_size))
print(data_by_motor_size['CO2 Emissions (g/km)'].mean())

print("\n")
print("\n")

# D dio zadatka

#Iz data uzeti sve retke di je data[Make] jednak audi
data_only_audi = data[(data['Make'] == "Audi")]
print(len(data_only_audi))
print(data_only_audi[(data['Cylinders'] == 4)]['CO2 Emissions (g/km)'].mean())

print("\n")
print("\n")

# E dio zadatka

#Grupiro sam prema cylindrima
data_g_by_cylinders = data.groupby('Cylinders')
print(data_g_by_cylinders['Cylinders'].count())
print(data_g_by_cylinders['CO2 Emissions (g/km)'].mean())

print("\n")
print("\n")

# F dio zadatka

#Uzmi sva vozila iz date gdje je data[fuel] = d i od tih vozila uzmi [fuel consumption] i izracunaj mean
print(data[(data['Fuel Type'] == 'D')]
      ['Fuel Consumption City (L/100km)'].mean())
print(data[(data['Fuel Type'] == 'D')]
      ['Fuel Consumption City (L/100km)'].median())

print(data[(data['Fuel Type'] == 'X')]
      ['Fuel Consumption City (L/100km)'].mean())
print(data[(data['Fuel Type'] == 'X')]
      ['Fuel Consumption City (L/100km)'].median())

print("\n")
print("\n")

# G dio zadatka

new_data = data[(data['Cylinders'] == 4) & (data['Fuel Type'] == 'D')]
sorted_new_data = new_data.sort_values(
    by=['Fuel Consumption City (L/100km)'])
print(sorted_new_data.head(1))

print("\n")
print("\n")

# H dio zadatka

print(data[(data['Transmission'] == 'M')].count())


#I dio zadatka

