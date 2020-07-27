import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My Application")
        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)

    # In Qt terms, this callbacks are called "slots"
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me")
        self.button.setEnabled(False)
        self.setWindowTitle("My oneshot app")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
