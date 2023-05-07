import sys
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from datetime import datetime

class Doctor:
    def __init__(self):
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName("MedicalAppointment.db")
        if not self.database.open():
            print("Unable to open database")
    
    #Function for setting the Location Query Model and access Location entries from database
    def getLocation(self):
        queryModel = QSqlQueryModel()
        queryModel.setQuery("SELECT Location FROM Doctor", self.database)
        return queryModel

    #Function for setting the Info Query Model and access all entries from database
    def getInfo(self):
        queryModel = QSqlQueryModel()
        queryModel.setQuery("SELECT * FROM Doctor", self.database)
        return queryModel
    
class HistoryLog:
    def __init__(self):
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName("MedicalAppointment.db")
        if not self.database.open():
            print("Unable to open database")
    
    def addToHistLog(self, name, doctor, date):
        query = QSqlQuery()
        query.prepare("INSERT INTO HistLog (Name, DoctorName, Date) VALUES (:name, :doctor, :date)")
        query.bindValue(":name", name)
        query.bindValue(":doctor", doctor)
        query.bindValue(":date", date)

        if not query.exec():
            print("Error inserting data into HistLog table:", query.lastError().text())