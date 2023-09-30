import cv2
from simple_facerec import SimpleFacerec
import threading
import copy

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

# Flag to indicate whether recognition is currently being performed
recognizing = False

def recognize_faces(frame):
    global recognizing
    recognizing = True
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame_copy, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame_copy, (x1, y1), (x2, y2), (0, 0, 200), 2)
    recognizing = False

while True:
    ret, frame = cap.read()
    frame_copy = copy.copy(frame)  # Create a copy of the frame for drawing

    if not recognizing:
        # Run face recognition in a separate thread
        recognition_thread = threading.Thread(target=recognize_faces, args=(frame,))
        recognition_thread.start()

    cv2.imshow("Frame", frame_copy)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
