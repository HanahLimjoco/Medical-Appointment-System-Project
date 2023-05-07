# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserInfo.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(689, 492)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(114, 125, 188);\n"
"}")
        self.userAddress = QLineEdit(Dialog)
        self.userAddress.setObjectName(u"userAddress")
        self.userAddress.setGeometry(QRect(220, 320, 411, 31))
        self.userAddress.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.submitButton1 = QPushButton(Dialog)
        self.submitButton1.setObjectName(u"submitButton1")
        self.submitButton1.setGeometry(QRect(250, 390, 141, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.submitButton1.setFont(font)
        self.submitButton1.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(185, 188, 223);\n"
"border-radius: 10px;\n"
"background-color: rgb(206, 208, 238);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(218, 220, 252);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 194, 238)\n"
"}")
        self.AppointmentLabel = QLabel(Dialog)
        self.AppointmentLabel.setObjectName(u"AppointmentLabel")
        self.AppointmentLabel.setGeometry(QRect(120, 80, 451, 51))
        font1 = QFont()
        font1.setPointSize(23)
        font1.setBold(True)
        self.AppointmentLabel.setFont(font1)
        self.AppointmentLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.EnterNameLabel = QLabel(Dialog)
        self.EnterNameLabel.setObjectName(u"EnterNameLabel")
        self.EnterNameLabel.setGeometry(QRect(80, 190, 121, 41))
        font2 = QFont()
        font2.setPointSize(14)
        self.EnterNameLabel.setFont(font2)
        self.EnterNameLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.userAge = QLineEdit(Dialog)
        self.userAge.setObjectName(u"userAge")
        self.userAge.setGeometry(QRect(220, 260, 61, 31))
        self.userAge.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.EnterAgeLabel = QLabel(Dialog)
        self.EnterAgeLabel.setObjectName(u"EnterAgeLabel")
        self.EnterAgeLabel.setGeometry(QRect(80, 250, 111, 41))
        self.EnterAgeLabel.setFont(font2)
        self.EnterAgeLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.EnterAddressLabel = QLabel(Dialog)
        self.EnterAddressLabel.setObjectName(u"EnterAddressLabel")
        self.EnterAddressLabel.setGeometry(QRect(80, 310, 131, 41))
        self.EnterAddressLabel.setFont(font2)
        self.EnterAddressLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 10px;\n"
"padding-left: 2px;\n"
"}")
        self.userName = QLineEdit(Dialog)
        self.userName.setObjectName(u"userName")
        self.userName.setGeometry(QRect(220, 200, 291, 31))
        self.userName.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.userAddress.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ex: Metro Manila, Makati City, Alsons Building 2286 Pasong Tamo Ext.", None))
        self.submitButton1.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.AppointmentLabel.setText(QCoreApplication.translate("Dialog", u"Medical Appointment System", None))
        self.EnterNameLabel.setText(QCoreApplication.translate("Dialog", u"Enter Name:", None))
        self.userAge.setPlaceholderText(QCoreApplication.translate("Dialog", u"Age", None))
        self.EnterAgeLabel.setText(QCoreApplication.translate("Dialog", u"Enter Age:", None))
        self.EnterAddressLabel.setText(QCoreApplication.translate("Dialog", u"Enter Address:", None))
        self.userName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Last Name, First Name MI.", None))
    # retranslateUi

