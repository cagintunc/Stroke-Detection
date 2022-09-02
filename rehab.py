import cv2
import poseEstimation
from datetime import datetime
import sys
import time
from PyQt5 import QtWidgets
import tkinter
import matplotlib
import mainGui
import pyttsx3 as p
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tensorflow as tf



class Rehab:

    def __init__(self, method_id=0):
        physical_device = tf.config.experimental.list_physical_devices("GPU")
        print(f"Number of GPUs are {len(physical_device)}")
        if len(physical_device) > 0:
            tf.config.experimental.set_memory_growth(physical_device[0], True)
        self.method_id = method_id
        self.pose = poseEstimation.PoseDetector()
        self.cap = cv2.VideoCapture(0)
        self.landmarks_1 = dict()
        self.landmarks_2 = dict()
        self.left_wrist = [0, 0]
        self.right_wrist = [0, 0]
        self.left_elbow = [0, 0]
        self.right_elbow = [0, 0]
        self.score = 0
        self.value_1 = 50
        self.value_2 = 200
        self.animation = [False, False]
        self.boolean = [[False, False], [False, False]]  # which step is finished ?
        self.engine = p.init()
        self.engine.setProperty("rate", 150)
        for i in range(34): # 33-th index for time.
            self.landmarks_1[i] = []
            self.landmarks_2[i] = []
        self.welcome_page()

    def welcome_page(self):
        """app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        MainWindow.setWindowTitle("EPIONE")
        ui = mainGui.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        time.sleep(1)
        # self.speak("welcome to the rehabilitation application!")
        time.sleep(1)
        MainWindow.close()"""
        self.begin()

    def begin(self):
        # self.speak("please do the following exercises which every step will be written on the screen.")
        accurate_position_landmarks_1 = {12, 14, 16, 11, 13, 15, 17, 18, 19, 20, 21, 22} # for arm motion
        accurate_position_landmarks_2 = {11, 12, 24, 23, 26, 25}
        accomplish = False
        indicator = 0 # how many step accomplished ?
        begining = datetime.now()
        while True:
            success, img = self.cap.read()
            img_new = self.pose.find_pose(img)
            positions = self.pose.get_positions(img)
            current_poses = self.pose.get_landmarks()
            current_poses = set(current_poses) # current posses are the currently seen landmarks id
            flag_1 = accurate_position_landmarks_1.issubset(current_poses)
            current = datetime.now()
            difference = (current - begining)
            if difference.total_seconds() <= 6:
                cv2.putText(img, "Get your position", (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                            1, (0, 0, 255))
            elif flag_1 and indicator < 15 and difference.total_seconds() > 6:
                cv2.putText(img, "True", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
                for i in accurate_position_landmarks_1:
                    self.landmarks_1[i].append([positions[i][0], positions[i][1]])
                    if i == 15:
                        self.right_wrist[0] = positions[i][0]
                        self.right_wrist[1] = positions[i][1]
                    elif i == 13:
                        self.right_elbow[0] = positions[i][0]
                        self.right_elbow[1] = positions[i][1]
                    elif i == 16:
                        self.left_wrist[0] = positions[i][0]
                        self.left_wrist[1] = positions[i][1]
                    elif i == 14:
                        self.left_elbow[0] = positions[i][0]
                        self.left_elbow[1] = positions[i][1]
                    elif i == 11: # for trying
                        self.arm_up_down(img, (positions[i][0], positions[i][1]), "right", self.value_1, self.value_2)
                    elif i == 12:
                        self.arm_up_down(img, (positions[i][0], positions[i][1]), "left", self.value_1, self.value_2)
                self.landmarks_1[33].append(difference.total_seconds())
                if self.boolean[0][0] and self.boolean[0][1]:
                    self.value_1 += 10
                    self.boolean[0] = [False, False]
                    indicator += 1
            elif flag_1 is False:
                cv2.putText(img, "Wrong Position!!", (50, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 7)
            elif self.boolean[0][0] is False and self.boolean[0][1] is False:
                self.boolean[0] = [True, True]
                self.score += 50
            cv2.imshow("EPIONE", img)
            if cv2.waitKey(20) and int(difference.total_seconds()) >= 30:
                cv2.destroyAllWindows()
                self.cap.release()
                self.plot_graph()
                break

    def arm_up_down(self, image, positions, flag, value_1, value_2):
        cv2.putText(image, "Take up your arm",
                    (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (90, 0, 255), 3)
        cv2.putText(image, "through purple line", (50, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (90, 0, 255), 3)
        if flag == "right":
            right_line_end = (positions[0] + value_1, positions[1] - value_2)
            cv2.line(img=image, pt1=positions,
                     pt2=right_line_end, color=(200, 0, 240), thickness=10)
            # print("Right:  ", self.function_1(positions, (positions[0]+80, positions[1]-250), 150))
            self.is_accomplished(positions, right_line_end, "right")
        elif flag == "left":
            left_line_end = (positions[0] - value_1, positions[1] - value_2)
            cv2.line(img=image, pt1=positions,
                     pt2=left_line_end, color=(200, 0, 240), thickness=10)
            # print("Left: ", self.function_1(positions, (positions[0]-80, positions[1]-250), 150))
            self.is_accomplished(positions, left_line_end, "left")

    def is_accomplished(self, positions, line_end, flag):
        if flag == "left":
            if len(self.left_elbow) >= 1 and len(self.left_wrist) >= 1:
                x_of_node_elbow = get_x_of(positions[0], self.left_elbow[0])
                x_of_node_wrist = get_x_of(positions[0], self.left_wrist[0])
                if abs(positions[0] - self.left_elbow[0]) > 0 and abs(positions[0] - self.left_wrist[0]) > 0:
                    # print("result: ", abs(self.function_1(positions, line_end, x_of_node) -
                    #                      self.function_1(positions, self.left_wrist, x_of_node)))
                    first_condition = abs(self.function_1(positions, line_end, x_of_node_elbow) -
                                          self.function_1(positions, self.left_elbow, x_of_node_elbow)) < 15
                    second_condition = abs(self.function_1(positions, line_end, x_of_node_wrist) -
                                           self.function_1(positions, self.left_wrist, x_of_node_wrist)) < 15
                    if first_condition and second_condition:
                        self.boolean[0][0] = True

        elif flag == "right":
            if len(self.right_elbow) >= 1 and len(self.right_wrist) >= 1:
                x_of_node_elbow = get_x_of(positions[0], self.right_elbow[0])
                x_of_node_wrist = get_x_of(positions[0], self.left_wrist[0])
                if abs(positions[0] - self.right_elbow[0]) > 0 and abs(positions[0] - self.right_wrist[0]) > 0:
                    # print("result: ", abs(self.function_1(positions, line_end, x_of_node) -
                    #                      self.function_1(positions, self.left_wrist, x_of_node)))
                    first_condition = abs(self.function_1(positions, line_end, x_of_node_elbow) -
                                          self.function_1(positions, self.right_elbow, x_of_node_elbow)) < 15
                    second_condition = abs(self.function_1(positions, line_end, x_of_node_wrist) -
                                           self.function_1(positions, self.right_wrist, x_of_node_wrist)) < 15
                    if first_condition and second_condition:
                        self.boolean[0][1] = True

    def function_1(self, point_1, point_2, x):
        slope = (point_2[1] - point_1[1])/(point_2[0] - point_1[0])
        y = (slope * (x - point_1[0])) + point_1[1]
        return y

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


def get_x_of(first_point, end_point):
    return (first_point + end_point) / 2


"""drive = GoogleDrive(GoogleAuth())
rehab = Rehab()
rehab.plot_graph()

gfile = drive.CreateFile({'parents': [{'id': '1g48AMfeQ4qtirJH4ZF4f5RofaPOlFRjM'}]})
gfile.SetContentFile("graph_x_axis.png")
gfile.Upload()

gfile = drive.CreateFile({'parents': [{'id': '1g48AMfeQ4qtirJH4ZF4f5RofaPOlFRjM'}]})
gfile.SetContentFile("graph_y_axis.png")
gfile.Upload()"""