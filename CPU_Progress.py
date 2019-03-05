import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
import system_info
import CPU_USAGE

#This is how to convert a UI file into a python file.  Must be performed in the directory of the UI file.
#call python -m PyQt5.uic.pyuic -x filename.ui -o filename.py
class MainUIWindow(QMainWindow, CPU_USAGE.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainUIWindow, self).__init__(parent)
        self.setupUi(self)
        self.thread_class = Thread_Class()
        self.thread_class.start()

        self.update_progressBar()

    def update_progressBar(self):
        val = system_info.getCPU()
        self.progressBar.setValue(val)

class Thread_Class(QtCore.QThread):
    def __init__(self, parent = None):
        super(Thread_Class,self).__init__(parent)
        self.setupUi(self)
    def run(self):
        while 1:
            val = system_info.getCPU()

if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)
    app = MainUIWindow()
    app.show()
    sys.exit(app.exec_())