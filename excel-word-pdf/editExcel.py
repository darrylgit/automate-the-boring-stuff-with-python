import openpyxl
import os

os.chdir('/home/daniel/Coding/automate-the-boring-stuff/excel-word-pdf')

# Create new workbook
wb = openpyxl.Workbook()


sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'] = 42
sheet['A2'] = 'Hello'


sheet2 = wb.create_sheet()
sheet2.title = "New Sheet"

wb.save('example3.xlsx')
