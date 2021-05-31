import cv2
import random

img = cv2.imread('assets/cortez.jpg', -1)
img = cv2.resize(img, (800, 750))
print(img.shape)
# Coping and Pasting parts of images
tag = img[375:420, 350:700]  # [row, column]
img[100:145, 450:800] = tag
# the paste coordinates must have the same dimension as the copied one
print(f'tag_shape = {tag.shape}')
print(f'tag_0 = {tag.shape[0]}')
print(f'tag_1 = {tag.shape[1]}')
print(f'tag_2 = {tag.shape[2]}')

# Changing Pixel colors
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Images', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
