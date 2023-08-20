from gui.SelectReviewers import Ui_SelectReviewers, app, SelectReviewers
from gui.ReviewersData import Ui_ReviewersData
from utils.AddRecords import AddRecords
from gui.Loading import records
from datetime import date, datetime

wordObj = AddRecords('template/template.xlsx')
wordObj.loadTemp()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


records2 = {'A':[0,0,1,2,3,1,4,2,0,1,4,3,2],"S S":[0,0,1,2,3,"Abs",4,2,0,'Abs',4,3,2], "SH":[2,3,4,2,3,1,4,2,0,1,4,3,2]}


ui = Ui_SelectReviewers()
ui.setupUi(SelectReviewers)
SelectReviewers.show()
app.exec_()
wordObj.addReviewerData(records)
wordObj.saveExcel(f'{date.today()}, {current_time} --> output.xlsx')