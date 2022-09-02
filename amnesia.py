from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1202, 863)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindow.sizePolicy().hasHeightForWidth())
        self.MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lbms.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(58, 58, 86);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(670, 30, 491, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.describe_last_event = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.describe_last_event.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"\n"
"}")
        self.describe_last_event.setObjectName("describe_last_event")
        self.verticalLayout.addWidget(self.describe_last_event)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.time = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.time.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.time.setObjectName("time")
        self.verticalLayout.addWidget(self.time)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.day_of_week = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.day_of_week.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.day_of_week.setObjectName("day_of_week")
        self.verticalLayout.addWidget(self.day_of_week)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.day_of_month = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.day_of_month.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(89, 0, 0);\n"
"}\n"
"")
        self.day_of_month.setObjectName("day_of_month")
        self.verticalLayout.addWidget(self.day_of_month)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.month = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.month.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.month.setObjectName("month")
        self.verticalLayout.addWidget(self.month)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.year = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.year.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.year.setObjectName("year")
        self.verticalLayout.addWidget(self.year)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(800, 690, 251, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    \n"
"    \n"
"    background-color: rgb(84, 0, 0);\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(0, 0, 86);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 40, 591, 731))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.name.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.name.setObjectName("name")
        self.verticalLayout_3.addWidget(self.name)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.born_date = QtWidgets.QDateEdit(self.verticalLayoutWidget_3)
        self.born_date.setStyleSheet("QDateEdit { \n"
"    color: white;\n"
"    background-color: rgb(89, 0, 0);\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.born_date.setObjectName("born_date")
        self.verticalLayout_3.addWidget(self.born_date)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.live = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.live.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.live.setObjectName("live")
        self.verticalLayout_3.addWidget(self.live)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.city_building = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.city_building.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.city_building.setObjectName("city_building")
        self.verticalLayout_3.addWidget(self.city_building)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.app_setup_date = QtWidgets.QDateEdit(self.verticalLayoutWidget_3) ###################
        self.app_setup_date.setStyleSheet("QDateEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.app_setup_date.setObjectName("app_setup_date")
        self.verticalLayout_3.addWidget(self.app_setup_date)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.how_get_here = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.how_get_here.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.how_get_here.setObjectName("how_get_here")
        self.verticalLayout_3.addWidget(self.how_get_here)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("QLabel{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: white;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.first_event_after = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.first_event_after.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(89, 0, 0);\n"
"}")
        self.first_event_after.setObjectName("first_event_after")
        self.verticalLayout_3.addWidget(self.first_event_after)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.pushButton.clicked.connect(self.clicked_button)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "EPIONE"))
        self.label.setText(_translate("MainWindow", "Can you describe the last event you\n"
                                                    "can recall before the accident?"))
        self.label_2.setText(_translate("MainWindow", "What time is it now ?"))
        self.label_3.setText(_translate("MainWindow", "What day of the week is it ?"))
        self.label_4.setText(_translate("MainWindow", "What day of the month is it ?"))
        self.label_5.setText(_translate("MainWindow", "What is the month ?"))
        self.label_6.setText(_translate("MainWindow", "What is the year ?"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label_7.setText(_translate("MainWindow", "What is your name ?"))
        self.label_8.setText(_translate("MainWindow", "When were you born ?"))
        self.label_9.setText(_translate("MainWindow", "Where do you live ?"))
        self.label_10.setText(_translate("MainWindow", "Where are you now ? (City, Building)"))
        self.label_11.setText(_translate("MainWindow", "When were you setted up this app ?"))
        self.label_12.setText(_translate("MainWindow", "How did you get here ?"))
        self.label_13.setText(_translate("MainWindow", "What is the first event you can remember\n"
                                                       "after the injury ?"))

    def clicked_button(self):
        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
        file_name = "last_amnesia_result.txt"
        list_tk = []
        time_update = self.time.text().split(":")

        list_tk.append("Name:" + self.name.text())
        list_tk.append("Born:" + self.born_date.text())
        list_tk.append("Live:" + self.live.text())
        list_tk.append("City_building:" + self.city_building.text())
        list_tk.append("Setup_date:" + self.app_setup_date.text())
        list_tk.append("How_get_here:" + self.how_get_here.text())
        list_tk.append("Event_after:" + self.first_event_after.text())
        list_tk.append("Event_before:" + self.describe_last_event.text())
        list_tk.append("Time:" + time_update[0] + "/" + time_update[1])
        list_tk.append("Day_of_week:" + self.day_of_week.text())
        list_tk.append("Month:" + self.month.text())
        list_tk.append("Day_of_month:" + self.day_of_month.text())
        list_tk.append("Year:" + self.year.text())
        with open(file_name, "w", encoding="utf-8") as file:
            for line in list_tk:
                file.write(line + "\n")
        """gfile = drive.CreateFile({'parents': [{'id': '1i8IFot2UFFXSUtVBqeWqJ4mYKgvXqX4B'}]})
        gfile.SetContentFile(file_name)
        gfile.Upload()"""
        self.MainWindow.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
