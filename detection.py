import os
import time
from datetime import datetime
import tensorflow as tf
import pyttsx3 as p
import cv2
import numpy as np
import poseEstimation
import setUpGui
import arm_gui
import enchant
import sys
from PyQt5 import QtWidgets
from pydrive import drive
from tensorflow.keras.preprocessing import image
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import detect
import Video
import calendar


def pre_process(img):
    img = image.img_to_array(img)
    img_expanded = np.expand_dims(img, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_expanded)


def delete_blanks(_line):
    if _line.count(" ") >= 1:
        fresh_line = str()
        for char in _line:
            if char != " ":
                fresh_line = fresh_line + char
        _line = fresh_line
    return _line


def get_percentage_from_similarity(string_1, string_2):
    total_strength = max(len(string_2), len(string_2))
    print(total_strength)
    overlapping_strength = 0
    print(min(len(string_1), len(string_2)))
    for index in range(min(len(string_1), len(string_2))):
        if string_1[index] == string_2[index]:
            overlapping_strength += 1
    print(overlapping_strength, total_strength)
    return overlapping_strength / total_strength


def get_name_of_exp(dir_list):
    n = 0
    for element in dir_list:
        if element[3:] == "":
            dir_list[n] = 1
        else:
            dir_list[n] = int(element[3:])
        n += 1
    print(dir_list)
    return max(dir_list)


def get_month_name(month):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months[month]


def find_day(date):
    born = datetime.strptime(date, '%d %m %Y').weekday()
    return calendar.day_name[born]


def difference_time(h_1, m_1, h_2, m_2):
    t_1 = h_1 * 60 + m_1
    t_2 = h_2 * 60 + m_2
    if t_1 == t_2:
        print("The times are the same")
        return
    else:
        diff = t_2 - t_1
        print("diff: %d" % diff)
    hours = (int(diff / 60)) % 12
    print("hours: %d" % hours)
    mins = diff % 60
    print("mins: %d" % mins)
    return hours, mins


def get_result_2(result_2):
    if os.path.exists("experimental_results") is False:
        os.mkdir("experimental_results")
    file_name = "arm_weakness_test_result.txt"
    with open(file_name, "w", encoding="utf-8") as result_file:
        result_file.write("-----Right---------------------------------------------------------Left-----\n")
        result_file.write("X             Y  -------------------------------------------  X             Y\n")
        n = 0
        while n < max(len(result_2["left wrist"]), len(result_2["right wrist"])):
            my_string = "%spx          %spx  ------------------" \
                        "-------------------  %spx          %spx" % (result_2["left wrist"][n][0],
                                                                     result_2["left wrist"][n][1],
                                                                     result_2["right wrist"][n][0],
                                                                     result_2["right wrist"][n][1])
            result_file.write(my_string + "\n")
            n += 1
    gfile = drive.CreateFile({'parents': [{'id': '14ZL7iTYFaw_vdTU7v_rmt-Abq2K8FRyq'}]})
    gfile.SetContentFile(file_name)
    gfile.Upload()
    return 0


def get_result_3(result_3, my_info):
    out_of = 100.000
    points = {
        "Name": 1, "Surname": 1,
        "Born date month": 4 / 3, "Born date day": 4 / 3, "Born date year": 4 / 3,
        "Live": 4,
        "City": 5, "Building": 5,
        "SetUp date": 3,
        "How get here": 5,
        "First event after": 5, "Last event before": 5,
        "Time": 5,
        "Day of week": 5, "Day of month": 7,
        "What is the month": 15,
        "What is the year": 30
    }
    total = 0.000
    # Name
    name_surname = result_3["Name"].split(" ")
    if len(name_surname) > 1:
        if name_surname[0].lower() == my_info["Name"].lower():
            total += points["Name"]
        if name_surname[1].lower() == my_info["Surname"].lower():
            total += points["Surname"]
    else:
        if name_surname[0].lower() == my_info["Name"].lower() or name_surname[0].lower() == my_info["Surname"].lower():
            total += 1
    # Born
    born_date_user_give = result_3["Born"].rstrip().split("/")
    real_born_date = my_info["Birthday"].rstrip().split("/")
    index = 0
    while index < len(real_born_date):
        if real_born_date[index] == born_date_user_give[index]:
            total += 4 / 3
        index += 1
    print("After born date, total: ", total)
    # Live
    live_country_user_give = result_3["Live"].rstrip().lower()
    real_live_country = my_info["Live"].rstrip().lower()
    if real_live_country == live_country_user_give:
        total += points["Live"]
    print("After live, total: ", total)
    # City, Building
    city_building_user_give = result_3["City_building"].rstrip()
    print(city_building_user_give)
    if city_building_user_give.count(",") > 0:
        city_building_user_give = city_building_user_give.split(",")
        for i in range(2):
            city_building_user_give[i] = delete_blanks(city_building_user_give[i].lower())
    real_city_building = my_info["Address"].rstrip()
    if real_city_building.count(",") > 0:
        real_city_building = real_city_building.split(",")
        for i in range(2):
            real_city_building[i] = delete_blanks(real_city_building[i].lower())
    for i in range(2):
        percentage = get_percentage_from_similarity(real_city_building[i],
                                                    city_building_user_give[i])
        print("percent: " + str(percentage))
        if percentage >= 0.7:
            total += 5
    print("After city, building, total: ", total)
    # SetUp date
    date_setup = result_3["Setup_date"].split("/")
    setup_date_user_give = date_setup[0] + "/" + date_setup[2]
    if setup_date_user_give == my_info["Setup_date"]:
        total += points["SetUp date"]
    print("After setup date, total: ", total)
    # How to get here ?
    propositions = ["through", "by", "with", "via", "upon", "on", "along with"]
    transportation = ["car", "bike", "motorcycle", "ship", "train", "plane",
                      "airplane", "taxi", "ferry", "metro", "boat", "steamer", "bus",
                      "tram", "walk", "run", "lift", "vessel", "craft", "wheelchair",
                      "wheel chair", "stretcher", "helicopter", "copter", "chopper",
                      "ambulance", "foot", "subway", "underground railroad", "tube"]
    chars = result_3["How_get_here"].lower().split(" ")
    while "" in chars:
        chars.remove("")
    # investigation on chars
    temp_dictionary = {
        "transportation": 0,
        "proposition": 0
    }
    for char in chars:
        if char in transportation:
            temp_dictionary["transportation"] += 1
        elif char in propositions:
            temp_dictionary["proposition"] += 1
    if temp_dictionary["transportation"] >= 1:
        total += 5
    elif temp_dictionary["proposition"] >= 1:
        total += 2.5
    print("After how to get here, total: ", total)
    # TODO before the accident
    possible_words_1 = ["remember", "recall", "bethink", "bring to mind",
                        "think back on", "reminisce", "come to mind", "think",
                        "reproduce", "recapture", "recur", "bear in mind", "come",
                        "revoke", "revive", "flash on", "fetch up"]
    possible_words_2 = ["can't", "don't", "not", "doesn't", "couldn't",
                        "haven't", "hadn't"]
    possible_words_3 = ["forget", "unmindful", "lose sight of", "disremember",
                        "unaware", "misremember", "oblivious"]
    chars = result_3["Event_before"].lower().split(" ")
    unnecessary_chars = ["", " ", "a", "an", "the", "i"]
    for unwanted in unnecessary_chars:
        while unwanted in chars:
            chars.remove(unwanted)
    d = enchant.Dict("en_US")
    flag_1, flag_2, flag_3 = False, False, False
    founded_valid_words = 0
    for char in chars:
        if char in possible_words_1:
            flag_1 = True
        elif char in possible_words_2:
            flag_2 = True
        elif char in possible_words_3:
            flag_3 = True
        elif d.check(char):
            founded_valid_words += 1
    if (flag_1 and flag_2) or flag_3:
        pass
    elif founded_valid_words > 0:
        total += points["Last event before"]
    print("After before accident, total: ", total)
    # TODO after the accident
    proper_words_1 = ["trouble", "difficulty", "paralysis", "numbness",
                      "confusion", "headache", "problems", "bad", "mental fog",
                      "brain cloud", "brain fog", "mental cloud"]
    proper_words_2 = ["not", "can't", "cannot", "couldn't", "could not", "not able to",
                      "wasn't able to", "didn't"]
    proper_words_3 = ["speak", "speech", "walk", "move", "feel", "grab", "watch",
                      "see", "say", "tell", "explain", "describe", "do", "make",
                      "hear", "stand", "walk", "talk"]
    chars = result_3["Event_after"].lower().split(" ")
    number_of_others = 0
    check_1, check_2, check_3 = False, False, False
    for char in chars:
        if char in proper_words_1:
            check_1 = True
        elif char in proper_words_2:
            check_2 = True
        elif char in proper_words_3:
            check_3 = True
        elif d.check(char):
            number_of_others += 1
    if (check_1 and check_3) or (check_2 and check_3):
        total += points["First event after"]
    else:
        if number_of_others >= 3:  # SVT from English grammar
            out_of -= points["First event after"]
    print("After after accident, total: ", total)

    # TODO Time
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_real_time = current_time.split(":")
    chars = result_3["Time"].split("/")
    hours_dictionary = {"real": [int(current_real_time[0]), int(current_real_time[1])]}
    if len(chars) == 1:
        hours_dictionary["given"] = [int(chars[0]), 0]
    else:
        hours_dictionary["given"] = [int(chars[0]), int(chars[1])]
    # TODO Continue from here
    hours_mins = difference_time(hours_dictionary["real"][0], hours_dictionary["real"][1],
                                 hours_dictionary["given"][0], hours_dictionary["given"][1])
    half_hours = (2 * hours_mins[0]) + (hours_mins[1] / 30)
    total -= half_hours
    print("After time, total: ", total)

    # TODO Day of the week
    date_of_today = datetime.now().strftime("%d %m %Y")
    if result_3["Day_of_week"].lower() == find_day(date_of_today).lower():
        total += points["Day of week"]
    print("Day of the week", total)

    # TODO Day of month
    day_month_year = date_of_today.split(" ")
    print("day_month_year", day_month_year)
    if int(day_month_year[0]) == int(result_3["Day_of_month"]):
        total += points["Day of month"]
    print("Day of the month", total)

    # TODO Month name
    if get_month_name(int(day_month_year[1])).lower() == result_3["Month"].lower():
        total += points["What is the month"]
    print("After month: ", total)

    # TODO Year
    if day_month_year[2] == result_3["Year"]:
        total += points["What is the year"]
    print("After year: ", total)

    print("Score: " + str(total))
    return total / out_of


def evaluate_scores(result_1, result_2, result_3, info):
    try:
        _result = result_1["stroke"] / (result_1["normal"] + result_1["stroke"]) \
                  + get_result_2(result_2) \
                  + get_result_3(result_3, info)
        return _result
    except ZeroDivisionError:
        print("There is no face found in the test;"
              "\nin order to detect any stroke indications, your face is needed in video")


def arm_indication():
    accurate_position_landmarks = {12, 14, 16, 11, 13, 15, 24, 23}
    pose = poseEstimation.PoseDetector()
    cap = cv2.VideoCapture(0)
    positions_of_wrist = {
        "left wrist": [],
        "right wrist": [],
        "time": []
    }
    begining = datetime.now()
    while True:
        success, img = cap.read()
        img_new = pose.find_pose(img)
        positions = pose.get_positions(img, "detection")
        current_poses = pose.get_landmarks()
        current_poses = set(current_poses)
        flag = accurate_position_landmarks.issubset(current_poses)
        # flag = True
        current = datetime.now()
        difference = (current - begining)
        if flag:
            positions_of_wrist["left wrist"].append((positions[0][1], positions[0][2]))
            positions_of_wrist["right wrist"].append((positions[1][1], positions[1][2]))
            cv2.putText(img, "Right", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
        else:
            cv2.putText(img, "PROBLEM!", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 4)
        positions_of_wrist["time"].append(difference.total_seconds() * 10)
        cv2.imshow("EPIONE", img)
        if cv2.waitKey(20) & int(difference.total_seconds()) >= 30:
            cv2.destroyAllWindows()
            cap.release()
            break
    return positions_of_wrist


def face_dropping():
    capture_1 = cv2.VideoCapture(0)
    video = Video.Video()
    dim = video.get_dimensions(capture_1, "720p")
    video_type_cv2 = video.get_video_type()
    out = cv2.VideoWriter(video.file_name + ".avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"),
                          video.frames_per_second, dim)
    begining = datetime.now()
    while True:
        ret, frame = capture_1.read()
        out.write(frame)
        cv2.imshow("Frame", frame)
        current = datetime.now()
        difference = (current - begining).total_seconds()
        if cv2.waitKey(20) and int(difference) >= 3:
            break
    capture_1.release()
    out.release()
    cv2.destroyAllWindows()
    os.chdir("C:\\Users\\cagin\\OneDrive\\Masaüstü\\Full Documents\\projects\\hackatone")
    # run detect.py
    # best.pt dosyası YOKK
    detect.run(weights="model\\best.pt", imgsz=640, conf_thres=0.80, save_txt=True,
               source=f"{video.file_name}" + ".avi")
    path = "C:\\Users\\cagin\\OneDrive\\Masaüstü\\Full Documents\\projects\\hackatone\\runs\\detect"
    list_of_dir = os.listdir(path)
    name_of_txt = ""
    number = get_name_of_exp(list_of_dir)
    name_of_exp = ""
    if number != 1:
        name_of_exp = "exp" + str(number)
    else:
        name_of_exp = "exp"
    print("Directory name: " + name_of_exp)
    path += "\\" + name_of_exp + "\\" + "labels"
    labels_list = os.listdir(path)
    results = {"normal": 0,
               "stroke": 0}
    for label in labels_list:
        my_file = open(path + "\\" + label, "r", encoding="utf-8")
        my_lines = my_file.readline().split(" ")
        if my_lines[0] == "0":
            results["normal"] += 1
        elif my_lines[0] == "1":
            results["stroke"] += 1
        my_file.close()
    return results



def main_():
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("EPIONE")
    print("gt: ", os.getcwd())
    if os.path.exists("data_of_user.txt") is False:
        app = QtWidgets.QApplication(sys.argv)
        st = setUpGui
        st.main(app)
        app.exec_()

    else:
        results_1 = face_dropping()
        print(results_1)
        # TODO: Arm detection
        armGui = QtWidgets.QMainWindow()
        armGui.setWindowTitle("Pose")
        ui_2 = arm_gui.Ui_MainWindow()
        ui_2.setupUi(MainWindow)
        MainWindow.show()
        time.sleep(4)
        ui_2.close()
        ### Result 2 ###
        results_2 = arm_indication()
        print("burda 1") ################################################################
        x_left, x_right, y_left, y_right = [], [], [], []
        for coordinate in results_2["left wrist"]:
            x_left.append(coordinate[0])
            y_left.append(coordinate[1])
        for coordinate in results_2["right wrist"]:
            x_right.append(coordinate[0])
            y_right.append(coordinate[1])
        # result_2 must be evaluated!
        print("burda 2") ################################################################
        if len(x_left) == 0 or len(x_right) == 0 or len(y_left) == 0 or len(y_right) == 0:
            print("You must show your upper body to the program!!")
            sys.exit(0)

        my_information = {}
        with open("data_of_user.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                line = line.rstrip().split(":")
                if len(line) > 1:
                    my_information[line[0]] = line[1]
        # TODO Amnesia Test
        # amnesia test 1
        print("burdaaaa") ################################################################
        os.system('cmd /c "python amnesia.py"')

        results_3 = {}
        if os.path.exists("last_amnesia_result.txt"):
            with open("last_amnesia_result.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    line_as_list = line.rstrip().split(":")
                    if len(line_as_list) > 1:
                        results_3[line_as_list[0]] = line_as_list[1]
            #############################
            gfile_3 = drive.CreateFile({'parents': [{'id': '1_AVLJN1s-dSpF0tLhpIsKgjsmyeqiRhP'}]})
            gfile_3.SetContentFile("last_amnesia_result.txt")
            gfile_3.Upload()
        else:
            print("There is a problem.\nRestart your application.")

        result = evaluate_scores(results_1, results_2, results_3, my_information)
        print("Total result: ", result)




