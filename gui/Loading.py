from PyQt5 import QtCore, QtGui, QtWidgets

records = {}
class Ui_LoadingDialog(object):
    
    def setupUi(self, LoadingDialog):
        LoadingDialog.setObjectName("LoadingDialog")
        LoadingDialog.resize(400, 168)
        
        self.label = QtWidgets.QLabel(LoadingDialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(LoadingDialog)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(LoadingDialog)
        QtCore.QMetaObject.connectSlotsByName(LoadingDialog)

    def retranslateUi(self, LoadingDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadingDialog.setWindowTitle(_translate("LoadingDialog", "Dialog"))
        self.label.setText(_translate("LoadingDialog", "Your excel Generated"))
        self.label_2.setText(_translate("LoadingDialog", "Successfully!"))

    def saveData(self):
        from .ReviewersData import data
        from .SelectReviewers import names

        for name in names:
            for ls in data:
                for i in range(len(ls)):
                    if ls[i]=='':
                        ls[i] = '--'
                records[name] = ls
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadingDialog = QtWidgets.QDialog()
    ui = Ui_LoadingDialog()
    ui.setupUi(LoadingDialog)
    LoadingDialog.show()
    sys.exit(app.exec_())
