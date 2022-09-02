import cv2
import mediapipe as mp

class HandDetection():

    def __init__(self, mode=False, maxHands=2,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.cap = cv2.VideoCapture(0)
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.handPositions = {
            "right": [],
            "left": []
        }

    def find_hands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        if self.result.multi_hand_landmarks:
            for handLMS in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLMS, self.mpHands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, handNO=0, draw=True):
        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNO]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * w)
                lmList.append([id, cx, cy])
        return lmList

    def start(self):
        while True:
            success, img = self.cap.read()
            img = self.find_hands(img)
            cv2.imshow("image", img)
            if cv2.waitKey(20) and 0xFF == "q":
                cv2.destroyAllWindows()
                self.cap.release()
                break

