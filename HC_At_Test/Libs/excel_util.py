# -*-coding:utf-8-*-
import xlrd
import xlutils
from PO.common.common_util import get_project_path
data_path = get_project_path() + '\\Data\\game\\hc_game.xls'
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
        读取excel数据组合列键值对列表
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


if __name__ == "__main__":
    #ex = ExcelUtil()
    # list = ex.read_excel_addlist()
    # user = list[0]["evn"]
    # skin = list[0]["skin"]
    # type = list[0]["type"]
    # num = len(list)
    # print(num)
    # for i in range(len(list)):
    #     if list[i]["evn"] == "演示环境" and list[i]["skin"] == "豪彩" and list[i]["type"] == "前端":
    #         print(list[i])
    ex = ExcelUtil(data_path)
    list = ex.read_excel_addlist()
    print(list)
    #print(list[0]['lottery'])
    str1 = list[0]['item'].split('|')
    print(str1)
    #print(list[0]['lottery_id'])
    #print('http://csdqthcweb.lx901.com/OffcialOtherGame/Index/{}'.format(list[0]['lottery_id']))
    print(len(str1))
    print(str1[2][3])
    temp = str1[2].split(',')
    print(temp)
    print(len(temp))
    temp1 = str1[0].split(',')
    print(len(temp1))
    print(temp1)



    # for i in range(len(str1)):
    #     j = 1
    #     j += i
    #     print(i)
    #     print(j)











