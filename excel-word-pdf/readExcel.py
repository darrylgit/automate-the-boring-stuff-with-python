import openpyxl
import os

os.chdir('/home/daniel/Coding/automate-the-boring-stuff/excel-word-pdf')

workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.get_sheet_by_name('Sheet1')

for i in range(1, 8):
    print(i, sheet.cell(row=i, column=2).value)
