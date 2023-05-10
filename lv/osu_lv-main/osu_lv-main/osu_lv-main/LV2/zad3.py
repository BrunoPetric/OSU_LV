import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('road.jpg')
img = img[:,:,0].copy()
plt.imshow(img, cmap='gray')
plt.show()
imgBright = img+150
imgBright[img > 105] = 255
plt.imshow(imgBright, cmap='gray')
plt.show()

columns = img[1,:].size
imgSecondQuarter = img[:,int(columns/4):int(columns/2)]
plt.imshow(imgSecondQuarter, cmap='gray')
plt.show()

imgRot90 = np.rot90(img, axes=(1,0))
plt.imshow(imgRot90, cmap='gray')
plt.show()

imgFlip = np.flip(img, axis=1)
plt.imshow(imgFlip, cmap='gray')
plt.show()