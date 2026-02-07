import numpy as np
import cv2 as cv
from pathlib import Path


def get_image():
    Class = 'please'
    Path('DATASET/'+Class).mkdir(parents=True, exist_ok=True)
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    i = 0
    count=0
    print(" Press 'A' to start Capture")
    while True:
       
        ret, frame = cap.read()
        if count==1:
            print("Capturing")
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # frame = cv.flip(frame,1)
        if count!=0:
            i+= 1
            if i % 5==0:
                cv.imwrite('DATASET/'+Class+'/'+str(i)+'.png',frame)
      
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('a') : # or i > 500:
            count=1
        if cv.waitKey(1) == ord('q') or i > 500:
            break
  
    cap.release()
    cv.destroyAllWindows()
if __name__ == "__main__":
   get_image()
  
