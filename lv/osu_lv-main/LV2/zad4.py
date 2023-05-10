import numpy as np
import matplotlib.pyplot as plt

white = np.ones((50, 50)) * 255
black = np.zeros((50, 50))

upper_row = np.hstack((black, white))
lower_row = np.hstack((white, black))
img = np.vstack((upper_row, lower_row))

plt.figure()
plt.title("Slika")
plt.imshow(img, cmap="gray")
plt.show()
