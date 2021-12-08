
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

face_data = []
dataset_path = "./dataset/"
file_name = input("Enter the name of the person : ")

while True:
    ret, frame = cap.read()

    if ret == False:
        continue

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 5)
    # if len(faces) == 0:
    #     continue
    faces = sorted(faces, key=lambda f: f[2]*f[3])

    for (x, y, w, h) in faces[-1:]:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        offset = 10
        face_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
        face_section = cv2.resize(face_section, (100, 100))
        face_data.append(face_section)
        print(len(face_section))

    cv2.imshow("Frame", frame)

    keypressed = cv2.waitKey(1) & 0xFF
    if keypressed == ord('q'):
        break

image = cv2.imread('test.jpeg')


face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0], -1))
print(face_data.shape)

np.save(dataset_path+file_name+'.npy', face_data)
print("Data saved!!")

cap.release()
cap.destroyAllWindows()
