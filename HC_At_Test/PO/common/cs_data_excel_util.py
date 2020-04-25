# -*-coding:utf-8-*-
from PO.common.common_util import *
import logging
from Libs.excel_util import ExcelUtil
def login_info(env,skin,type):
    '''
    判断环境，皮肤，前后台获取登录信息
    :return:
    '''
    file_path = get_project_path() + '\\Data\\log_evn_info.xls'
    list = ExcelUtil(file_path).read_excel_addlist()
    info = []
    try:
        for i in range(len(list)):
            if list[i]['evn'] == env and list[i]['skin'] == skin and list[i]['type'] == type:
                info = list[i]
    except Exception as err:
        logging.info(err)

    return info


if __name__ == "__main__":
    temp = login_info("演示环境","豪彩","前端")
    print(temp["evn"])

