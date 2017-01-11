import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sqlite3

conn = sqlite3.connect('fitnessTracker.db')



class WorkoutRecord(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    

    
    
    def initUI(self):
        
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        
        addBtn = QPushButton('Add new record', self)
        addBtn.resize(addBtn.sizeHint())
        #addBtn.move(90, 150)
        addBtn.clicked.connect(self.addNewRecord)
        
        checkBtn = QPushButton('Check existing records', self)
        checkBtn.resize(checkBtn.sizeHint())
        checkBtn.clicked.connect(self.checkRecords)
        
        
        hbox = QVBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(addBtn)
        hbox.addWidget(checkBtn)
        
        vbox = QFormLayout()
        
        self.dateInput = QLineEdit()
        vbox.addRow("date", self.dateInput)
        
        self.lengthInput = QLineEdit()
        vbox.addRow("workout length", self.lengthInput)
        
        self.typeInput = QLineEdit()
        vbox.addRow("workout type", self.typeInput)
        
        self.weightInput = QLineEdit()
        vbox.addRow("current weight", self.weightInput)
        
        
        vbox.addRow(hbox)
        
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.center()
        self.setWindowTitle('Fitness Tracker!')
        self.setWindowIcon(QIcon('web.png'))

        
        self.show()

    def center(self):
    
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def addNewRecord(self):
        print("adding new record");


    def checkRecords(self):
        print("checking records");

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = WorkoutRecord()
    sys.exit(app.exec_())
