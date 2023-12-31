from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from .Loading import Ui_LoadingDialog

import sys

app = QtWidgets.QApplication(sys.argv)
SelectReviewers = QtWidgets.QMainWindow()

names = []
class Ui_SelectReviewers(object):

    def __init__(self):
        from .ReviewersData import Ui_ReviewersData
        self.reviewersDataWindow = QtWidgets.QMainWindow()
        self.reviewersDataUi = Ui_ReviewersData()

    def openReviewersDataWindow(self):
        self.reviewersDataUi.setupUi(self.reviewersDataWindow)
        self.reviewersDataWindow.show()
    
    def setReviewerName(self, Name):
        names.append(Name)

    def getReviewerName(self):
        return names
    
    def check(self, label):
        if label == 'HL':
            self.label_HL.setText("Checked ✔️")
    
    def openLoadingWindow(self):
        self.loadingWindow = QtWidgets.QDialog()
        self.loadingUi = Ui_LoadingDialog()
        self.loadingUi.setupUi(self.loadingWindow)
        self.loadingWindow.show()
        self.loadingUi.saveData()
        self.loadingWindow.close()
        app.quit()
        
    def setupUi(self, SelectReviewers):
        SelectReviewers.setObjectName("SelectReviewers")
        SelectReviewers.resize(617, 500)
        self.centralwidget = QtWidgets.QWidget(SelectReviewers)
        self.centralwidget.setObjectName("centralwidget")
        
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(100, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("label")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 30, 291, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(60, 40, 21, 381))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(70, 410, 481, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(540, 40, 16, 381))
        self.line_5.setMaximumSize(QtCore.QSize(16, 16777215))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        
        self.button_reviewer_A = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_A.clicked.connect(SelectReviewers.close)
        self.button_reviewer_A.setEnabled(True)
        self.button_reviewer_A.setGeometry(QtCore.QRect(150, 70, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_A.setFont(font)
        self.button_reviewer_A.setObjectName("pushButton")
        self.button_reviewer_A.clicked.connect(partial(self.setReviewerName, 'A'))
        self.button_reviewer_S = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_S.clicked.connect(SelectReviewers.close)
        self.button_reviewer_S.setGeometry(QtCore.QRect(150, 120, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_S.setFont(font)
        self.button_reviewer_S.setObjectName("pushButton_2")
        self.button_reviewer_S.clicked.connect(partial(self.setReviewerName, 'S'))

        
        self.button_reviewer_SH = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_SH.clicked.connect(SelectReviewers.close)
        self.button_reviewer_SH.setGeometry(QtCore.QRect(150, 170, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_SH.setFont(font)
        self.button_reviewer_SH.setObjectName("pushButton_3")
        self.button_reviewer_SH.clicked.connect(partial(self.setReviewerName, 'SH'))

        
        self.button_reviewer_AM= QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_AM.clicked.connect(SelectReviewers.close)
        self.button_reviewer_AM.setGeometry(QtCore.QRect(150, 220, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_AM.setFont(font)
        self.button_reviewer_AM.setObjectName("pushButton_4")
        self.button_reviewer_AM.clicked.connect(partial(self.setReviewerName, 'AM'))

        
        self.button_reviewer_AS = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_AS.clicked.connect(SelectReviewers.close)
        self.button_reviewer_AS.setGeometry(QtCore.QRect(150, 270, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_AS.setFont(font)
        self.button_reviewer_AS.setObjectName("pushButton_5")
        self.button_reviewer_AS.clicked.connect(partial(self.setReviewerName, 'AS'))

        
        self.button_reviewer_SS = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_SS.clicked.connect(SelectReviewers.close)
        self.button_reviewer_SS.setGeometry(QtCore.QRect(370, 170, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_SS.setFont(font)
        self.button_reviewer_SS.setObjectName("pushButton_6")
        self.button_reviewer_SS.clicked.connect(partial(self.setReviewerName, 'SS'))

        
        self.button_reviewer_M = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_M.clicked.connect(SelectReviewers.close)
        self.button_reviewer_M.setGeometry(QtCore.QRect(370, 270, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_M.setFont(font)
        self.button_reviewer_M.setObjectName("pushButton_7")
        self.button_reviewer_M.clicked.connect(partial(self.setReviewerName, 'M'))

        
        self.button_reviewer_J = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_J.clicked.connect(SelectReviewers.close)
        self.button_reviewer_J.setGeometry(QtCore.QRect(370, 120, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_J.setFont(font)
        self.button_reviewer_J.setObjectName("pushButton_8")
        self.button_reviewer_J.clicked.connect(partial(self.setReviewerName, 'J'))

        
        self.button_reviewer_H = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_H.clicked.connect(SelectReviewers.close)
        self.button_reviewer_H.setGeometry(QtCore.QRect(370, 70, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_H.setFont(font)
        self.button_reviewer_H.setObjectName("pushButton_9")
        self.button_reviewer_H.clicked.connect(partial(self.setReviewerName, 'H'))

        self.button_reviewer_HL = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_HL.clicked.connect(SelectReviewers.close)
        self.button_reviewer_HL.setGeometry(QtCore.QRect(370, 220, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_HL.setFont(font)
        self.button_reviewer_HL.setObjectName("pushButton_10")
        self.button_reviewer_HL.clicked.connect(partial(self.setReviewerName, 'HL'))

        
        self.button_reviewer_MA = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openReviewersDataWindow())
        self.button_reviewer_MA.clicked.connect(SelectReviewers.close)
        self.button_reviewer_MA.setGeometry(QtCore.QRect(260, 320, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_reviewer_MA.setFont(font)
        self.button_reviewer_MA.setObjectName("pushButton_11")
        self.button_reviewer_MA.clicked.connect(partial(self.setReviewerName, 'MA'))

        
        self.label_HL = QtWidgets.QLabel(self.centralwidget)
        self.label_HL.setGeometry(QtCore.QRect(330, 220, 31, 16))
        self.label_HL.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_HL.setObjectName("label_10")
        self.button_reviewer_HL.clicked.connect(partial(self.check,'HL'))

        
        self.label_SS = QtWidgets.QLabel(self.centralwidget)
        self.label_SS.setGeometry(QtCore.QRect(330, 170, 31, 16))
        self.label_SS.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_SS.setText("")
        self.label_SS.setObjectName("label_12")
        
        self.label_J = QtWidgets.QLabel(self.centralwidget)
        self.label_J.setGeometry(QtCore.QRect(330, 120, 31, 16))
        self.label_J.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_J.setText("")
        self.label_J.setObjectName("label_13")
        
        self.label_H = QtWidgets.QLabel(self.centralwidget)
        self.label_H.setGeometry(QtCore.QRect(330, 70, 31, 16))
        self.label_H.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_H.setText("")
        self.label_H.setObjectName("label_14")
        
        self.label_M = QtWidgets.QLabel(self.centralwidget)
        self.label_M.setGeometry(QtCore.QRect(330, 270, 31, 16))
        self.label_M.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_M.setText("")
        self.label_M.setObjectName("label_11")
        
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(110, 70, 31, 16))
        self.label_A.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_A.setText("")
        self.label_A.setObjectName("label_15")
        
        self.label_S = QtWidgets.QLabel(self.centralwidget)
        self.label_S.setGeometry(QtCore.QRect(110, 120, 31, 16))
        self.label_S.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_S.setText("")
        self.label_S.setObjectName("label_16")
        
        self.label_SH = QtWidgets.QLabel(self.centralwidget)
        self.label_SH.setGeometry(QtCore.QRect(110, 170, 31, 16))
        self.label_SH.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_SH.setText("")
        self.label_SH.setObjectName("label_17")
        
        self.label_AM = QtWidgets.QLabel(self.centralwidget)
        self.label_AM.setGeometry(QtCore.QRect(110, 220, 31, 16))
        self.label_AM.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_AM.setText("")
        self.label_AM.setObjectName("label_18")
        
        self.label_AS = QtWidgets.QLabel(self.centralwidget)
        self.label_AS.setGeometry(QtCore.QRect(110, 270, 31, 16))
        self.label_AS.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_AS.setText("")
        self.label_AS.setObjectName("label_19")
        
        self.label_MA = QtWidgets.QLabel(self.centralwidget)
        self.label_MA.setGeometry(QtCore.QRect(230, 330, 31, 16))
        self.label_MA.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_MA.setText("")
        self.label_MA.setObjectName("label_20")
        
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openLoadingWindow())
        self.pushButtonNext.setGeometry(QtCore.QRect(430, 370, 93, 31))
        
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonNext.setFont(font)
        self.pushButtonNext.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.pushButtonNext.setObjectName("pushButton_12")
        
        SelectReviewers.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SelectReviewers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 26))
        self.menubar.setObjectName("menubar")
        SelectReviewers.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SelectReviewers)
        self.statusbar.setObjectName("statusbar")
        SelectReviewers.setStatusBar(self.statusbar)

        self.retranslateUi(SelectReviewers)
        QtCore.QMetaObject.connectSlotsByName(SelectReviewers)

    def retranslateUi(self, SelectReviewers):
        _translate = QtCore.QCoreApplication.translate
        SelectReviewers.setWindowTitle(_translate("SelectReviewers", "MainWindow"))
        self.labelTitle.setText(_translate("SelectReviewers", "Reviewers Selected"))
        self.button_reviewer_A .setText(_translate("SelectReviewers", "Reviewer A"))
        self.button_reviewer_S.setText(_translate("SelectReviewers", "Reviewer S"))
        self.button_reviewer_SH.setText(_translate("SelectReviewers", "Reviewer SH"))
        self.button_reviewer_AM.setText(_translate("SelectReviewers", "Reviewer AM"))
        self.button_reviewer_AS.setText(_translate("SelectReviewers", "Reviewer AS"))
        self.button_reviewer_SS.setText(_translate("SelectReviewers", "Reviewer S S"))
        self.button_reviewer_M.setText(_translate("SelectReviewers", "Reviewer M"))
        self.button_reviewer_J.setText(_translate("SelectReviewers", "Reviewer J"))
        self.button_reviewer_H.setText(_translate("SelectReviewers", "Reviewer H"))
        self.button_reviewer_HL.setText(_translate("SelectReviewers", "Reviewer H L"))
        self.button_reviewer_MA.setText(_translate("SelectReviewers", "Reviewer MA"))
        self.pushButtonNext.setText(_translate("SelectReviewers", "Next")) 


    
