# -*-coding:utf-8-*-
import xlrd
import xlutils
from xlrd import xldate_as_tuple
from PO.common.common_util import *
from datetime import datetime
data_path = get_project_path() + '\\Data\\game\\hc_game.xls'
activ_path = get_project_path() + '\\Data\\activ\\activ_data.xls'

class ExcelUtil(object):
    '''
    读取excel文件数据
    '''
    def __init__(self,file_path = None,index = None):
        if file_path == None:
            self.file_path = get_project_path() + '\\Data\\log_evn_info.xls'
        else:
            self.file_path = file_path
        if index == None:
            self.index = 0
        else:
            self.index = index
        self.data = xlrd.open_workbook(self.file_path)  # 打开文件获取整个文件数据
        self.sheet = self.data.sheets()[self.index]  # 获取sheet页内容


    def get_rows(self):
        '''
        获取行数
        :return:
        '''
        rows = self.sheet.nrows
        if rows >= 1:
            return rows
        else:
            return None
    def get_cols(self):
        '''
        获取列数
        :return:
        '''
        cols = self.sheet.ncols
        if cols >= 1:
            return cols
        else:
            return None

    def read_excel_addlist(self):
        '''
        读取excel数据组合列键值对列表/适合不用转换数据的excel表格
        :return:
        '''

        list = []
        rows = self.get_rows()
        # 获取第一行得值
        rows_value = self.sheet.row_values(0)
        for i in range(1,rows):
            values = self.sheet.row_values(i)
            dic =dict(zip(rows_value,values))
            list.append(dic)
        return list


    def read_excel_value_type_getdata(self):
        '''
        获取excel数据转换类型/获取键值对/适合需要转换数据的excel表格
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
        rows = self.get_rows()
        clos = self.get_cols()
        #value = self.sheet.cell(1,2).value # 获取单元格数据
        # 定义list添加值
        data_list = []
        # 获取第一行的值
        for i in range(1,rows):
            row_dict = {}
            for j in range(clos):
                cell = self.sheet.cell(i,j).value
                ctype = self.sheet.cell(i,j).ctype
                # 判断类型为数据且cell是否为整数
                if ctype == 2 and cell % 1 ==0:
                    cell = int(cell)
                elif ctype == 3 :
                    # 转换成时间的数字组成元组
                    data = xldate_as_tuple(cell,0)
                    # 转换为时间
                    data = datetime(*data)
                    # 转换时间制定格式
                    cell = data.strftime('%Y/%m/%d %H:%M:%S')
                elif ctype == 4:
                    cell = 'test'
                row_dict.update({self.sheet.cell(0,j).value:cell})
            data_list.append(row_dict)
        return data_list


if __name__ == "__main__":
    ex = ExcelUtil(activ_path)
    list1 = ex.read_excel_value_type_getdata()
    print(list1)
    print(list1[0]['top_bet_activ'])
    num = list1[0]['top_bet_activ'].split('|')[1] # [0] 代表切割完后list的下标0值复制给num
    print(num)
    input_value = util_str_convert_tupledata(num)
    for item_num,value in input_value:
        print(item_num,value)
        l = 0
        for j in range(len(value)):
            l += 1
            print(l)
            # shuru i l












