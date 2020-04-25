# coding = utf-8
import xlrd
import os
from xlutils.copy import copy
from study_test_file.test import *
from datetime import datetime
from xlrd import xldate_as_tuple
class Excel_data:
    def __init__(self,file_path=None,index=None):
        if file_path == None:
            self.file_path = os.path.join(os.getcwd(),"\\python\\config\\case_data.xls")
        else:
            self.file_path = file_path
        if index == None:
            self.index = 0
        else:
            self.index = index
        self.data = xlrd.open_workbook(self.file_path) # 打开文件获取整个文件数据
        self.sheet = self.data.sheets()[self.index] # 获取sheet页内容
    def get_data(self):
        '''
        每行数据列表添加至列表里
        '''
        list = [] # 定义空的列表用来添加每行数据
        rows = self.get_rows()
        if rows != None:
            for i in range(rows):
                row_value = self.sheet.row_values(i) # 获取指定行的数据
                list.append(row_value)
                return list
        return None

    def get_rows(self):
        '''
        获取文件行数
        '''
        rows = self.sheet.nrows  # 获取sheet所有行数
        if rows >= 1: # 容错处理（防止文件无数据或者未保存获取失败情况导致程序崩溃）
            return rows
        else:
            return None
    def get_cols(self):
        '''
        获取文件列数
        :return:
        '''
        cols = self.sheet.ncols # 获取sheet所有列数
        return cols

    def get_cell_value(self,row,col):
        '''
        获取单元格数据
        '''
        if self.get_rows()>= row:
            cell_value = self.sheet.cell(row,col).value #行列索引确定单元格数据
            return cell_value
        return None

    # 获取sheet页数据组合排列为行列对应值字典的列表
    def read_excel_data_list(self):
        result = []
        rows = self.get_rows()
        keys = self.sheet.row_values(0) # 获取第一行栏目标题数据
        for i in range(1,rows):
            row_value = self.sheet.row_values(i)
            row_dict =dict(zip(keys,row_value)) # 排列组合为行列对应值的字典
            result.append(row_dict)
        return result


    def read_excel_data_and_type_cast(self):
        '''
        获取excel数据并转换类型
        :return:
        '''
        # 0-empty
        # 1-string
        # 2-number
        # 3-date
        # 4-boolean
        # 5-Error
        # data = xlrd.open_workbook(self.file_path) # 打开文件获取整个文件数据
        # sheet = data.sheet_by_index(self.index) # 获取sheet页的内容
        rows = self.get_rows() # 获取sheet页的所有行数
        cols = self.get_cols() # 获取sheet页的所有列数
        list = []
        for i in range(1,rows):
            result = {}
            for j in range(cols):
                ctype = self.sheet.cell(i,j).ctype # 获取单元格数据类型
                cell = self.get_cell_value(i,j)
                if ctype == 2 and ctype % 1 == 0: # 如果是整形
                    cell = int(cell)
                elif ctype == 3:
                    data = datetime(*xldate_as_tuple(cell,0))
                    cell = data.strftime('%Y/%m%d %H:%M:%S')
                elif ctype == 4:
                    cell = True if cell == 1 else False
                result.update({self.sheet.cell_value(0,j):cell})
            list.append(result)
        return list



    def write_datas(self,row,value):
        '''
        写入excel数据
        :return:
        '''
        read_data = xlrd.open_workbook(self.file_path) # 读取的excel现有的数据
        write_data = copy(read_data) # 复制现有的数据
        write_data.get_sheet(0).write(row,9,value) # 在指定行，列添加value
        write_data.save(self.file_path) # 写完数据后保存和保存路径


if __name__ == '__main__':
    # ex = Excel_data('F:\python\config\keyword.xls')
    # #print(ex.write_datas(1,"test"))
    # temp = ex.get_cell_value(4,8)
    # data_list = temp.split("=")
    file_path = get_project_path() + "\\libs\\PageCheck.xlsx"
    sheet_name = 0
    ec = Excel_data(file_path,sheet_name)
    list_value = ec.read_excel_data_and_type_cast()
    print(list_value)











