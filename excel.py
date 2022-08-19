import xlrd
import xlwt
import xlwings
import os

folder_path = r"D:\Cpanku\Desktop\py_excel"
excel_file = []
for path,dir,file in os.walk(folder_path):
    for name in file:
        if not "~$" in name:
            excel_file.append(os.path.join(path,name))

data = xlrd.open_workbook(excel_file[0])
table = data.sheet_by_index(0)
name_col = table.col_values(colx=1);name_col.pop(0)
ac_rows = 0
for i in range(len(name_col)):
    if i == 0 or name_col[i] == "":
        pass
    else:
        ac_rows += 1
information = table.row_values(rowx=1)

sql = [[""]*(ac_rows+1)]*len(information-1)

for i in range(1,table.ncols):
    get_rol = table.col_values(colx=i)
    for j in range(len(get_rol)):
        if get_rol[j] == '' or j==0:
            get_rol.pop(j)
    
