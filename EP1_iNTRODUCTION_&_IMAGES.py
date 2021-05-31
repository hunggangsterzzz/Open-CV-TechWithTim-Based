import cv2

img = cv2.imread('assets/cortez.jpg', 1)

# RESIZE THE IMAGE
img = cv2.resize(img, (400, 400))  # Resize and rotate
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # Alternative
# The values of 'fx' and 'fy' = fracs or floats ==> multiply the pixel number by

# ROTATE THE IMAGE
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('new_img.jpg', img)  # save the recent image to a new one

# blue-green-red

# -1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# 0, cv2. IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

cv2.imshow('Image', img)  # display the image
cv2.waitKey(0)  # wait up to infinite amount of time until mouse-clicking on the screen
cv2.destroyAllWindows()
