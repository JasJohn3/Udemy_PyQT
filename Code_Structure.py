
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QWidget

import sys

app = QApplication(sys.argv)
#creating a window
window = QWidget()
#displaying the window
window.show()
#execute window loop
app.exec()
