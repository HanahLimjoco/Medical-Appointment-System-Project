import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from UI.MedicalAppointment_ui import UserInfo

def main():
    # Initialize the Qt application
    app = QApplication(sys.argv)

    # Create the main window
    window = UserInfo()

    # Create the stacked widget and add the main window to it
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setFixedWidth(681)
    widget.setFixedHeight(492)
    widget.show()

    # Run the application
    app.exec()

if __name__ == '__main__':
    main()