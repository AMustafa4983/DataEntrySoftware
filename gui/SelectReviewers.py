from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

app = QApplication([])

class SelectReviewers(QMainWindow):
    '''
        This class for reveiwers list window.
        it makes the user select number of reveiwers that was attended the sesion.

        --> showWindow() - function to run the code that render the window
        --> setReviewers() - assign reviewers names to variables or append it in a list.
        --> getReviewers() - return selected reviewers.

        ---> windowTitle - string
    ''' 
    
    def __init__(self):
        super(SelectReviewers, self).__init__()
        uic.loadUi("ui/selectreviewers.ui",self)
        
    def showWindow():
        window = SelectReviewers()
        window.show()
        app.exec_()

    def setReviewers():
        return None

    def getReviewers():
        return None
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # import tkinter as tk
    # from tkinter import LabelFrame
    
    # window = tk.Tk()
    # window.title("Select Reviewers",)
    # window.geometry('600x450')
    # frame = LabelFrame(window, text="Choose Reviewers", padx=20, pady=20)
    # frame.pack(pady=20, padx=10)

    # C1 = tk.Checkbutton(frame, text="Reviewer1", width=200, anchor="w").pack()

    # C2 = tk.Checkbutton(frame, text = "Reviewer2", width=200, anchor="w").pack()

    # C3 = tk.Checkbutton(frame, text = "Reviewer3", width=200, anchor="w").pack()

    # C4 = tk.Checkbutton(frame, text = "Reviewer4", width=200, anchor="w").pack()
    
    # C5 = tk.Checkbutton(frame, text="Reviewer5", width=200,anchor="w").pack()

    # C6 = tk.Checkbutton(frame, text = "Reviewer6", width=200,anchor="w").pack()

    # C7 = tk.Checkbutton(frame, text = "Reviewer7", width=200,anchor="w").pack()

    # C8 = tk.Checkbutton(frame, text = "Reviewer8", width=200,anchor="w").pack()
    
    # C9 = tk.Checkbutton(frame, text = "Reviewer9", width=200,anchor="w").pack()

    # C10 = tk.Checkbutton(frame, text = "Reviewer10", width=200,anchor="w").pack()

    # window.mainloop()
    
 

    
    
    
