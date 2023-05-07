# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserDiagnosis.ui'
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
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 795)
        font = QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(151, 166, 220)\n"
"}")
        self.userTemp = QLineEdit(Dialog)
        self.userTemp.setObjectName(u"userTemp")
        self.userTemp.setGeometry(QRect(770, 140, 71, 31))
        self.userTemp.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.submitButton2 = QPushButton(Dialog)
        self.submitButton2.setObjectName(u"submitButton2")
        self.submitButton2.setGeometry(QRect(370, 730, 141, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.submitButton2.setFont(font1)
        self.submitButton2.setStyleSheet(u"QPushButton{\n"
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
        self.WelcomeLabel = QLabel(Dialog)
        self.WelcomeLabel.setObjectName(u"WelcomeLabel")
        self.WelcomeLabel.setGeometry(QRect(350, 10, 191, 51))
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        self.WelcomeLabel.setFont(font2)
        self.WelcomeLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(99, 101, 185);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.WeightLabel = QLabel(Dialog)
        self.WeightLabel.setObjectName(u"WeightLabel")
        self.WeightLabel.setGeometry(QRect(60, 140, 121, 31))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.WeightLabel.setFont(font3)
        self.WeightLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.userHeight = QLineEdit(Dialog)
        self.userHeight.setObjectName(u"userHeight")
        self.userHeight.setGeometry(QRect(430, 140, 81, 31))
        self.userHeight.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.HeightLabel = QLabel(Dialog)
        self.HeightLabel.setObjectName(u"HeightLabel")
        self.HeightLabel.setGeometry(QRect(300, 140, 121, 31))
        self.HeightLabel.setFont(font)
        self.HeightLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.TempLabel = QLabel(Dialog)
        self.TempLabel.setObjectName(u"TempLabel")
        self.TempLabel.setGeometry(QRect(530, 140, 231, 31))
        self.TempLabel.setFont(font)
        self.TempLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.userWeight = QLineEdit(Dialog)
        self.userWeight.setObjectName(u"userWeight")
        self.userWeight.setGeometry(QRect(190, 140, 81, 31))
        self.userWeight.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.InstructionsLabel1 = QLabel(Dialog)
        self.InstructionsLabel1.setObjectName(u"InstructionsLabel1")
        self.InstructionsLabel1.setGeometry(QRect(40, 70, 821, 21))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.InstructionsLabel1.setFont(font4)
        self.InstructionsLabel1.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 8px;\n"
"padding-left: 5px;\n"
"}")
        self.InstructionsLabel2 = QLabel(Dialog)
        self.InstructionsLabel2.setObjectName(u"InstructionsLabel2")
        self.InstructionsLabel2.setGeometry(QRect(160, 90, 601, 21))
        self.InstructionsLabel2.setFont(font4)
        self.InstructionsLabel2.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 8px;\n"
"padding-left: 5px;\n"
"}")
        self.userExer = QLineEdit(Dialog)
        self.userExer.setObjectName(u"userExer")
        self.userExer.setGeometry(QRect(370, 240, 61, 31))
        self.userExer.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.surgeryLabel = QLabel(Dialog)
        self.surgeryLabel.setObjectName(u"surgeryLabel")
        self.surgeryLabel.setGeometry(QRect(20, 280, 331, 31))
        self.surgeryLabel.setFont(font)
        self.surgeryLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.ExerLabel = QLabel(Dialog)
        self.ExerLabel.setObjectName(u"ExerLabel")
        self.ExerLabel.setGeometry(QRect(190, 240, 161, 31))
        self.ExerLabel.setFont(font)
        self.ExerLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.MedicationLabel = QLabel(Dialog)
        self.MedicationLabel.setObjectName(u"MedicationLabel")
        self.MedicationLabel.setGeometry(QRect(100, 420, 391, 31))
        self.MedicationLabel.setFont(font)
        self.MedicationLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.userSurgery = QLineEdit(Dialog)
        self.userSurgery.setObjectName(u"userSurgery")
        self.userSurgery.setGeometry(QRect(370, 280, 61, 31))
        self.userSurgery.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.userMedication = QTextEdit(Dialog)
        self.userMedication.setObjectName(u"userMedication")
        self.userMedication.setGeometry(QRect(100, 460, 711, 51))
        self.userMedication.setStyleSheet(u"QTextEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.vaccinationLabel = QLabel(Dialog)
        self.vaccinationLabel.setObjectName(u"vaccinationLabel")
        self.vaccinationLabel.setGeometry(QRect(450, 240, 341, 31))
        self.vaccinationLabel.setFont(font)
        self.vaccinationLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.userVaccination = QLineEdit(Dialog)
        self.userVaccination.setObjectName(u"userVaccination")
        self.userVaccination.setGeometry(QRect(800, 240, 61, 31))
        self.userVaccination.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.allergyLabel = QLabel(Dialog)
        self.allergyLabel.setObjectName(u"allergyLabel")
        self.allergyLabel.setGeometry(QRect(100, 520, 91, 31))
        self.allergyLabel.setFont(font)
        self.allergyLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.userAllergy = QTextEdit(Dialog)
        self.userAllergy.setObjectName(u"userAllergy")
        self.userAllergy.setGeometry(QRect(100, 560, 711, 51))
        self.userAllergy.setStyleSheet(u"QTextEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.diabetesLabel = QLabel(Dialog)
        self.diabetesLabel.setObjectName(u"diabetesLabel")
        self.diabetesLabel.setGeometry(QRect(460, 280, 331, 31))
        self.diabetesLabel.setFont(font)
        self.diabetesLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.userDiabetes = QLineEdit(Dialog)
        self.userDiabetes.setObjectName(u"userDiabetes")
        self.userDiabetes.setGeometry(QRect(800, 280, 61, 31))
        self.userDiabetes.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.InstructionsLabel2_2 = QLabel(Dialog)
        self.InstructionsLabel2_2.setObjectName(u"InstructionsLabel2_2")
        self.InstructionsLabel2_2.setGeometry(QRect(0, 190, 911, 31))
        self.InstructionsLabel2_2.setFont(font4)
        self.InstructionsLabel2_2.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 8px;\n"
"}")
        self.commonSymptomsLabel = QLabel(Dialog)
        self.commonSymptomsLabel.setObjectName(u"commonSymptomsLabel")
        self.commonSymptomsLabel.setGeometry(QRect(20, 330, 591, 31))
        self.commonSymptomsLabel.setFont(font)
        self.commonSymptomsLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.userCommonSymptoms = QLineEdit(Dialog)
        self.userCommonSymptoms.setObjectName(u"userCommonSymptoms")
        self.userCommonSymptoms.setGeometry(QRect(620, 330, 61, 31))
        self.userCommonSymptoms.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.famDiseaseLabel = QLabel(Dialog)
        self.famDiseaseLabel.setObjectName(u"famDiseaseLabel")
        self.famDiseaseLabel.setGeometry(QRect(100, 620, 151, 31))
        self.famDiseaseLabel.setFont(font)
        self.famDiseaseLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.userFamDisease = QTextEdit(Dialog)
        self.userFamDisease.setObjectName(u"userFamDisease")
        self.userFamDisease.setGeometry(QRect(100, 660, 711, 51))
        self.userFamDisease.setStyleSheet(u"QTextEdit{\n"
"border: 2px solid rgb(55, 57, 124);\n"
"border-radius: 10px;\n"
"color: rgb(14, 15, 21);\n"
"padding-left: 10px;\n"
"padding-right: 20px;\n"
"background-color: rgb(242, 242, 255);\n"
"}")
        self.InstructionsLabel2_3 = QLabel(Dialog)
        self.InstructionsLabel2_3.setObjectName(u"InstructionsLabel2_3")
        self.InstructionsLabel2_3.setGeometry(QRect(-10, 380, 921, 31))
        self.InstructionsLabel2_3.setFont(font4)
        self.InstructionsLabel2_3.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 8px;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.userTemp.setText("")
        self.userTemp.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ex: 30", None))
        self.submitButton2.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.WelcomeLabel.setText(QCoreApplication.translate("Dialog", u"Welcome! ", None))
        self.WeightLabel.setText(QCoreApplication.translate("Dialog", u"Weight (kg):", None))
        self.userHeight.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ex: 158", None))
        self.HeightLabel.setText(QCoreApplication.translate("Dialog", u"Height (cm):", None))
        self.TempLabel.setText(QCoreApplication.translate("Dialog", u"Current Temperature (\u00b0C):", None))
        self.userWeight.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ex: 60", None))
        self.InstructionsLabel1.setText(QCoreApplication.translate("Dialog", u"Kindly fill out this form. Enter all the information in the text boxes, and press the \"Submit\" button if you are done.", None))
        self.InstructionsLabel2.setText(QCoreApplication.translate("Dialog", u"Please enter 'N/A' if you do not have any allergies, medications, or family diseases.", None))
        self.userExer.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y/N", None))
        self.surgeryLabel.setText(QCoreApplication.translate("Dialog", u"Have you had any surgeries recently?", None))
        self.ExerLabel.setText(QCoreApplication.translate("Dialog", u"Do you exercise?", None))
        self.MedicationLabel.setText(QCoreApplication.translate("Dialog", u"What medications are you taking right now?", None))
        self.userSurgery.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y/N", None))
        self.vaccinationLabel.setText(QCoreApplication.translate("Dialog", u"Have you had any recent vaccinations?", None))
        self.userVaccination.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y/N", None))
        self.allergyLabel.setText(QCoreApplication.translate("Dialog", u"Allergies:", None))
        self.diabetesLabel.setText(QCoreApplication.translate("Dialog", u"Do you have a history with Diabetes?", None))
        self.userDiabetes.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y/N", None))
        self.InstructionsLabel2_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Answer the items below with only &quot;Yes&quot; or &quot;No&quot;.</p></body></html>", None))
        self.commonSymptomsLabel.setText(QCoreApplication.translate("Dialog", u"Have you experienced common symptoms such as colds and others?", None))
        self.userCommonSymptoms.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y/N", None))
        self.famDiseaseLabel.setText(QCoreApplication.translate("Dialog", u"Family Diseases:", None))
        self.InstructionsLabel2_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Use the text boxes below to specify your answer. Use commas to separate your answers. Example: Asthma, Haemophilia</p></body></html>", None))
    # retranslateUi

