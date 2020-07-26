import sys

from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # Always do this when subclassing Qt classes
        self.setWindowTitle("My Application")
        button = QPushButton("Press me!")
        button.setMaximumSize(QSize(200, 100))
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
