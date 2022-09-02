import sys
import mainMain
from PyQt5 import QtCore, QtGui, QtWidgets

def app():
    app = QtWidgets.QApplication(sys.argv)
    SetUpWindow = QtWidgets.QMainWindow()
    ui = mainMain.Ui_MainWindow()
    ui.setupUi(SetUpWindow, app)
    app.exec_()

app()


