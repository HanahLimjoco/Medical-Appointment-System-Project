# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Summary.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(931, 652)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(114, 125, 188);\n"
"}")
        self.SummaryLabel = QLabel(Dialog)
        self.SummaryLabel.setObjectName(u"SummaryLabel")
        self.SummaryLabel.setGeometry(QRect(280, 10, 361, 51))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.SummaryLabel.setFont(font)
        self.SummaryLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color: rgb(90, 76, 148);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.okButton = QPushButton(Dialog)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setGeometry(QRect(380, 570, 141, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.okButton.setFont(font1)
        self.okButton.setStyleSheet(u"QPushButton{\n"
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
        self.InstructionsLabel.setGeometry(QRect(100, 70, 761, 31))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.InstructionsLabel.setFont(font2)
        self.InstructionsLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 8px;\n"
"padding-left: 5px;\n"
"}")
        self.InstructionsLabel2 = QLabel(Dialog)
        self.InstructionsLabel2.setObjectName(u"InstructionsLabel2")
        self.InstructionsLabel2.setGeometry(QRect(250, 100, 461, 31))
        self.InstructionsLabel2.setFont(font2)
        self.InstructionsLabel2.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 8px;\n"
"padding-left: 5px;\n"
"}")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 140, 901, 401))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 2px solid rgb(95, 102, 131);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(95, 102, 131);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	color: rgb(0, 0, 0);\n"
"    background-color: rgb(136, 143, 185)\n"
"}\n"
"\n"
"QTabWidget::tab:selected {\n"
"    background-color: rgb(193, 203, 244);\n"
"}")
        self.UserInfoTab = QWidget()
        self.UserInfoTab.setObjectName(u"UserInfoTab")
        self.UserInfoTab.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(193, 203, 244)\n"
"}")
        self.NameLabel = QLabel(self.UserInfoTab)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setGeometry(QRect(40, 20, 71, 31))
        font3 = QFont()
        font3.setPointSize(15)
        self.NameLabel.setFont(font3)
        self.NameLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.AgeLabel = QLabel(self.UserInfoTab)
        self.AgeLabel.setObjectName(u"AgeLabel")
        self.AgeLabel.setGeometry(QRect(50, 70, 61, 31))
        self.AgeLabel.setFont(font3)
        self.AgeLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"}")
        self.AgeValueLabel = QLabel(self.UserInfoTab)
        self.AgeValueLabel.setObjectName(u"AgeValueLabel")
        self.AgeValueLabel.setGeometry(QRect(120, 70, 201, 31))
        self.AgeValueLabel.setFont(font3)
        self.AgeValueLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0)\n"
"}")
        self.NameValueLabel = QLabel(self.UserInfoTab)
        self.NameValueLabel.setObjectName(u"NameValueLabel")
        self.NameValueLabel.setGeometry(QRect(120, 20, 451, 31))
        self.NameValueLabel.setFont(font3)
        self.NameValueLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0)\n"
"}")
        self.AddressValueLabel = QLabel(self.UserInfoTab)
        self.AddressValueLabel.setObjectName(u"AddressValueLabel")
        self.AddressValueLabel.setGeometry(QRect(120, 120, 731, 31))
        self.AddressValueLabel.setFont(font3)
        self.AddressValueLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0)\n"
"}")
        self.AddressLabel = QLabel(self.UserInfoTab)
        self.AddressLabel.setObjectName(u"AddressLabel")
        self.AddressLabel.setGeometry(QRect(20, 120, 91, 31))
        self.AddressLabel.setFont(font3)
        self.AddressLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.tabWidget.addTab(self.UserInfoTab, "")
        self.UserDiagnosisTab = QWidget()
        self.UserDiagnosisTab.setObjectName(u"UserDiagnosisTab")
        self.UserDiagnosisTab.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(193, 203, 244)\n"
"}")
        self.WeightLabel = QLabel(self.UserDiagnosisTab)
        self.WeightLabel.setObjectName(u"WeightLabel")
        self.WeightLabel.setGeometry(QRect(40, 40, 91, 31))
        font4 = QFont()
        font4.setPointSize(11)
        self.WeightLabel.setFont(font4)
        self.WeightLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.HeightLabel = QLabel(self.UserDiagnosisTab)
        self.HeightLabel.setObjectName(u"HeightLabel")
        self.HeightLabel.setGeometry(QRect(40, 90, 91, 31))
        self.HeightLabel.setFont(font4)
        self.HeightLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.TempLabel = QLabel(self.UserDiagnosisTab)
        self.TempLabel.setObjectName(u"TempLabel")
        self.TempLabel.setGeometry(QRect(40, 140, 181, 31))
        self.TempLabel.setFont(font4)
        self.TempLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.DiabetesLabel = QLabel(self.UserDiagnosisTab)
        self.DiabetesLabel.setObjectName(u"DiabetesLabel")
        self.DiabetesLabel.setGeometry(QRect(520, 150, 261, 31))
        self.DiabetesLabel.setFont(font4)
        self.DiabetesLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.ExerLabel = QLabel(self.UserDiagnosisTab)
        self.ExerLabel.setObjectName(u"ExerLabel")
        self.ExerLabel.setGeometry(QRect(650, 190, 131, 31))
        self.ExerLabel.setFont(font4)
        self.ExerLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.SurgeryLabel = QLabel(self.UserDiagnosisTab)
        self.SurgeryLabel.setObjectName(u"SurgeryLabel")
        self.SurgeryLabel.setGeometry(QRect(520, 69, 261, 31))
        self.SurgeryLabel.setFont(font4)
        self.SurgeryLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.vaccinationLabel = QLabel(self.UserDiagnosisTab)
        self.vaccinationLabel.setObjectName(u"vaccinationLabel")
        self.vaccinationLabel.setGeometry(QRect(510, 110, 271, 31))
        self.vaccinationLabel.setFont(font4)
        self.vaccinationLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.MedicationLabel = QLabel(self.UserDiagnosisTab)
        self.MedicationLabel.setObjectName(u"MedicationLabel")
        self.MedicationLabel.setGeometry(QRect(20, 240, 221, 31))
        font5 = QFont()
        font5.setPointSize(12)
        self.MedicationLabel.setFont(font5)
        self.MedicationLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.AllergyLabel = QLabel(self.UserDiagnosisTab)
        self.AllergyLabel.setObjectName(u"AllergyLabel")
        self.AllergyLabel.setGeometry(QRect(160, 280, 81, 31))
        self.AllergyLabel.setFont(font4)
        self.AllergyLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.FamDiseaseLabel = QLabel(self.UserDiagnosisTab)
        self.FamDiseaseLabel.setObjectName(u"FamDiseaseLabel")
        self.FamDiseaseLabel.setGeometry(QRect(110, 320, 131, 31))
        self.FamDiseaseLabel.setFont(font5)
        self.FamDiseaseLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.WeightValueLabel = QLabel(self.UserDiagnosisTab)
        self.WeightValueLabel.setObjectName(u"WeightValueLabel")
        self.WeightValueLabel.setGeometry(QRect(140, 40, 91, 31))
        self.WeightValueLabel.setFont(font4)
        self.HeightValueLabel = QLabel(self.UserDiagnosisTab)
        self.HeightValueLabel.setObjectName(u"HeightValueLabel")
        self.HeightValueLabel.setGeometry(QRect(140, 90, 91, 31))
        self.HeightValueLabel.setFont(font4)
        self.TempValueLabel = QLabel(self.UserDiagnosisTab)
        self.TempValueLabel.setObjectName(u"TempValueLabel")
        self.TempValueLabel.setGeometry(QRect(230, 140, 71, 31))
        self.TempValueLabel.setFont(font4)
        self.ExerValueLabel = QLabel(self.UserDiagnosisTab)
        self.ExerValueLabel.setObjectName(u"ExerValueLabel")
        self.ExerValueLabel.setGeometry(QRect(790, 195, 71, 21))
        self.ExerValueLabel.setFont(font4)
        self.SurgeryValueLabel = QLabel(self.UserDiagnosisTab)
        self.SurgeryValueLabel.setObjectName(u"SurgeryValueLabel")
        self.SurgeryValueLabel.setGeometry(QRect(790, 70, 71, 31))
        self.SurgeryValueLabel.setFont(font4)
        self.VaccinationValueLabel = QLabel(self.UserDiagnosisTab)
        self.VaccinationValueLabel.setObjectName(u"VaccinationValueLabel")
        self.VaccinationValueLabel.setGeometry(QRect(790, 115, 71, 21))
        self.VaccinationValueLabel.setFont(font4)
        self.DiabetesValueLabel = QLabel(self.UserDiagnosisTab)
        self.DiabetesValueLabel.setObjectName(u"DiabetesValueLabel")
        self.DiabetesValueLabel.setGeometry(QRect(790, 150, 71, 31))
        self.DiabetesValueLabel.setFont(font4)
        self.MedicationValueLabel = QLabel(self.UserDiagnosisTab)
        self.MedicationValueLabel.setObjectName(u"MedicationValueLabel")
        self.MedicationValueLabel.setGeometry(QRect(250, 241, 611, 31))
        self.MedicationValueLabel.setFont(font4)
        self.AllergyValueLabel = QLabel(self.UserDiagnosisTab)
        self.AllergyValueLabel.setObjectName(u"AllergyValueLabel")
        self.AllergyValueLabel.setGeometry(QRect(250, 280, 611, 31))
        self.AllergyValueLabel.setFont(font4)
        self.FamDiseaseValueLabel = QLabel(self.UserDiagnosisTab)
        self.FamDiseaseValueLabel.setObjectName(u"FamDiseaseValueLabel")
        self.FamDiseaseValueLabel.setGeometry(QRect(250, 320, 611, 31))
        self.FamDiseaseValueLabel.setFont(font4)
        self.CommonSymptomsLabel = QLabel(self.UserDiagnosisTab)
        self.CommonSymptomsLabel.setObjectName(u"CommonSymptomsLabel")
        self.CommonSymptomsLabel.setGeometry(QRect(310, 30, 471, 31))
        self.CommonSymptomsLabel.setFont(font4)
        self.CommonSymptomsLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.CommonSymptomsValueLabel = QLabel(self.UserDiagnosisTab)
        self.CommonSymptomsValueLabel.setObjectName(u"CommonSymptomsValueLabel")
        self.CommonSymptomsValueLabel.setGeometry(QRect(790, 30, 71, 31))
        self.CommonSymptomsValueLabel.setFont(font4)
        self.tabWidget.addTab(self.UserDiagnosisTab, "")
        self.DoctorInfoTab = QWidget()
        self.DoctorInfoTab.setObjectName(u"DoctorInfoTab")
        self.DoctorInfoTab.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(193, 203, 244)\n"
"}")
        self.EmailLabel = QLabel(self.DoctorInfoTab)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setGeometry(QRect(110, 70, 71, 31))
        self.EmailLabel.setFont(font3)
        self.EmailLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.DoctorNameLabel = QLabel(self.DoctorInfoTab)
        self.DoctorNameLabel.setObjectName(u"DoctorNameLabel")
        self.DoctorNameLabel.setGeometry(QRect(40, 20, 141, 31))
        self.DoctorNameLabel.setFont(font3)
        self.DoctorNameLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.DoctorNameValueLabel = QLabel(self.DoctorInfoTab)
        self.DoctorNameValueLabel.setObjectName(u"DoctorNameValueLabel")
        self.DoctorNameValueLabel.setGeometry(QRect(200, 20, 291, 31))
        self.DoctorNameValueLabel.setFont(font3)
        self.ContactLabel = QLabel(self.DoctorInfoTab)
        self.ContactLabel.setObjectName(u"ContactLabel")
        self.ContactLabel.setGeometry(QRect(20, 120, 171, 31))
        self.ContactLabel.setFont(font3)
        self.ContactLabel.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 254, 234);\n"
"background-color:rgb(82, 87, 136);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}")
        self.ContactValueLabel = QLabel(self.DoctorInfoTab)
        self.ContactValueLabel.setObjectName(u"ContactValueLabel")
        self.ContactValueLabel.setGeometry(QRect(200, 120, 171, 31))
        self.ContactValueLabel.setFont(font3)
        self.EmailValueLabel = QLabel(self.DoctorInfoTab)
        self.EmailValueLabel.setObjectName(u"EmailValueLabel")
        self.EmailValueLabel.setGeometry(QRect(200, 70, 341, 31))
        self.EmailValueLabel.setFont(font3)
        self.tabWidget.addTab(self.DoctorInfoTab, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.SummaryLabel.setText(QCoreApplication.translate("Dialog", u"Summary of Information", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.InstructionsLabel.setText(QCoreApplication.translate("Dialog", u"Presented here is all of the information you have inputted. This session has been recorded in this system's ", None))
        self.InstructionsLabel2.setText(QCoreApplication.translate("Dialog", u"appointment log. Thank you for using our appointment system.", None))
        self.NameLabel.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.AgeLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Age:</p></body></html>", None))
        self.AgeValueLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Placeholder Text</span></p></body></html>", None))
        self.NameValueLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Placeholder Text</span></p></body></html>", None))
        self.AddressValueLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Placeholder Text</span></p></body></html>", None))
        self.AddressLabel.setText(QCoreApplication.translate("Dialog", u"Address:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UserInfoTab), QCoreApplication.translate("Dialog", u"User Information", None))
        self.WeightLabel.setText(QCoreApplication.translate("Dialog", u"Weight (kg):", None))
        self.HeightLabel.setText(QCoreApplication.translate("Dialog", u"Height (cm):", None))
        self.TempLabel.setText(QCoreApplication.translate("Dialog", u"Current Temperature (\u00b0C):", None))
        self.DiabetesLabel.setText(QCoreApplication.translate("Dialog", u"Do you have a history with Diabetes?", None))
        self.ExerLabel.setText(QCoreApplication.translate("Dialog", u"Do you exercise?", None))
        self.SurgeryLabel.setText(QCoreApplication.translate("Dialog", u"Have you had any surgeries recently?", None))
        self.vaccinationLabel.setText(QCoreApplication.translate("Dialog", u"Have you had any recent vaccinations?", None))
        self.MedicationLabel.setText(QCoreApplication.translate("Dialog", u"Currently Taken Medications:", None))
        self.AllergyLabel.setText(QCoreApplication.translate("Dialog", u"Allergies:", None))
        self.FamDiseaseLabel.setText(QCoreApplication.translate("Dialog", u"Family Diseases:", None))
        self.WeightValueLabel.setText("")
        self.HeightValueLabel.setText("")
        self.TempValueLabel.setText("")
        self.ExerValueLabel.setText("")
        self.SurgeryValueLabel.setText("")
        self.VaccinationValueLabel.setText("")
        self.DiabetesValueLabel.setText("")
        self.MedicationValueLabel.setText("")
        self.AllergyValueLabel.setText("")
        self.FamDiseaseValueLabel.setText("")
        self.CommonSymptomsLabel.setText(QCoreApplication.translate("Dialog", u"Have you experienced common symptoms such as colds and others?", None))
        self.CommonSymptomsValueLabel.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UserDiagnosisTab), QCoreApplication.translate("Dialog", u"User Medical Information", None))
        self.EmailLabel.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.DoctorNameLabel.setText(QCoreApplication.translate("Dialog", u"Doctor Name:", None))
        self.DoctorNameValueLabel.setText("")
        self.ContactLabel.setText(QCoreApplication.translate("Dialog", u"Contact Number:", None))
        self.ContactValueLabel.setText("")
        self.EmailValueLabel.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DoctorInfoTab), QCoreApplication.translate("Dialog", u"Doctor Information", None))
    # retranslateUi

