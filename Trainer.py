"""
Strategy / Design:

We need something to take a bunch of photos very quickly, so we have a training data set.

1. Activate the Camera
    1.5. Ask for user_id, which is a number
2. Take a picture of your face
3. save the picture to a folder called "dataset/User.<user_id>" as a jpg
4. repeat steps 2-3 100 times
5. turn off camera.

"""

import numpy as np
import cv2
import os
from PIL import Image

class Trainer():
    def capture_data(self):
        cap = cv2.VideoCapture(0)
        cap.set(3,640) # width of frame
        cap.set(4,480) # height of frame

        user_id = input('type a unique number (1-10) as your id and hit enter')
        
        #make a classifier that detects faces (do "classifier = .....")
        classifier_ladeda = cv2.CascadeClassifier('/Users/carterlack/Desktop/projects/face_recognize/face_data.xml')
        
        # variable to hold count of pictures taken
        count = 0

        while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # use the classifier to detect faces
            faces = classifier_ladeda.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.imwrite("data_set/image_" + str(user_id) +"_" + str(count) + ".jpg", gray[y:y+h, x:x+w])
                count = count + 1
                cv2.imshow('image', frame)
            k = cv2.waitKey(100) & 0xff
            if k == 27:
                break
            elif count >= 70:
                break
        cap.release()
        cv2.destroyAllWindows()
        


    def get_images(self, path, detector):
        all_paths = []
        for image in os.listdir('data_set'):
            full_path = os.path.join(path, image)
            all_paths.append(full_path)
        # print(all_paths)
        faceThings = []
        ids = []
        for image_path in all_paths:
            opened_image = Image.open(image_path).convert('L')
            img_np = np.array(opened_image, 'uint8')
            id = image_path.split('_')[2]
            int_id = int(id)

            faces = detector.detectMultiScale(img_np)
            for (x, w, y, h) in faces:
                faceThings.append(img_np[y:y+h, x:x+w])
                ids.append(int_id)
                
        return faceThings, ids

            
    def train(self):
        path = 'data_set'
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        detector = cv2.CascadeClassifier('/Users/carterlack/Desktop/projects/face_recognize/face_data.xml')
        faceThings, ids = self.get_images(path, detector)
        recognizer.train(faceThings, np.array(ids))
        recognizer.write('trainer_data.yml')
        print("\n  [INFO] {0} faces trained".format(len(np.unique(ids))))




    # go through all images, and convert it into grayscale, then change them into numbers, then try to train on the array of numbers._
Trainer().capture_data()
Trainer().train()
# 

        
