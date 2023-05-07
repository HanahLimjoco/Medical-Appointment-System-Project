import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.uic import loadUi
from datetime import datetime
from DAL.MedicalAppointment_dal import Doctor, HistoryLog

class UserInfo(QDialog):
    def __init__(self):
        super(UserInfo, self).__init__()
        loadUi("D:\\SCHOOL\\2Y TERM 3\\CPE106L\\ProjectFinal\\SOURCE CODES\\UI\\UserInfo.ui",self)
        self.submitButton1.clicked.connect(self.goToDiagnosis)

    def goToDiagnosis(self):
        # Check if any required fields are empty
        if not self.userName.text() or not self.userAge.text() or not self.userAddress.text():
            QtWidgets.QMessageBox.warning(self, "Required Fields", "Please fill out all required fields.")
            return
        
        userdiagnosis = UserDiagnosis()
        widget.addWidget(userdiagnosis)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(900)
        widget.setFixedHeight(795)

class UserDiagnosis(QDialog):
    def __init__(self):
        super(UserDiagnosis, self).__init__()
        loadUi("D:\\SCHOOL\\2Y TERM 3\\CPE106L\\ProjectFinal\\SOURCE CODES\\UI\\UserDiagnosis.ui",self)
        self.submitButton2.clicked.connect(self.goToDoctors)
    
    def goToDoctors(self):

        if not self.userWeight.text() or not self.userHeight.text() or not self.userTemp.text() or not self.userExer.text() or not self.userCommonSymptoms.text() or not self.userMedication.toPlainText() or not self.userAllergy.toPlainText() or not self.userFamDisease.toPlainText():
            QtWidgets.QMessageBox.warning(self, "Required Fields", "Please fill out all required fields.")
            return

        user_info = {
            "name": mainwindow.userName.text(),
            "age": mainwindow.userAge.text(),
            "address": mainwindow.userAddress.text(),
        }
        
        user_diagnosis = {
            "weight": self.userWeight.text(),
            "height": self.userHeight.text(),
            "temp": self.userTemp.text(),
            "exer": self.userExer.text(),
            "surgery": self.userSurgery.text(),
            "vaccination": self.userVaccination.text(),
            "diabetes": self.userDiabetes.text(),
            "common_symptoms": self.userCommonSymptoms.text(),
            "medication": self.userMedication.toPlainText(),
            "allergy": self.userAllergy.toPlainText(),
            "fam_disease": self.userFamDisease.toPlainText(),
        }

        doctordialog = DoctorDialog(user_info, user_diagnosis)
        widget.addWidget(doctordialog)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(674)
        widget.setFixedHeight(567)

class DoctorDialog(QDialog):
    def __init__(self, user_info, user_diagnosis):
        super(DoctorDialog, self).__init__()
        loadUi("D:\\SCHOOL\\2Y TERM 3\\CPE106L\\ProjectFinal\\SOURCE CODES\\UI\\Doctors.ui", self)  # Load the UI from file

        self.user_info = user_info
        self.user_diagnosis = user_diagnosis

        #Calls Doctor class to access database and read data from the Doctors table
        self.database = Doctor()
        self.queryModelLocation = self.database.getLocation()
        self.queryModelInfo = self.database.getInfo()
        
        #If values in combo box is changed
        self.comboBox.setModel(self.queryModelLocation)
        self.comboBox.currentIndexChanged.connect(self.setInfo)
        
        #If Submit button is pressed
        self.submitButton3.clicked.connect(self.goToSummary)

    #shows the information in the labels
    def setInfo(self, index):
        # Line Edit
        record = self.queryModelInfo.record(index)
        self.NameValueLabel.setText(record.value("Name"))
        self.EmailValueLabel.setText(str(record.value("Email")))
        self.ContactValueLabel.setText(str(record.value("ContactNumber")))

    def goToSummary(self):
        doctor_info = {
            "name": self.NameValueLabel.text(),
            "email": self.EmailValueLabel.text(),
            "contact": self.ContactValueLabel.text(),
        }
        
        summarydialog = SummaryDialog(self.user_info, self.user_diagnosis, doctor_info)
        widget.addWidget(summarydialog)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(931)
        widget.setFixedHeight(652)

class SummaryDialog(QDialog):
    def __init__(self, user_info, user_diagnosis, doctor_info):
        super(SummaryDialog, self).__init__()
        loadUi("D:\\SCHOOL\\2Y TERM 3\\CPE106L\\ProjectFinal\\SOURCE CODES\\UI\\Summary.ui", self)

        # Show user information in labels
        self.NameValueLabel.setText(user_info["name"])
        self.AgeValueLabel.setText(user_info["age"])
        self.AddressValueLabel.setText(user_info["address"])

        # Show user diagnosis information in labels
        self.WeightValueLabel.setText(user_diagnosis["weight"])
        self.HeightValueLabel.setText(user_diagnosis["height"])
        self.TempValueLabel.setText(user_diagnosis["temp"])
        self.ExerValueLabel.setText(user_diagnosis["exer"])
        self.SurgeryValueLabel.setText(user_diagnosis["surgery"])
        self.VaccinationValueLabel.setText(user_diagnosis["vaccination"])
        self.DiabetesValueLabel.setText(user_diagnosis["diabetes"])
        self.CommonSymptomsValueLabel.setText(user_diagnosis["common_symptoms"])
        self.MedicationValueLabel.setText(user_diagnosis["medication"])
        self.AllergyValueLabel.setText(user_diagnosis["allergy"])
        self.FamDiseaseValueLabel.setText(user_diagnosis["fam_disease"])

        # Show doctor information in labels
        self.DoctorNameValueLabel.setText(doctor_info["name"])
        self.EmailValueLabel.setText(doctor_info["email"])
        self.ContactValueLabel.setText(doctor_info["contact"])

        #call HistoryLog() class to access database and store name, doctor's name, and date & time using the addToHistLog method
        self.database = HistoryLog()
        storeName = user_info["name"]
        storeDoctor = doctor_info["name"]
        storeDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.database.addToHistLog(storeName, storeDoctor, storeDate)

        #If OK button is pressed
        self.okButton.clicked.connect(QtWidgets.QApplication.quit)

# Initialize the Qt application
app = QApplication(sys.argv)

# Create the main window
mainwindow = UserInfo()

# Create the stacked widget and add the main window to it
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(681)
widget.setFixedHeight(492)
widget.show()
app.exec()