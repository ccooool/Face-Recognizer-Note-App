import numpy as np
import cv2
import os
import time



class Recognizer():
    def recognize(self):
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('trainer_data.yml')
        cascadePath = "face_data.xml"
        faceDetector = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX

        id = 0

        names = [None, "Carter", "Dad", None, "Carter", None, None, None, "Carter", "Carter"]
        # starting the video
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)
        
        # set minimum size of face to be recognized
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True: 
            ret,frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
            faces = faceDetector.detectMultiScale(gray,scaleFactor= 1.2, minNeighbors= 5,  minSize=(int(minW), int(minH)))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                id, confidence = face_recognizer.predict(gray[y: y+h, x:x+w])

                if confidence < 90:
                    str_id = names[id]
                else:
                    str_id = "unknown"
                confidence = " {0}%".format(round(100-confidence))

                cv2.putText(frame, str_id if str_id != "unknown" else str_id, (x+5, y-5), font, 1, (255,255,255), 2)
                cv2.putText(frame, str(confidence), (x+5, y+h-5), font, 1, (255,255,0), 2)



            cv2.imshow('camera', frame)
            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break

        cam.release()
        cv2.destroyAllWindows()

    def recognize_carter(self):
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('trainer_data.yml')
        cascadePath = "face_data.xml"
        faceDetector = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX

        id = 0

        names = [None, "Carter", "Dad", None, "Carter", None, None, None, "Carter", "Carter"]
        # starting the video
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)
        
        # set minimum size of face to be recognized
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        start = time.time()
        str_id = ""
        while True: 
            ret,frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
            faces = faceDetector.detectMultiScale(gray,scaleFactor= 1.2, minNeighbors= 5,  minSize=(int(minW), int(minH)))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                id, confidence = face_recognizer.predict(gray[y: y+h, x:x+w])

                if confidence < 90:
                    str_id = names[id]
                else:
                    str_id = "unknown"
                confidence = " {0}%".format(round(100-confidence))
                
                cv2.putText(frame, str_id if str_id != "unknown" else str_id, (x+5, y-5), font, 1, (255,255,255), 2)
                cv2.putText(frame, str(confidence), (x+5, y+h-5), font, 1, (255,255,0), 2)

            cv2.imshow('camera', frame)
            if str_id == "Carter":
                return True
            # stop users after 10 seconds of failing
            if (time.time() - start > 10):
                return False

            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break

        cam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    Recognizer().recognize()