import numpy as np
import cv2



class Detector():

    def test_camera(self):
        # begin capturing video, set frame
        cap = cv2.VideoCapture(0) #capture video
        cap.set(3,640) # width of frame
        cap.set(4,480) # height of frame

        while(True):

            ret, frame = cap.read()
            frame = cv2.flip(frame, 0)
            cv2.imshow('frame', frame) # display the video 
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            cv2.imshow('gray', gray)
            frame = cv2.flip(frame, 0)
            gray2 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            cv2.imshow('gray2', gray2)

            k = cv2.waitKey(30)
            
            if k == 27: # check for esc
                break

        cap.release()
        cv2.destroyAllWindows()


    # goal: open a camera, capture video, and draw a box around the face in the video
    def face_find(self):
        
        classifier = cv2.CascadeClassifier('/Users/carterlack/Desktop/projects/face_recognize/face_data.xml') # creates a classifier that recognises the face
        cap = cv2.VideoCapture(0) # starts video
        cap.set(3,640) # width of frame
        cap.set(4,480) # height of frame

        while(True): #continue repeating prosses
            ret, frame = cap.read() # capture the current picture from the video camera
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) 

            # detect face before showing the video
            faces = classifier.detectMultiScale(gray_frame, scaleFactor=1.2, minNeighbors=5, minSize=(20,20))
            # draw rectangle around all faces
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2) # determens where the rectangle around the face goes
                roi_gray = gray_frame[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

            # check for escape key pressed
            cv2.imshow('frame', frame)
            k = cv2.waitKey(30)
            if k == 27: 
                break

        cap.release()
        cv2.destroyAllWindows()
    
    def find_smile(self):
        classifier = cv2.CascadeClassifier('/Users/carterlack/Desktop/projects/face_recognize/face_data.xml')
        classifier2 = cv2.CascadeClassifier("/Users/carterlack/Desktop/projects/face_recognize/smile_data.xml") 

        cap = cv2.VideoCapture(0)
        cap.set(3,640) # width of frame
        cap.set(4,480) # height of frame
        while(True):
            ret, frame = cap.read() # capture the current picture from the video camera
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) 
            # detect face before showing the video
            faces = classifier.detectMultiScale(gray_frame, scaleFactor=1.3,  minNeighbors=5, minSize=(20,20))
            # first, find the face
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
                roi_gray = gray_frame[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                # then, find the smile
                smiles = classifier2.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=15,minSize=(20,20))
                for (xx,yy,ww,hh) in smiles:
                    cv2.rectangle(roi_color,(xx,yy), (xx+ww, yy+hh), (255,0,0), 2)    

                cv2.imshow('frame', frame)
            # cv2.imshow('frame', gray_frame)

            k = cv2.waitKey(30)
            if k == 27: # check for esc
                break

        cap.release()
        cv2.destroyAllWindows()
    
        
Detector().find_smile()