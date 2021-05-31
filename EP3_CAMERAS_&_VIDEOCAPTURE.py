import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# 0,1,2... == the number of cams you use. 0 = 1 cam, 1 = 2 cams


while True:
    ret, frame = cap.read()  # return frame = image = numPi array
    # ret tells you whether capture is working

    print(frame)
    width = int(cap.get(3))
    height = int(cap.get(4))
    # 3,4 are 2 of 17 properties of object capturing

    image = np.zeros(frame.shape, np.uint8)  # unsigned integer 8-bit (0-255)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height // 2, :width // 2] = smaller_frame  # top-left
    # image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height // 2:, :width // 2] = smaller_frame  # bottom-left
    image[:height // 2, width // 2:] = smaller_frame  # top-right
    image[height // 2:, width // 2:] = smaller_frame  # bottom-right
    # image[height // 2:, width // 2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        # ord() func returns an int representing the Unicode char
        print(ord('q'))
        break

cap.release()  # release the camera resource
cv2.destroyAllWindows()
