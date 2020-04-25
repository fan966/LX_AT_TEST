# coding = utf-8
import xlrd
import os
path = os.path.join(os.getcwd(),"\\python\\config\\case_data.xls") # 获取excel文件路径
#print(path)
# xlrd打开文件获取整个文件数据
data = xlrd.open_workbook(path)
# 获取excel文件所有sheet工作名
#print(data.sheet_names())
# 获取第一个工作表
table = data.sheets()[0]
# 获取第一个工作表行数
rows = table.nrows
# 获取文件列数
cols_num = table.ncols
#print(cols_num)
# 获取整行内容 第一行0表示下标
rows_value = table.row_values(0)
#print(rows_value) # 返回一个列表数据 数字后面会加小数点和一个零
# 获取整列内容  第一列0表示下标
cols_value = table.col_values(0)
# 循环获取每行的内容加入列表内
list = []
for i in range(rows):
    #print(table.row_values(i))
    list.append(table.row_values(i))

#print(list)
# 获取单元格内容--使用单元格定位
cell_A1 = table.cell(0,0).value
cell_A2 =table.cell(2,4).value
#print(cell_A1)
#print(cell_A2)
# 获取单元格内容--使用行/列索引
cell_b1 = table.row(2)[4].value
cell_b2 = table.row(1)[1].value
#print(cell_b1,':',cell_b2)
cell_c1 = table.col(4)[0].value
cell_c2 = table.col(2)[2].value
#print(cell_c1,":",cell_c2)




