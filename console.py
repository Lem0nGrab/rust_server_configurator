# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'console-ui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Console(object):
    def setupUi(self, Console):
        Console.setObjectName("Console")
        Console.resize(817, 532)
        self.groupBox_12 = QtWidgets.QGroupBox(Console)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 30, 661, 401))
        self.groupBox_12.setObjectName("groupBox_12")
        self.rust_console = QtWidgets.QTextBrowser(self.groupBox_12)
        self.rust_console.setGeometry(QtCore.QRect(10, 20, 640, 370))
        self.rust_console.setObjectName("rust_console")
        self.exit_button = QtWidgets.QPushButton(Console)
        self.exit_button.setGeometry(QtCore.QRect(710, 480, 91, 31))
        self.exit_button.setObjectName("exit_button")
        self.pushButton_2 = QtWidgets.QPushButton(Console)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 440, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Console)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 440, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Console)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 480, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox = QtWidgets.QGroupBox(Console)
        self.groupBox.setGeometry(QtCore.QRect(680, 30, 120, 401))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 91, 20))
        self.checkBox.setObjectName("checkBox")
        self.groupBox_2 = QtWidgets.QGroupBox(Console)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 440, 161, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(74, 50, 81, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Console)
        QtCore.QMetaObject.connectSlotsByName(Console)

    def retranslateUi(self, Console):
        _translate = QtCore.QCoreApplication.translate
        Console.setWindowTitle(_translate("Console", "Form"))
        self.groupBox_12.setTitle(_translate("Console", "Output command"))
        self.exit_button.setText(_translate("Console", "Exit"))
        self.pushButton_2.setText(_translate("Console", "Stop server"))
        self.pushButton_3.setText(_translate("Console", "Restart server"))
        self.pushButton_4.setText(_translate("Console", "Kick all"))
        self.groupBox.setTitle(_translate("Console", "GroupBox"))
        self.checkBox.setText(_translate("Console", "Radiation"))
        self.groupBox_2.setTitle(_translate("Console", "Admins"))
        self.pushButton_5.setText(_translate("Console", "Make admin"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Console = QtWidgets.QWidget()
    ui = Ui_Console()
    ui.setupUi(Console)
    Console.show()
    sys.exit(app.exec_())
