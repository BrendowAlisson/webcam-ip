import cv2
import time

class Camera(object):
    def __init__(self):
        self.__video = cv2.VideoCapture(0)
        self.__font = cv2.FONT_HERSHEY_SIMPLEX

    def __del__(self):
        self.__video.release()

    def capture_frame(self):
        __, __frame = self.__video.read()
        __time = time.strftime('%H:%M:%S')
        __flipped = cv2.flip(__frame, 1)
        cv2.putText(__flipped, __time, (50,50), self.__font , 2,(0, 0, 255), 5)
        __, __jpeg = cv2.imencode('.jpg', __flipped)
        return __jpeg.tobytes()

