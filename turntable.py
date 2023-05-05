import cv2
import time
cam=cv2.VideoCapture(0)
while not cam.isOpened():
    time.sleep(1)
while True:
    ret, frame= cam.read()
    if ret:
        cv2.imshow("table", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
cam.release()