from uiFiles.GameOfLifeWindow import Ui_MainWindow
from PySide6 import QtSql, QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
import random

class GameOfLife(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.verticalLayout.setSpacing(0)
    
    def draw(self, population: list):
        # containingWidget_V = QFrame(self.centralwidget)
        for line in population:
            
            containingFrame_H = QFrame()
            horizontalLayout = QHBoxLayout(containingFrame_H)
            horizontalLayout.setSpacing(0)
            horizontalLayout.setContentsMargins(0, 0, 0, 0)
            
            for subject in line:
                new_subject = QFrame(containingFrame_H)
                if subject == 1:
                    new_subject.setStyleSheet("background: #ddd;")
                    # new_subject.setStyleSheet("background: #ddd; border:1px solid black;")
                else:
                    new_subject.setStyleSheet("background:black;")
                horizontalLayout.addWidget(new_subject)
        
            self.verticalLayout.addWidget(containingFrame_H)

length = random.randint(30, 70)
liste = [[random.randint(0, 1) for i in range(length)] for j in range(length)]

app = QApplication()
MainWindow = GameOfLife()
MainWindow.setStyleSheet(open('./styleMain.css', encoding='utf-8').read())
MainWindow.show()
MainWindow.draw(liste)
app.exec()

