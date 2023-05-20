from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QTextBrowser
from PyQt6.QtCore import Qt, pyqtSlot


class IPv6(QWidget):
    def __init__(self, parent=None):
        super(IPv6, self).__init__(parent)

        self.address = QLineEdit(self)

        # Aufgabe 1
        self.address.setInputMask("<Hhhh:Hhhh:Hhhh:Hhhh:Hhhh:Hhhh:Hhhh:Hhhh/90;_")

        # Aufgabe 2
        self.address.textChanged.connect(self.process_text)

        self.subnetmask = QTextBrowser(self)
        self.hex = QTextBrowser(self)

        layout = QGridLayout(self)

        layout.addWidget(QLabel("IPv6-Adresse:"), 1, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Subnetmask:"), 2, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Hexadezimal:"), 3, 1, Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.address, 1, 2)
        layout.addWidget(self.subnetmask, 2, 2)
        layout.addWidget(self.hex, 3, 2)

        self.setLayout(layout)

    # Aufgabe 2
    @pyqtSlot(str)
    def process_text(self, text: str):
        # Aufgabe 3
        split_str = text.split("/")

        if split_str[1]:
            self.subnetmask.setText(split_str[1])

        if split_str[0]:
            fields = split_str[0].split(":")

            memory = "0x"
            for field in fields:
                memory += field

            self.hex.setText(memory)

            #self.hex.setText("0x" + split_str[0].replace(":", ""))
