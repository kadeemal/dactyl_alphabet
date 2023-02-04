import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self, mode=False, max_hands=2, model_comp=1, det_conf=0.5, track_conf=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.model_comp = model_comp
        self.det_conf = det_conf
        self.track_conf = track_conf
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.model_comp, self.det_conf, self.track_conf)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, handNo=0, draw=False):
        landmark_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        return landmark_list


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector
    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        landmark_list = detector.find_position(img)
        cv2.imshow("HandTrack", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
