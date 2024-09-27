import matplotlib.pyplot as plt
from PIL import Image
from sys import argv
from skimage import exposure, util
import numpy as np

filename = argv[1]
with Image.open(filename) as image:
    img = np.array(image)
    img = util.img_as_ubyte(img)

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

fig, axs = plt.subplots(4, 2)

axs[1, 0].imshow(img)
axs[1, 0].axis("off")
axs[1, 0].set_title("Исходное изображение")

axs[0, 0].axis("off")
axs[2, 0].axis("off")
axs[3, 0].axis("off")

histogram = image.histogram()
r_pil_hist = histogram[0:256]
g_pil_hist = histogram[256:512]
b_pil_hist = histogram[512:]

axs[0, 1].plot(r_pil_hist, color="#FF0000", label="R-канал")
axs[0, 1].plot(g_pil_hist, color="#00FF00")
axs[0, 1].plot(b_pil_hist, color="#0000FF")
axs[0, 1].set_title("Гистограмма изображения")


r_hist, r_bins = exposure.histogram(r)
axs[1, 1].plot(r_bins, r_hist, color="#FF0000")
axs[1, 1].set_title("Гистограмма R-канала")

g_hist, g_bins = exposure.histogram(g)
axs[2, 1].plot(g_bins, g_hist, color="#00FF00")
axs[2, 1].set_title("Гистограмма G-канала")

b_hist, b_bins = exposure.histogram(b)
axs[3, 1].plot(b_bins, b_hist, color="#0000FF")
axs[3, 1].set_title("Гистограмма B-канала")
plt.tight_layout()
plt.savefig("histogram.jpg")
plt.show()

