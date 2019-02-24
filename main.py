import sys, random, subprocess

import strip as strip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from settings import *
from console import *


class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Установка заголовка окна
        self.setWindowTitle('Rust server configurator')
        self.ui.server_seed.insert(str(random.randint(1,50000)))
        # Действия при нажатие на кнопку Start
        self.ui.start_server_button.clicked.connect(self.start_button_clicked)
        # Действия при нажатии на кнопку Cancel
        self.ui.cancel_button.clicked.connect(self.close)
        # Действие при нажатии на кнопку New Window

    def start_button_clicked(self):
        # Метод запускается при нажатии на кнопку Start
        # Первичная строка запуска, которая не меняется
        #run_options = 'RustDedicated.exe -batchmode '
        # params Параметры запуска
        server_address = self.ui.listen_address.text()
        server_port = self.ui.server_port.text()
        server_world_size = self.ui.world_size
        #run_options = run_options + ' +server.port ' + server_port + ' +server.ip ' + server_address + " +server.worldsize "
        #running_server.show()
        command = "python sample.py"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=1)
        for line in iter(proc.stdout.readline, b''):
            print(line)
            #self.ui.result_box.append(str(line))
        proc.stdout.close()
        proc.wait()
        #out = out.strip(' (b\t\n\rNone)')

        #out = str(proc.stdout.readline())

        #running_server.console_output(data=(out))



class ServerWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Console()
        self.ui.setupUi(self)
        self.setWindowTitle('Rust server console')
        self.ui.exit_button.clicked.connect(self.close)
    def console_output(self,data):
        self.ui.rust_console.setText(data)


#def start_button_clicked(run_string):
#    myapp.ui.result_box.setText(str(run_string))


#RustDedicated.exe -batchmode +server.worldsize 5000 +server.hostname "My Server Name" +server.port 28015 +server.identity "my_server" +server.seed 4609391 -logFile "output.txt"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = SettingsWindow()
    running_server = ServerWindow()
    myapp.show()
    sys.exit(app.exec_())
