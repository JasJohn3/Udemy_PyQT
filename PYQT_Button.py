import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget, QLineEdit, QComboBox
from PyQt5.QtWidgets import QPushButton,QMessageBox
from PyQt5.QtCore import QSize
import Some_Loop as Some_Loop

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setMinimumSize(QSize(600, 400))
        self.setWindowTitle("PyQt button example")

#creates a text box for the window
        self.line_edit = QLineEdit(self)
        self.line_edit.resize(200,50)
        self.line_edit.move(200,100)
        self.line_edit.setPlaceholderText('Enter Your Name')

#creates a button that accepts the user input as an argument
        self.pybutton2 = QPushButton('OK', self)
        self.pybutton2.clicked.connect(self.clickMethod2)
        self.pybutton2.resize(200, 50)
        self.pybutton2.move(200, 150)

#creates an exit button for the program
        self.pybutton = QPushButton('Exit', self)
        self.pybutton.clicked.connect(self.clickMethod)
        self.pybutton.resize(200,50)
        self.pybutton.move(200, 200)

        # Create a Dropdown Menu Combo Box
        self.combo_box = QComboBox(self)
        self.combo_box.move(50, 100)

    def clickMethod(self):
        exit()

    def clickMethod2(self):
        total_training = self.line_edit.text()
        self.sender(Some_Loop(total_training))

def Some_Loop(total_training):
    for i in range(total_training):
        print("Hello "+ i)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )