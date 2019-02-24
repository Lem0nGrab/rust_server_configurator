# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings-ui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(861, 480)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        Dialog.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 188, 61))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.world_size = QtWidgets.QComboBox(self.groupBox)
        self.world_size.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.world_size.setObjectName("world_size")
        self.world_size.addItem("")
        self.world_size.addItem("")
        self.world_size.addItem("")
        self.world_size.addItem("")
        self.world_size.addItem("")
        self.world_size.addItem("")
        self.world_size.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 188, 60))
        self.groupBox_2.setObjectName("groupBox_2")
        self.server_name = QtWidgets.QLineEdit(self.groupBox_2)
        self.server_name.setGeometry(QtCore.QRect(10, 20, 170, 22))
        self.server_name.setObjectName("server_name")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 170, 188, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.server_port = QtWidgets.QSpinBox(self.groupBox_3)
        self.server_port.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.server_port.setMinimum(1024)
        self.server_port.setMaximum(65535)
        self.server_port.setProperty("value", 28015)
        self.server_port.setObjectName("server_port")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(230, 31, 188, 60))
        self.groupBox_4.setObjectName("groupBox_4")
        self.server_seed = QtWidgets.QLineEdit(self.groupBox_4)
        self.server_seed.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.server_seed.setToolTip("")
        self.server_seed.setStatusTip("")
        self.server_seed.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.server_seed.setObjectName("server_seed")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(230, 100, 188, 60))
        self.groupBox_5.setObjectName("groupBox_5")
        self.listen_address = QtWidgets.QLineEdit(self.groupBox_5)
        self.listen_address.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.listen_address.setToolTip("")
        self.listen_address.setObjectName("listen_address")
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(230, 170, 188, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.saving_interval = QtWidgets.QSpinBox(self.groupBox_6)
        self.saving_interval.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.saving_interval.setMinimum(100)
        self.saving_interval.setMaximum(10000)
        self.saving_interval.setProperty("value", 300)
        self.saving_interval.setObjectName("saving_interval")
        self.groupBox_7 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 410, 340, 50))
        self.groupBox_7.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_7.setCheckable(True)
        self.groupBox_7.setChecked(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.server_log_path = QtWidgets.QLineEdit(self.groupBox_7)
        self.server_log_path.setGeometry(QtCore.QRect(10, 20, 311, 22))
        self.server_log_path.setObjectName("server_log_path")
        self.groupBox_8 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 240, 188, 61))
        self.groupBox_8.setObjectName("groupBox_8")
        self.server_max_players = QtWidgets.QSpinBox(self.groupBox_8)
        self.server_max_players.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.server_max_players.setMinimum(1)
        self.server_max_players.setMaximum(250)
        self.server_max_players.setProperty("value", 50)
        self.server_max_players.setObjectName("server_max_players")
        self.groupBox_9 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_9.setGeometry(QtCore.QRect(660, 31, 188, 60))
        self.groupBox_9.setObjectName("groupBox_9")
        self.rcon_passwd = QtWidgets.QLineEdit(self.groupBox_9)
        self.rcon_passwd.setGeometry(QtCore.QRect(10, 20, 170, 22))
        self.rcon_passwd.setText("")
        self.rcon_passwd.setObjectName("rcon_passwd")
        self.groupBox_10 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 310, 188, 61))
        self.groupBox_10.setObjectName("groupBox_10")
        self.server_ticket_rate = QtWidgets.QSpinBox(self.groupBox_10)
        self.server_ticket_rate.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.server_ticket_rate.setMinimum(1)
        self.server_ticket_rate.setMaximum(50)
        self.server_ticket_rate.setProperty("value", 10)
        self.server_ticket_rate.setObjectName("server_ticket_rate")
        self.groupBox_11 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_11.setGeometry(QtCore.QRect(460, 31, 188, 60))
        self.groupBox_11.setObjectName("groupBox_11")
        self.ip_addr = QtWidgets.QLineEdit(self.groupBox_11)
        self.ip_addr.setGeometry(QtCore.QRect(10, 20, 170, 22))
        self.ip_addr.setObjectName("ip_addr")
        self.start_server_button = QtWidgets.QPushButton(Dialog)
        self.start_server_button.setGeometry(QtCore.QRect(610, 430, 102, 32))
        self.start_server_button.setObjectName("start_server_button")
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(730, 430, 102, 32))
        self.cancel_button.setToolTip("")
        self.cancel_button.setObjectName("cancel_button")
        self.groupBox_12 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_12.setGeometry(QtCore.QRect(230, 240, 561, 131))
        self.groupBox_12.setObjectName("groupBox_12")
        self.result_box = QtWidgets.QTextBrowser(self.groupBox_12)
        self.result_box.setGeometry(QtCore.QRect(10, 20, 541, 101))
        self.result_box.setObjectName("result_box")
        self.new_window_button = QtWidgets.QPushButton(Dialog)
        self.new_window_button.setGeometry(QtCore.QRect(674, 150, 91, 31))
        self.new_window_button.setObjectName("new_window_button")

        self.retranslateUi(Dialog)
        self.result_box.textChanged.connect(self.result_box.reload)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Rust server configure"))
        self.groupBox.setToolTip(_translate("Dialog", "World size in square meteres. The bigger you make your world the larger RAM you need"))
        self.groupBox.setTitle(_translate("Dialog", "World size"))
        self.world_size.setItemText(0, _translate("Dialog", "1000"))
        self.world_size.setItemText(1, _translate("Dialog", "2000"))
        self.world_size.setItemText(2, _translate("Dialog", "3000"))
        self.world_size.setItemText(3, _translate("Dialog", "4000"))
        self.world_size.setItemText(4, _translate("Dialog", "5000"))
        self.world_size.setItemText(5, _translate("Dialog", "6000"))
        self.world_size.setItemText(6, _translate("Dialog", "7000"))
        self.groupBox_2.setTitle(_translate("Dialog", "Server name"))
        self.server_name.setText(_translate("Dialog", "Dedicated Rust Server"))
        self.groupBox_3.setTitle(_translate("Dialog", "Server port"))
        self.groupBox_4.setToolTip(_translate("Dialog", "Server\'s seed. Makes your world unique."))
        self.groupBox_4.setTitle(_translate("Dialog", "Server seed"))
        self.groupBox_5.setToolTip(_translate("Dialog", "IP address that server will listen on. 0.0.0.0 means all of availale IP addresses"))
        self.groupBox_5.setTitle(_translate("Dialog", "Listen address"))
        self.listen_address.setText(_translate("Dialog", "0.0.0.0"))
        self.groupBox_6.setToolTip(_translate("Dialog", "Interval in seconds showing how often your server will save current world state"))
        self.groupBox_6.setTitle(_translate("Dialog", "Saving interval (sec)"))
        self.groupBox_7.setToolTip(_translate("Dialog", "Path to your server log file"))
        self.groupBox_7.setTitle(_translate("Dialog", "Log file path"))
        self.server_log_path.setText(_translate("Dialog", ".\\server.log"))
        self.groupBox_8.setToolTip(_translate("Dialog", "Maximum number of player that can be connected to the server"))
        self.groupBox_8.setTitle(_translate("Dialog", "Server max players"))
        self.groupBox_9.setToolTip(_translate("Dialog", "If you are planing to connect to your server\'s console remotely provide a password for security reasons."))
        self.groupBox_9.setTitle(_translate("Dialog", "RCON Password"))
        self.groupBox_10.setToolTip(_translate("Dialog", "Server refresh rate. Not recomended to go above 30"))
        self.groupBox_10.setTitle(_translate("Dialog", "Server ticket rate"))
        self.groupBox_11.setToolTip(_translate("Dialog", "This is your RCON server\'s IP address. 0.0.0.0 means RCON will listen on each available IP address on your server"))
        self.groupBox_11.setTitle(_translate("Dialog", "RCON address"))
        self.ip_addr.setText(_translate("Dialog", "0.0.0.0"))
        self.start_server_button.setToolTip(_translate("Dialog", "Start the server with current settings"))
        self.start_server_button.setText(_translate("Dialog", "Start server"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.groupBox_12.setTitle(_translate("Dialog", "Output command"))
        self.new_window_button.setText(_translate("Dialog", "New Window"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())