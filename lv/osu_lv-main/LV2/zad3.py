import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road.jpg")
img = img[:,:,0].copy()

#A
add_brightness = 150
light_img = np.where((255 - img) < add_brightness, 255, img+add_brightness)

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()
plt.title("A) Svjetlija slika")
plt.imshow(light_img, cmap="gray")
plt.show()

#B
quarters = np.hsplit(img, 4)
second_quarter = quarters[1]
plt.title("B) Druga četvrtina")
plt.imshow(second_quarter, cmap="gray")
plt.show()

#C
rotated = np.rot90(img)
rotated = np.rot90(rotated)
rotated = np.rot90(rotated)
plt.title("C) Rotirano za 90°")
plt.imshow(rotated, cmap="gray")
plt.show()

#D
mirror = np.flip(img, axis=1)
plt.title("D) Zrcaljena slika")
plt.imshow(mirror, cmap="gray")
plt.show()
