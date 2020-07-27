import sys

from PySide2.QtWidgets import QApplication, QSpinBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Line edit")

        widget = QSpinBox()  # QDoubleSpinBox is for floats
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # or: widget.setRange(-10, 3)
        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.valueChanged[str].connect(self.value_changed_str)

        self.setCentralWidget(widget)

    @staticmethod
    def value_changed(i):
        print(i)

    @staticmethod
    def value_changed_str(s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
