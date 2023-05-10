import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6, num=30)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, "b", linewidth =5, marker =".", markersize=5)
plt.plot(x, z, "g", linewidth =5, marker =".", markersize=5)
plt.axis([0, 6, -2, 2])
plt.xlabel("x")
plt.ylabel("vrijednosti funkcije")
plt.title("sinus funkcija")
plt.show()