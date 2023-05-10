import numpy as np
import matplotlib . pyplot as plt
img = plt . imread ("road.jpg")
img = img [ :,:,0]. copy ()
plt . figure ()
plt . imshow ( img , cmap ="gray")
plt.title('original')
plt . show ()

plt . figure ()
plt . imshow ( img , cmap ="gray", alpha=0.5)
plt.title('posvijetliti')
plt . show ()

sirina = img.shape[1]

img_cet = img[:, int(sirina/4) : int(sirina/2)]
plt . figure ()
plt . imshow ( img_cet, cmap ="gray")
plt.title('druga cetvrtina')
plt . show ()

plt . figure ()
plt . imshow ( np.rot90(img), cmap ="gray")
plt.title('druga cetvrtina')
plt . show ()

plt . figure ()
plt . imshow ( np.fliplr(img), cmap ="gray")
plt.title('druga cetvrtina')
plt . show ()

