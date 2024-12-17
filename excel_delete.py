# 行削除テスト


import openpyxl

file_name = "data1.xlsx"

wb = openpyxl.load_workbook(file_name)
ws = wb['Sheet1']


def end_row():
    start_num = 4
    i = start_num
    while True:
        dte_str = ws.cell(i,4).value
        if dte_str != None:
            i += 1
        else:
            break
    return i-1        

finish_row_num = end_row()
print(finish_row_num)
