from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.current_date = date.today().strftime("%Y:%m")
        self.current_date = self.current_date.split(":")
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(650, 527)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lbms.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(47, 47, 70);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.label.setObjectName("label")
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setGeometry(QtCore.QRect(10, 50, 271, 30))
        self.name_line.setMinimumSize(QtCore.QSize(0, 40))
        self.name_line.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(65, 0, 0);\n"
"}\n"
"")
        self.name_line.setObjectName("name_line")
        self.surname_line = QtWidgets.QLineEdit(self.centralwidget)
        self.surname_line.setGeometry(QtCore.QRect(350, 50, 281, 30))
        self.surname_line.setMinimumSize(QtCore.QSize(0, 40))
        self.surname_line.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(65, 0, 0);\n"
"}\n"
"")
        self.surname_line.setObjectName("surname_line")
        self.birth_date = QtWidgets.QDateEdit(self.centralwidget)
        self.birth_date.setGeometry(QtCore.QRect(10, 140, 291, 61))
        self.birth_date.setStyleSheet("\n"
"QDateEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(65, 0, 0);\n"
"}\n"
"")
        self.birth_date.setDateTime(QtCore.QDateTime(QtCore.QDate(1992, 11, 7), QtCore.QTime(0, 0, 0)))
        self.birth_date.setObjectName("birth_date")
        self.live_line = QtWidgets.QLineEdit(self.centralwidget)
        self.live_line.setGeometry(QtCore.QRect(330, 240, 301, 30))
        self.live_line.setMinimumSize(QtCore.QSize(0, 40))
        self.live_line.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(65, 0, 0);\n"
"}\n"
"")
        self.live_line.setObjectName("live_line")
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(330, 300, 301, 30))
        self.address.setMinimumSize(QtCore.QSize(0, 40))
        self.address.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(65, 0, 0);\n"
"}\n"
"")
        self.address.setObjectName("phone_line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 400, 141, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(65, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 0, 103);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 10, 251, 31))
        self.label_6.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 271, 31))
        self.label_7.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 301, 41))
        self.label_8.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 290, 301, 41))
        self.label_9.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_9.setObjectName("label_9")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.pushButton.clicked.connect(self.clicked_button)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "EPIONE Set Up"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.label_6.setText(_translate("MainWindow", "Surname"))
        self.label_7.setText(_translate("MainWindow", "Birthday"))
        self.label_8.setText(_translate("MainWindow", "Where do you live ?"))
        self.label_9.setText(_translate("MainWindow", "Address ( City, Building):"))

    def clicked_button(self):
        year = self.current_date[0]
        month = self.current_date[1]
        my_list = ["", "", "", "", "", "", ""]
        my_list[0] = "Name:" + self.name_line.text()
        my_list[1] = "Surname:" + self.surname_line.text()
        my_list[2] = "Birthday:" + self.birth_date.text()
        my_list[3] = "Live:" + self.live_line.text()
        my_list[4] = "Address:" + self.address.text()
        my_list[5] = "Setup_date:" + month + "/" + year
        with open("data_of_user.txt", "w", encoding="utf-8") as data:
            for line in my_list:
                line = line + "\n"
                data.write(line)
        self.MainWindow.close()

def main_(app):
    SetUpWindow = QtWidgets.QMainWindow()
    SetUpWindow.setWindowTitle("Set Up EPIONE")
    ui = Ui_MainWindow()
    ui.setupUi(SetUpWindow) ## sorunn burda
    SetUpWindow.show()
    app.exec_()

