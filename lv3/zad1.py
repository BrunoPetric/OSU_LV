import pandas as pd
import matplotlib.pyplot as plt
data = pd . read_csv ('data_C02_emission.csv')
print ('Broj mjerenja: ', len ( data ))
print ( data . info () )
print ( data . isnull () . sum () )
data . dropna ( axis =0 )
data . dropna ( axis =1 )
data . drop_duplicates ()
data = data . reset_index ( drop = True )

cols = ['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']
data[cols] = data[cols].astype('category')
print ( data . info () )

sort_data = data.sort_values(by=['Fuel Consumption City (L/100km)']) 
print ( sort_data [['Make','Model', 'Fuel Consumption City (L/100km)']].head(3))
print ( sort_data [['Make','Model', 'Fuel Consumption City (L/100km)']].tail(3))

c_data = (data [( data ['Engine Size (L)'] >= 2.5  ) & ( data ['Engine Size (L)'] <= 3.5 )])
print('Broj vozila koja imaju velicinu motora izmedu 2.5 i 3.5 L: ', len(c_data))
print('prosjecna C02 emisija plinova za ova vozila: ', c_data['CO2 Emissions (g/km)'].mean())

audi_data = (data[ data.Make == 'Audi'])
print('Broj audi vozila: ', len(audi_data))
audi4_data = (audi_data[audi_data.Cylinders == 4])
print('prosjecna emisija C02 plinova automobila proizvoda Audi koji imaju 4 cilindara: ', audi4_data['CO2 Emissions (g/km)'].mean())

even_data = (data[ data.Cylinders %2 == 0])
new_data = even_data.groupby('Cylinders').apply(print)
#new_filtered_data = (new_data[new_data.Cylinders.groups==4])
#print(new_data.Cylinders.describe())

dizel_data = (data[data['Fuel Type'] == 'D'])
print('prosjecna gradska potrošnja u slucaju vozila koja koriste dizel: ', dizel_data['Fuel Consumption City (L/100km)'].mean())
print('medijalna gradska potrošnja u slucaju vozila koja koriste dizel: ', dizel_data['Fuel Consumption City (L/100km)'].median())
benzin_data = (data[data['Fuel Type'] == 'X'])
print('prosjecna gradska potrošnja u slucaju vozila koja koriste regularni benzin: ', benzin_data['Fuel Consumption City (L/100km)'].mean())
print('medijalna gradska potrošnja u slucaju vozila koja koriste regularni benzin: ', benzin_data['Fuel Consumption City (L/100km)'].median())

dizel4_data = (dizel_data[dizel_data.Cylinders==4])
sort_dizel4_data = dizel4_data.sort_values(by=['Fuel Consumption City (L/100km)'])
print(sort_dizel4_data.tail(1))

print('Broj vozila sa rucnim mjenjacem: ', len(data[data['Transmission'].str.contains('M')]))

print(data.corr(numeric_only = True))
