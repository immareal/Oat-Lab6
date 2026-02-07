from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open('kim.jpg')
c = im.histogram()

nr = []
ng = []
nb = []

for i in range(256):
    nr.append(c[i])
    ng.append(c[i+256])
    nb.append(c[i+512])

x = np.arange(256)

mean_r = np.sum(x * nr) / np.sum(nr)
mean_g = np.sum(x * ng) / np.sum(ng)
mean_b = np.sum(x * nb) / np.sum(nb)

plt.style.use('_mpl-gallery')
plt.xlabel('color value (0-255)')
plt.ylabel('pixel counts')

plt.plot(x, nr, c='r')
plt.plot(x, ng, c='g')
plt.plot(x, nb, c='b')

plt.axvline(mean_r, c='r', linestyle='--')
plt.axvline(mean_g, c='g', linestyle='--')
plt.axvline(mean_b, c='b', linestyle='--')

plt.show()