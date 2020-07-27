import sys

from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        # In order to modify the font, we retrieve it,
        # change it, and set it back
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        widget.setPixmap(QPixmap('assets/example.jpg'))
        widget.setScaledContents(True)
        widget.setFixedSize(QSize(200, 100))

        checkbox = QCheckBox("A checkbox")
        checkbox.setCheckState(Qt.Checked)
        checkbox.setTristate(True)
        checkbox.stateChanged.connect(self.show_state)

        # self.setCentralWidget(checkbox)
        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
