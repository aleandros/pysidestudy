from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

app = QApplication(sys.argv)
window = QWidget()
window.show() # Windoes are hidden by default
app.exec_()

# All widgets without parents are windows
pushbutton_window = QPushButton()
pushbutton_window.show()
app.exec_()

# QMainWindow provides more stuff
main_window = QMainWindow()
main_window.show()
app.exec_()