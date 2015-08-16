import matplotlib.pyplot as plt
import image
import numpy as np
import random


from skimage import io

images = io.ImageCollection('./photo/*')

fig, axes = plt.subplots(nrows=2, ncols=len(images))

for i in range(len(images)):
    img = image.Image(images[i])
    axes[0][i].imshow(img.img)
    axes[1][i].imshow(img.selected_img())

plt.show()