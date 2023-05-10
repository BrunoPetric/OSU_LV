import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=",", dtype=float, skiprows=1)

#A
print("a) Mjerenja su izvršena na", data.shape[0], "ljudi.")

#B
x = data[:, 1]
y = data[:, 2]

plt.title("b) Omjer visine i težine")
plt.xlabel("Visina")
plt.ylabel("Težina")
plt.scatter(x, y, color="g")
plt.show()

#C
x_50 = data[:,1][::50]
y_50 = data[:,2][::50]

plt.title("c) Omjer visine i težine za svaku 50u osobu")
plt.xlabel("Visina")
plt.ylabel("Težina")
plt.scatter(x_50, y_50, color="g")
plt.show()

#D
#vektor x već sadrži sve visine u ovom skupu
print("d) Najmanja visina u skupu je", min(x), "cm, a najveća", max(x), "cm.")
print("Prosječna visina u skupu iznosi", round(x_50.mean(), 2), "cm.")

#E
m = data[np.where(data[:,0] == 1)]
f = data[np.where(data[:,0] == 0)]
m = m[:,1]
f = f[:,1]

print("e) Najmanja visina u muškom skupu je", min(m), "cm, a najveća", max(m), "cm.")
print("Prosječna visina u muškom skupu iznosi", round(m.mean(), 2), "cm.")
print("Najmanja visina u ženskom skupu je", min(f), "cm, a najveća", max(f), "cm.")
print("Prosječna visina u ženskom skupu iznosi", round(f.mean(), 2), "cm.")
