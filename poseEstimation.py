import cv2
import mediapipe as mp


class PoseDetector:

    def __init__(self, mode=False, up_body=False,
                 smooth=True, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.up_body = up_body
        self.smooth = smooth
        self.detection_con = detection_con
        self.track_con = track_con

        self.mp_draw = mp.solutions.drawing_utils
        self.my_pose = mp.solutions.pose
        self.pose = self.my_pose.Pose(static_image_mode=self.mode,
                                      smooth_landmarks=self.smooth,
                                      min_detection_confidence=self.detection_con,
                                      min_tracking_confidence=self.track_con)

    def find_pose(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.pose.process(img_rgb)
        if self.result.pose_landmarks:
            if draw:
                self.mp_draw.draw_landmarks(img, self.result.pose_landmarks,
                                            self.my_pose.POSE_CONNECTIONS)
        return img

    def get_positions(self, img, flag="full"):
        lm_list = []
        lm_dict = {}
        cx, cy = (0, 0)
        if self.result.pose_landmarks is not None:
            if flag == "detection":
                for id, lm in enumerate(self.result.pose_landmarks.landmark):
                    if id == 15 or id == 16:
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lm_list.append([id, cx, cy])
            else:
                for i in range(33):
                    lm_dict[i] = []
                for id, lm in enumerate(self.result.pose_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_dict[id] = [cx, cy]
                return lm_dict
        return lm_list

    def get_landmarks(self):
        current_landmarks = []
        if self.result.pose_landmarks is not None:
            for id, lm in enumerate(self.result.pose_landmarks.landmark):
                if lm.visibility >= 0.50:
                    current_landmarks.append(id)
        return current_landmarks

