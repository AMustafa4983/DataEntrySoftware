from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExitDialog(object):
    def setupUi(self, ExitDialog):
        ExitDialog.setObjectName("ExitDialog")
        ExitDialog.resize(353, 206)
        
        self.label = QtWidgets.QLabel(ExitDialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        
        self.pushButtonOk = QtWidgets.QPushButton(ExitDialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(120, 140, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonOk.setFont(font)
        self.pushButtonOk.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.pushButtonOk.setObjectName("pushButton")
        
        self.label_2 = QtWidgets.QLabel(ExitDialog)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(ExitDialog)
        QtCore.QMetaObject.connectSlotsByName(ExitDialog)

    def retranslateUi(self, ExitDialog):
        _translate = QtCore.QCoreApplication.translate
        ExitDialog.setWindowTitle(_translate("ExitDialog", "Dialog"))
        self.label.setText(_translate("ExitDialog", "Your excel sheet is"))
        self.pushButtonOk.setText(_translate("ExitDialog", "OK"))
        self.label_2.setText(_translate("ExitDialog", "Done!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExitDialog = QtWidgets.QDialog()
    ui = Ui_ExitDialog()
    ui.setupUi(ExitDialog)
    ExitDialog.show()
    sys.exit(app.exec_())
