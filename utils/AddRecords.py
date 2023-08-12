import openpyxl

columnsName = {"A":6, "S":7, "SH":8, "AM":9, "AS":10, "H":11,"J":12, "S S":13, "H L":14, "M":15, "MA":16}

class AddRecords():
    '''
        this class used to add values to excel sheet.
        loadTemp() - Read Template and retrun active file.
    '''

    def __init__(self, path):
        self.path = path
        
        return None
    
    def loadTemp(self):
        try:
            self.wordbook_obj = openpyxl.load_workbook(self.path)
            print("Wordbook loaded!")
            self.sheet_obj = self.wordbook_obj.active
            print(f"Sheet {self.sheet_obj.title} is active now!")
        except Exception:
            raise "Loading template goes wrong | exception:"+ Exception

    def saveExcel(self,name):
        try:
            self.wordbook_obj.save(f'output/{name}.xlsx')
            return f"File Saved To output/{name}.xlsx"
        except Exception:
            raise "Saving File goes wrong | exception:"+ Exception

    def addReviewerData(self,scores):
        try:
            for key in scores.keys():
                column = columnsName[key]
                values = scores[key]
                for i in range(len(values)):
                    self.sheet_obj.cell(row=i+2,column=column,value=values[i])
        except Exception:
            raise "Adding Data goes wrong | exception:"+ Exception
