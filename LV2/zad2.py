import numpy as np
import matplotlib.pyplot as plt
import statistics
# using loadtxt()
arr = np.loadtxt("data.csv", skiprows=1, delimiter=",")
print('Broj osoba: ', len(arr)) 
plt.scatter(arr[:,1], arr[:,2])
plt.title('odnos visine i mase osobe')
plt.show()
a = arr[:,1]
b = arr[:,2]
plt.scatter(a[::50], b[::50])
plt.title('odnos visine i mase za svaku pedesetu osobu')
plt.show()
print('minimalna visina: ', a.min())
print('maksimalna visina: ', a.max())
print('srednja visina: ', a.mean())
print('-------------------------')
m = []
for osoba in arr:
    if (osoba[0] == 1):
        m.append(osoba[1])
print('minimalna visina muskaraca: ', min(m))
print('maksimalna visina muskaraca: ', max(m))
print('srednja visina muskaraca: ', statistics.mean(m))
print('-------------------------')
z = []
for osoba in arr:
    if (osoba[0] == 0):
        z.append(osoba[1])
print('minimalna visina zena: ', min(z))
print('maksimalna visina zena: ', max(z))
print('srednja visina zena: ', statistics.mean(z))
