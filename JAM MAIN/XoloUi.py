# Form implementation generated from reading ui file 'XoloUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_XoloUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.bg_1.setGeometry(QtCore.QRect(-110, -80, 1611, 821))
        self.bg_1.setText("")
        self.bg_1.setPixmap(QtGui.QPixmap("../JANVIXOLO/vecteezy_abstract-blue-circuit-digital-background_6736873.jpg"))
        self.bg_1.setScaledContents(True)
        self.bg_1.setObjectName("bg_1")
        self.bg_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_2.setGeometry(QtCore.QRect(630, 230, 111, 101))
        self.bg_2.setText("")
        self.bg_2.setPixmap(QtGui.QPixmap("../JANVIXOLO/Screenshot_20230423_000708_Microsoft 365 (Office) (2).png"))
        self.bg_2.setScaledContents(True)
        self.bg_2.setObjectName("bg_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(550, 400, 81, 31))
        self.pushButton_1.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(217, 215, 204);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 400, 81, 31))
        self.pushButton_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(217, 215, 204);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
