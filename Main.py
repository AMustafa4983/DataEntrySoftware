from gui.SelectReviewers import SelectReviewers
from gui.ReviewersData import ReviewersData
from gui.Exit import Exit
from utils.AddRecords import AddRecords

wordObj = AddRecords('template/template.xlsx')
wordObj.loadTemp()


records2 = {'A':[0,0,1,2,3,1,4,2,0,1,4,3,2],"S S":[0,0,1,2,3,"Abs",4,2,0,'Abs',4,3,2], "SH":[2,3,4,2,3,1,4,2,0,1,4,3,2]}

wordObj.addReviewerData(records2)

wordObj.saveExcel('test')