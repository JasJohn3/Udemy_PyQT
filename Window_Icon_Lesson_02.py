from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

#create an pyqt object
app = QApplication(sys.argv)

#create the window
window = QWidget()
#customizing our window
#window title
window.setWindowTitle('PYQT Udemy Lessons')
#Window.setGeometry(first value equal too #window.move(100,100), second value equal too #window.resize(600,400))
window.setGeometry(100,100,600,400)

#creating a Qbutton
button = QPushButton('close', window)
button.resize(200,100)
button.move(200,150)

def ClickMethod():
    exit(0)
#display the window
window.show()
#execute the main loop
app.exec()