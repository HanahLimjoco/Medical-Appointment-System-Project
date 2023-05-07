# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Doctors.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(674, 567)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(138, 153, 220)\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 30, 191, 51))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(99, 101, 185);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.submitButton3 = QPushButton(Dialog)
        self.submitButton3.setObjectName(u"submitButton3")
        self.submitButton3.setGeometry(QRect(260, 500, 141, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.submitButton3.setFont(font1)
        self.submitButton3.setStyleSheet(u"QPushButton{\n"
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
        self.InstructionsLabel = QLabel(Dialog)
        self.InstructionsLabel.setObjectName(u"InstructionsLabel")
        self.InstructionsLabel.setGeometry(QRect(-170, 100, 991, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.InstructionsLabel.setFont(font2)
        self.InstructionsLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 8px;\n"
"}")
        self.InstructionsLabel3 = QLabel(Dialog)
        self.InstructionsLabel3.setObjectName(u"InstructionsLabel3")
        self.InstructionsLabel3.setGeometry(QRect(-10, 470, 691, 21))
        self.InstructionsLabel3.setFont(font2)
        self.InstructionsLabel3.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 8px;\n"
"}")
        self.NameLabel = QLabel(Dialog)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setGeometry(QRect(160, 310, 71, 31))
        font3 = QFont()
        font3.setPointSize(14)
        self.NameLabel.setFont(font3)
        self.NameLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 150, 321, 21))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"border: 2px solid rgb(185, 188, 223);\n"
"border-radius: 10px;\n"
"background-color: rgb(206, 208, 238);\n"
"}\n"
"QComboBox:hover {\n"
"background-color: rgb(218, 220, 252);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(193, 194, 238)\n"
"}")
        self.InstructionsLabel2 = QLabel(Dialog)
        self.InstructionsLabel2.setObjectName(u"InstructionsLabel2")
        self.InstructionsLabel2.setGeometry(QRect(-10, 120, 691, 21))
        self.InstructionsLabel2.setFont(font2)
        self.InstructionsLabel2.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 8px;\n"
"}")
        self.EmailLabel = QLabel(Dialog)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setGeometry(QRect(160, 360, 71, 31))
        self.EmailLabel.setFont(font3)
        self.EmailLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"}")
        self.ContactLabel = QLabel(Dialog)
        self.ContactLabel.setObjectName(u"ContactLabel")
        self.ContactLabel.setGeometry(QRect(160, 410, 161, 31))
        self.ContactLabel.setFont(font3)
        self.ContactLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"}")
        self.NameValueLabel = QLabel(Dialog)
        self.NameValueLabel.setObjectName(u"NameValueLabel")
        self.NameValueLabel.setGeometry(QRect(240, 310, 291, 31))
        self.NameValueLabel.setFont(font3)
        self.NameValueLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.EmailValueLabel = QLabel(Dialog)
        self.EmailValueLabel.setObjectName(u"EmailValueLabel")
        self.EmailValueLabel.setGeometry(QRect(240, 360, 291, 31))
        self.EmailValueLabel.setFont(font3)
        self.EmailValueLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.ContactValueLabel = QLabel(Dialog)
        self.ContactValueLabel.setObjectName(u"ContactValueLabel")
        self.ContactValueLabel.setGeometry(QRect(330, 410, 171, 31))
        self.ContactValueLabel.setFont(font3)
        self.ContactValueLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255)\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Doctors List", None))
        self.submitButton3.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.InstructionsLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Refer to the drop-down box by clicking on it, and choose your preferred location for an appointment. </p></body></html>", None))
        self.InstructionsLabel3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Press the &quot;Submit&quot; button if you are done.</p></body></html>", None))
        self.NameLabel.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.InstructionsLabel2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">The details below will show more information on the doctor from that location.</p></body></html>", None))
        self.EmailLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Email:</p></body></html>", None))
        self.ContactLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Contact Number:</p></body></html>", None))
        self.NameValueLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Nothing Selected</span></p></body></html>", None))
        self.EmailValueLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Nothing Selected</span></p></body></html>", None))
        self.ContactValueLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Nothing Selected</span></p></body></html>", None))
    # retranslateUi

