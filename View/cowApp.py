import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QLineEdit, QPushButton
from Controller.calculateMilk import calculateMilk
class CowApp(QWidget):
    totalMilk = 0 # class variable to keep track of total milk
    def __init__(self, cowId):
        super().__init__()
        self.setWindowTitle("Milking App")
        self.setGeometry(100, 200, 500, 200)
        self.cowId = cowId

        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setText('Milking your cow')
        self.layout.addWidget(self.label)

        self.calculateMilkLabel = QLabel()
        self.layout.addWidget(self.calculateMilkLabel)

        self.totalMilkLabel = QLabel()
        self.totalMilkLabel.setText(f'You have milked {CowApp.totalMilk} liters total of milk ')
        self.layout.addWidget(self.totalMilkLabel)

        self.milkingButton = QPushButton("Milking")
        self.layout.addWidget(self.milkingButton)
        self.milkingButton.setStyleSheet("padding: 10px;")
        self.milkingButton.clicked.connect(self.milkingButtonClicked)

        self.setLayout(self.layout)
    def milkingButtonClicked(self):
        liter = calculateMilk(self.cowId)
        CowApp.totalMilk += liter
        self.calculateMilkLabel.setText(f'You have milked {liter} liters of milk this time')
        self.totalMilkLabel.setText(f'You have milked {CowApp.totalMilk} liters total of milk ')
        print('You have milked', liter, 'liters of milk this time')
        print('You have milked', CowApp.totalMilk, 'liters total of milk')

        self.notiLabel = QLabel()
        self.notiLabel.setText('Do you want to stop milking?')
        self.milkingButton.hide()

        self.layout.addWidget(self.notiLabel)

        self.milkingButton = QPushButton("Y")
        self.layout.addWidget(self.milkingButton)
        self.milkingButton.setStyleSheet("padding: 10px;")
        self.milkingButton.clicked.connect(self.stopMilking)
        
    def stopMilking(self):
        self.hide()
        print('You have stopped milking')