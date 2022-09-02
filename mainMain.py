
from PyQt5 import QtCore, QtGui, QtWidgets
import detection
import rehab
import handTracing

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, app):
        self.app = app
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(590, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 591, 571))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(57, 57, 85);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 50, 200, 121))
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"}")
        self.label.setObjectName("label")
        self.rehab_button = QtWidgets.QPushButton(self.frame)
        self.rehab_button.setGeometry(QtCore.QRect(140, 230, 301, 41))
        self.rehab_button.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(66, 0, 0);\n"
"    \n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.rehab_button.setObjectName("rehab_button")
        self.detection_button = QtWidgets.QPushButton(self.frame)
        self.detection_button.setGeometry(QtCore.QRect(140, 320, 301, 41))
        self.detection_button.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(66, 0, 0);\n"
"    \n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.detection_button.setObjectName("detection_button")
        self.hand_trace_button = QtWidgets.QPushButton(self.frame)
        self.hand_trace_button.setGeometry(QtCore.QRect(140, 400, 301, 41))
        self.hand_trace_button.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(66, 0, 0);\n"
"    \n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.hand_trace_button.setObjectName("hand_trace_button")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.rehab_button.clicked.connect(self.rehab)
        self.detection_button.clicked.connect(self.detection)
        self.hand_trace_button.clicked.connect(self.hand_trace)
        self.MainWindow.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "EPIONE"))
        self.label.setText(_translate("MainWindow", "WELCOME"))
        self.rehab_button.setText(_translate("MainWindow", "REHAB"))
        self.detection_button.setText(_translate("MainWindow", "DETECTION"))
        self.hand_trace_button.setText(_translate("MainWindow", "HAND TRACING"))

    def rehab(self):
        self.MainWindow.close()
        self.app.exec_()
        rehab.Rehab()

    def detection(self):
        self.MainWindow.close()
        detection.main_()

    def hand_trace(self):
        self.MainWindow.close()
        hands = handTracing.HandDetection()
        hands.start()
