import matplotlib.pyplot as plt
import image


from skimage import io

images = io.ImageCollection('./photo/*')

fig, axes = plt.subplots(nrows=1, ncols=len(images))

for i in range(len(images)):
    axes[i].imshow(images[i])

img = image.Image(images[0])
img.set_lines()
axes[0].imshow(img.lines, cmap='gray')

plt.show()