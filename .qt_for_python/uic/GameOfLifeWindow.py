# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GameOfLifeWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.wdgt_container = QWidget(self.centralwidget)
        self.wdgt_container.setObjectName(u"wdgt_container")
        self.wdgt_container.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.wdgt_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.wdgt_gameOfLife = QWidget(self.wdgt_container)
        self.wdgt_gameOfLife.setObjectName(u"wdgt_gameOfLife")
        self.verticalLayout_3 = QVBoxLayout(self.wdgt_gameOfLife)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.wdgt_gameOfLife)

        self.widget = QWidget(self.wdgt_container)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_stopCalc = QPushButton(self.widget)
        self.btn_stopCalc.setObjectName(u"btn_stopCalc")
        self.btn_stopCalc.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.btn_stopCalc.setFont(font)

        self.horizontalLayout.addWidget(self.btn_stopCalc)

        self.btn_startCalc = QPushButton(self.widget)
        self.btn_startCalc.setObjectName(u"btn_startCalc")
        self.btn_startCalc.setMinimumSize(QSize(100, 50))
        self.btn_startCalc.setMaximumSize(QSize(16777215, 50))
        self.btn_startCalc.setFont(font)

        self.horizontalLayout.addWidget(self.btn_startCalc)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.wdgt_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_stopCalc.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_startCalc.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

