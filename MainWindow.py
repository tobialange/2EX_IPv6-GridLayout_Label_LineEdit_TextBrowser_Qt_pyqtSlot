from PyQt6.QtWidgets import QMainWindow

from IPv6 import IPv6


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        widget = IPv6(self)
        self.setCentralWidget(widget)

        self.setWindowTitle("3. Stegreifaufgabe")