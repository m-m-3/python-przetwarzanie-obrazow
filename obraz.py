import urllib.request
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

url = "https://picsum.photos/id/1045/500/400"
with urllib.request.urlopen( url ) as plik:
    obraz = mpimg.imread(plik, format="jpg")

plt.imshow(obraz)
plt.axis("off")
plt.show()

obraz = cv2.resize(obraz, None, fx=0.5, fy=0.5)
obraz = cv2.cvtColor(obraz, cv2.COLOR_RGB2GRAY)
obraz = cv2.rotate(obraz, cv2.ROTATE_90_CLOCKWISE)

plt.imshow(obraz, cmap="gray")
plt.axis("off")
plt.show()
np.set_printoptions(threshold=np.inf, linewidth=200)
print(obraz)

