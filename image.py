from matplotlib import pyplot as plt
from time import time
import numpy as np
import cv2

# A function that vertically flips an image
# Note:
# Put # on lines 17-20 and remove that of line 21 to see the difference
# in the execution times for the loop-version and vectorized-version.
def flip(image):
    # image dimensions
    h = image.shape[0]
    w = image.shape[1]
    # pre-allocate array for the flipped image
    flipped_image = np.zeros((h, w, 3)).astype(np.uint8)
    # main loop
    #for id_c in range(3):
    #    for id_h in range(h):
    #        for id_w in range(w):
    #            flipped_image[id_h, id_w, id_c] = image[id_h, w-id_w-1, id_c]
    flipped_image = image[:, ::-1, :]
    return flipped_image

# start clock
start = time()

# set-up figure
fig = plt.figure(1, figsize=(9, 6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# read and plot image
image = cv2.imread(r"C:\Users\Kenneth Raposas\Desktop\codes\python_codes\141\sipser.png", 1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
ax1.imshow(image)
ax1.set_title("Original Image", fontsize=14)
ax1.axis("off")

# flip and plot resulting image
flipped_image = flip(image)
ax2.imshow(flipped_image)
ax2.set_title("Flipped Image", fontsize=14)
ax2.axis("off")

# save figure
plt.savefig(r"C:\Users\Kenneth Raposas\Desktop\codes\python_codes\141\flipped_image.pdf")

# stop time
end = time()
print("Elapsed time: {} seconds".format(end - start))
plt.show()