import sys
from PySide2.QtWidgets import QMainWindow, QComboBox, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combo box")
        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertAtTop)
        widget.setMaxCount(10)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()