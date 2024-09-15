import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QLineEdit, QPushButton
class GoatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Milking App")
        self.setGeometry(100, 200, 500, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setText('Chase the goats away')
        self.layout.addWidget(self.label)

        self.enterButton = QPushButton("Chase")
        self.layout.addWidget(self.enterButton)
        self.enterButton.setStyleSheet("padding: 10px;")
        self.enterButton.clicked.connect(self.enterButtonClicked)

        self.setLayout(self.layout)
    def enterButtonClicked(self):
        self.hide()