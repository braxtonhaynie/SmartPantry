from picamera2 import Picamera2, Preview
import cv2
import time
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
time.sleep(2)
picam2.configure(camera_config)
time.sleep(2)
picam2.start_preview(Preview.QTGL)
time.sleep(2)
picam2.start()
while True:
    if cv2.waitKey(1):
        break
time.sleep(2)
picam2.capture_file("test.jpg")