import numpy as np
import matplotlib.pyplot as plt

black1 = np.zeros((50,50))
black2 = black1.copy()
white1 = np.ones((50,50))
white2 = white1.copy()
row1 = np.hstack((black1,white1))
row2 = np.hstack((white2, black2))
full = np.vstack((row1,row2))
plt.figure()
plt.imshow(full, cmap='gray')
plt.show()