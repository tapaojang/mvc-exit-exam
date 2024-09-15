import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QLineEdit, QPushButton
from Controller.isValidCow import isValidCow
from Controller.isValidCow import isCow
from View.cowApp import CowApp
from View.goatApp import GoatApp
from Controller.calculateBreasts import calculateBreasts
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cow Strike")
        self.setGeometry(100, 200, 500, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setText('Enter your id : ')
        self.layout.addWidget(self.label)

        self.textbox = QLineEdit()
        self.layout.addWidget(self.textbox)
        self.textbox.setStyleSheet("padding: 10px;")

        self.enterButton = QPushButton("Enter")
        self.layout.addWidget(self.enterButton)
        self.enterButton.setStyleSheet("padding: 10px;")
        self.enterButton.clicked.connect(self.enterButtonClicked)

        self.setLayout(self.layout)
    def enterButtonClicked(self):
        cowId = self.textbox.text()
        if cowId and cowId[0] != '0'and len(cowId) == 8 and isValidCow(cowId):
            # self.label.setText(f'Your cow id : {cowId} ')
            if isCow(cowId): #cow or goat
                self.label.setText(f'Your cow id : {cowId} is a cow')
                breastsnum = calculateBreasts(cowId) # 3 or 4 if 3 cannot milk else can milk
                print('breastsnum in app:', breastsnum)
                if breastsnum == 4:
                    print('Your cow id :', cowId, 'is a cow with 4 breasts')
                    self.mlikingCow = CowApp(cowId)
                    self.mlikingCow.show()
                else:
                    print('Your cow id :', cowId, 'is a cow with 3 breasts')
                    self.label.setText(f'Your cow id : {cowId} is a cow with 3 breasts. You cannot milking')
            else:
                self.label.setText(f'Your cow id : {cowId} is a goat')
                self.chaseGoat = GoatApp()
                self.chaseGoat.show()
            
        else:
            self.label.setText('Invalid id')

        self.label.setText('Enter your id : ')
        self.textbox.clear()
    