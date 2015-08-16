import matplotlib.pyplot as plt
import image
import numpy as np
import random


from skimage import io

images = io.ImageCollection('./photo/*')

fig, axes = plt.subplots(nrows=1, ncols=len(images))

for i in range(len(images)):
    axes[i].imshow(images[i])

img = image.Image(images[2])
# img.set_lines()
# axes[0].imshow(img.lines, cmap='gray')
# print img.get_rectangles()
# print map(img.polygon_area, img.get_rectangles())
for l in sorted(img.get_rectangles(), key=lambda x: img.polygon_area(x)):
    print l
print sorted(map(img.polygon_area, img.get_rectangles()))


from skimage.draw import polygon

pic = np.zeros(images[0].shape, dtype=np.uint8)

for y_coords, x_coords in img.get_poly_coords():
    rr, cc = polygon(np.asarray(y_coords), np.asarray(x_coords), pic.shape)
    rand = random.randrange(50, 256)
    pic[rr, cc] = rand

#
# print img.get_rectangles()
# print img.get_poly_coords()
# print np.amax(pic)

axes[0].imshow(images[0])
axes[1].imshow(pic)
plt.show()