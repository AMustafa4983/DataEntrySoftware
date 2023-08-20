from PyQt5 import QtCore, QtGui, QtWidgets

data = []
class Ui_ReviewersData(object):
    
    # def openSelectReviwersWindow(self):
    #     from SelectReviewers import Ui_SelectReviewers
    #     self.selectReviewersWindow = QtWidgets.QMainWindow()
    #     self.selectReviewersUi = Ui_SelectReviewers()
    #     self.selectReviewersUi.setupUi(self.selectReviewersWindow)
    #     self.selectReviewersWindow.show()
        
    def passData(self):
        from .SelectReviewers import Ui_SelectReviewers
        self.selectReviewersWindow = QtWidgets.QMainWindow()
        self.selectReviewersUi = Ui_SelectReviewers()
        self.selectReviewersUi.setupUi(self.selectReviewersWindow)
        self.selectReviewersWindow.show()
        
        data_of_RTUR = self.textEdit_RTUR.toPlainText()
        data_of_RTUL = self.textEdit_RTUL.toPlainText()
        data_of_RTUCR = self.textEdit_RTUCR.toPlainText()
        data_of_RTUCL = self.textEdit_RTUCL.toPlainText()
        data_of_PTR = self.textEdit_PTR.toPlainText()
        data_of_PTL = self.textEdit_PTL.toPlainText()
        data_of_FTR = self.textEdit_FTR.toPlainText()
        data_of_FTL = self.textEdit_FTL.toPlainText()
        data_of_HMR = self.textEdit_HMR.toPlainText()
        data_of_HML = self.textEdit_HML.toPlainText()
        data_of_PSR = self.textEdit_PSR.toPlainText()
        data_of_PSL = self.textEdit_PSL.toPlainText()
        data_of_ACU = self.textEdit_ACU.toPlainText()
        
        self.setData([data_of_RTUR, data_of_RTUL, 
                data_of_RTUCR, data_of_RTUCL, 
                data_of_PTR, data_of_PTL, 
                data_of_FTR, data_of_FTL,
                data_of_HMR, data_of_HML,
                data_of_PSR, data_of_PSL,
                data_of_ACU])
        
    def setData(self, input):
        data.append(input)
        return None
    
    def getData(self):
        return data


    def setupUi(self, ReviewersData):
        ReviewersData.setObjectName("ReviewersData")
        ReviewersData.resize(716, 624)
        self.centralwidget = QtWidgets.QWidget(ReviewersData)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 270, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        self.label_HM_test = QtWidgets.QLabel(self.centralwidget)
        self.label_HM_test.setGeometry(QtCore.QRect(410, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_HM_test.setFont(font)
        self.label_HM_test.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_HM_test.setObjectName("label_15")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 40, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 180, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(300, 270, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(200, 370, 31, 31))
        self.commandLinkButton_4.setText("")
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        
        self.label_ACU_test = QtWidgets.QLabel(self.centralwidget)
        self.label_ACU_test.setGeometry(QtCore.QRect(410, 340, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_ACU_test.setFont(font)
        self.label_ACU_test.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_ACU_test.setObjectName("label_20")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 180, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.textEdit_RTUCL = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_RTUCL.setGeometry(QtCore.QRect(290, 200, 31, 31))
        self.textEdit_RTUCL.setObjectName("textEdit_3")
        
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(200, 190, 31, 31))
        self.commandLinkButton_2.setText("")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        
        self.label_PS_test = QtWidgets.QLabel(self.centralwidget)
        self.label_PS_test.setGeometry(QtCore.QRect(410, 240, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_PS_test.setFont(font)
        self.label_PS_test.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_PS_test.setObjectName("label_17")
        
        self.textEdit_FTR = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_FTR.setGeometry(QtCore.QRect(240, 380, 31, 31))
        self.textEdit_FTR.setObjectName("textEdit_8")
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(300, 360, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(80, 40, 91, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(570, 120, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        
        self.textEdit_HML = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_HML.setGeometry(QtCore.QRect(560, 140, 31, 31))
        self.textEdit_HML.setObjectName("textEdit_9")
        
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(360, 110, 20, 281))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setGeometry(QtCore.QRect(280, 460, 171, 41))
        self.pushButtonSave.clicked.connect(self.passData)
        self.pushButtonSave.clicked.connect(ReviewersData.close)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.pushButtonSave.setObjectName("pushButton")
        
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(570, 220, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        
        self.textEdit_RTUR = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_RTUR.setGeometry(QtCore.QRect(240, 110, 31, 31))
        self.textEdit_RTUR.setStyleSheet("")
        self.textEdit_RTUR.setObjectName("textEdit")
        
        self.label_FT_test = QtWidgets.QLabel(self.centralwidget)
        self.label_FT_test.setGeometry(QtCore.QRect(120, 380, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_FT_test.setFont(font)
        self.label_FT_test.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_FT_test.setObjectName("label_12")
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 360, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(470, 130, 31, 31))
        self.commandLinkButton_5.setText("")
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(170, 150, 111, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(180, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("label")
        
        self.label_RTUC_test = QtWidgets.QLabel(self.centralwidget)
        self.label_RTUC_test.setGeometry(QtCore.QRect(120, 200, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_RTUC_test.setFont(font)
        self.label_RTUC_test.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_RTUC_test.setObjectName("label_6")
        
        self.textEdit_ACU = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_ACU.setGeometry(QtCore.QRect(530, 340, 31, 31))
        self.textEdit_ACU.setObjectName("textEdit_13")
        
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(440, 190, 111, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 90, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.textEdit_RTUL = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_RTUL.setGeometry(QtCore.QRect(290, 110, 31, 31))
        self.textEdit_RTUL.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.textEdit_RTUL.setObjectName("textEdit_2")
        
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(80, 520, 571, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        
        self.textEdit_PTL = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_PTL.setGeometry(QtCore.QRect(290, 290, 31, 31))
        self.textEdit_PTL.setObjectName("textEdit_5")
        
        self.label_PT_test = QtWidgets.QLabel(self.centralwidget)
        self.label_PT_test.setGeometry(QtCore.QRect(120, 290, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_PT_test.setFont(font)
        self.label_PT_test.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_PT_test.setObjectName("label_9")
        
        self.textEdit_RTUCR = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_RTUCR.setGeometry(QtCore.QRect(240, 200, 31, 31))
        self.textEdit_RTUCR.setObjectName("textEdit_4")
        
        self.textEdit_PTR = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_PTR.setGeometry(QtCore.QRect(240, 290, 31, 31))
        self.textEdit_PTR.setObjectName("textEdit_6")
        
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(200, 280, 31, 31))
        self.commandLinkButton_3.setText("")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        
        self.textEdit_FTL = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_FTL.setGeometry(QtCore.QRect(290, 380, 31, 31))
        self.textEdit_FTL.setObjectName("textEdit_7")
        
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(440, 290, 111, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        
        self.commandLinkButton_7 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_7.setGeometry(QtCore.QRect(470, 330, 31, 31))
        self.commandLinkButton_7.setText("")
        self.commandLinkButton_7.setObjectName("commandLinkButton_7")
        
        self.textEdit_HMR = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_HMR.setGeometry(QtCore.QRect(510, 140, 31, 31))
        self.textEdit_HMR.setObjectName("textEdit_10")
        
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(640, 50, 16, 481))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(170, 240, 111, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(520, 220, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setEnabled(True)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(470, 230, 31, 31))
        self.commandLinkButton_6.setText("")
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        
        self.textEdit_PSR = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_PSR.setGeometry(QtCore.QRect(510, 240, 31, 31))
        self.textEdit_PSR.setObjectName("textEdit_11")
        
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(170, 330, 111, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(200, 100, 31, 31))
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        
        self.textEdit_PSL = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_PSL.setGeometry(QtCore.QRect(560, 240, 31, 31))
        self.textEdit_PSL.setObjectName("textEdit_12")
        
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(520, 120, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 50, 21, 481))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        ReviewersData.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReviewersData)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 26))
        self.menubar.setObjectName("menubar")
        ReviewersData.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ReviewersData)
        self.statusbar.setObjectName("statusbar")
        ReviewersData.setStatusBar(self.statusbar)

        self.retranslateUi(ReviewersData)
        QtCore.QMetaObject.connectSlotsByName(ReviewersData)


    def retranslateUi(self, ReviewersData):
        _translate = QtCore.QCoreApplication.translate
        ReviewersData.setWindowTitle(_translate("ReviewersData", "MainWindow"))
        self.label_8.setText(_translate("ReviewersData", "R"))
        self.label_HM_test.setText(_translate("ReviewersData", "3.5 HM"))
        self.label_5.setText(_translate("ReviewersData", "R"))
        self.label_10.setText(_translate("ReviewersData", "L"))
        self.label_ACU_test.setText(_translate("ReviewersData", "3.7 ACU"))
        self.label_7.setText(_translate("ReviewersData", "L"))
        self.label_PS_test.setText(_translate("ReviewersData", "3.6 PS"))
        self.label_13.setText(_translate("ReviewersData", "L"))
        self.label_16.setText(_translate("ReviewersData", "L"))
        self.pushButtonSave.setText(_translate("ReviewersData", "Save"))
        self.label_19.setText(_translate("ReviewersData", "L"))
        self.label_FT_test.setText(_translate("ReviewersData", "3.4 FT"))
        self.label_11.setText(_translate("ReviewersData", "R"))
        self.labelTitle.setText(_translate("ReviewersData", "Tests"))
        self.label_RTUC_test.setText(_translate("ReviewersData", "3.17 RTUC"))
        self.label_4.setText(_translate("ReviewersData", "L"))
        self.label_PT_test.setText(_translate("ReviewersData", "3.15 PT"))
        self.label_2.setText(_translate("ReviewersData", "3.17 RTU"))
        self.label_18.setText(_translate("ReviewersData", "R"))
        self.label_3.setText(_translate("ReviewersData", "R"))
        self.label_14.setText(_translate("ReviewersData", "R"))

    