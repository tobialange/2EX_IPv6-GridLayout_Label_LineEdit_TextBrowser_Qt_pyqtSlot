from PyQt6.QtWidgets import QApplication

from MainWindow import MainWindow


import sys

# See https://doc.qt.io/qtforpython/PySide6/
if __name__ == '__main__':
    application = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    application.exec()