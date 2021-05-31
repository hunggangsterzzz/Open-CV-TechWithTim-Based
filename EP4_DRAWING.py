import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# 0,1,2... == the number of cams you use. 0 = 1 cam, 1 = 2 cams


while True:
    ret, frame = cap.read()  # return frame = image = numPi array
    # ret tells you whether capture is working
    width = int(cap.get(3))
    height = int(cap.get(4))
    # 3,4 are 2 of 17 properties of object capturing

    # Drawing line
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)

    # Drawing rect
    img = cv2.rectangle(img, (100, 100), (200, 300), (128, 128, 128), 5)

    # Drawing circle
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), 6)

    # Drawing text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Hung is me', (200, height - 10), font, 1, (0, 0, 0), 7, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        # ord() func returns an int representing the Unicode char
        print(ord('q'))
        break

cap.release()  # release the camera resource
cv2.destroyAllWindows()
