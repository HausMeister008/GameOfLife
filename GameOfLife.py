from uiFiles.GameOfLifeWindow import Ui_MainWindow
from PySide6 import QtSql, QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class GameOfLife(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

app = QApplication()
MainWindow = GameOfLife()
MainWindow.setStyleSheet(open('./styleMain.css', encoding='utf-8').read())
MainWindow.show()
app.exec()