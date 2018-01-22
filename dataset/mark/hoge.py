# coding: utf-8

import cv2

def captureImage(filename):
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    cv2.imwrite(filename,frame)

    cap.release()

if __name__ == '__main__':
	captureImage("tmp.jpg")
	cv2.destroyAllWindows()
