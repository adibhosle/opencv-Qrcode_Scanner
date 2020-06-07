import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread("code.png")
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

with open('Data') as f:
    lists = f.read().splitlines()
    # print(lists)

# print(decode(img))
while True:
    ret, img = cap.read()
    for code in decode(img):
        mydata = code.data.decode('utf-8')
        # print(code.data.decode('utf-8'))
        if mydata in lists:
            data = 'Authorized'
            mcolor = (0, 255, 0)
        else:
            data = 'Un-Authorized'
            mcolor = (0, 0, 255)

        print(data)
        pts = np.array([code.polygon], np.int32)
        # pt = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, mcolor, 2)
        pt = code.rect
        cv2.putText(img, data, (pt[0], pt[1]), cv2.FONT_HERSHEY_COMPLEX, 0.9, mcolor, 1)
    cv2.imshow("Scanner", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.waitKey(0)
