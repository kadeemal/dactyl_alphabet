import cv2
import hand_tracking
import recognize_alphabet
import time
import threading


class Alphabet:

    def __init__(self, width_cam=1280, height_cam=720):
        # camera settings initialization
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, width_cam)
        self.cap.set(4, height_cam)
        self.detector = hand_tracking.HandDetector()

    def clean_file(self):
        file = open('recognize_text.txt', 'w+')
        file.seek(0)
        file.close()

    def camera_thread(self):
        while True:
            success, img = self.cap.read()
            self.detector.find_hands(img)
            landmark_list = self.detector.find_position(img, draw=False)
            if len(landmark_list) != 0:
                file = open('recognize_text.txt', 'r')
                cv2.putText(img, file.read(), (50, 150), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 5)
                file.close()
            else:
                file = open('recognize_text.txt', 'w')
                file.close()
            cv2.imshow('Russian dactyl alphabet', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def capture(self):
        # a separate thread for displaying characters on the screen
        threading.Thread(target=self.camera_thread).start()
        self.clean_file()
        while True:
            success, img = self.cap.read()
            self.detector.find_hands(img)
            landmark_list = self.detector.find_position(img, draw=False)
            if len(landmark_list) != 0:
                letter = recognize_alphabet.alphabet(landmark_list)
                file = open('recognize_text.txt', 'a')
                file.write(letter)
                file.close()
                time.sleep(2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
    a = Alphabet()
    a.capture()
