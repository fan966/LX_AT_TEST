# -*- coding:utf-8 -*-
def main():
    data_list= [['产品名称', '单笔限额', '计算周期(小时)', '利率', '利息上限', '续存次数', '剩余数量', '利息稽核倍数', '操作'], ['2', '2-23', '2小时', '2%', '2', '2', '1', '2倍', '立即购买'], ['3', '23-456', '4小时', '4%', '4', '4', '4', '4倍', '立即购买']]
    for i in range(1,len(data_list)):
        if data_list[i][8] == '立即购买':
            num = int(data_list[i][1].split('-')[0])-1
            # input
            # commit_btn
            # if text
        else:
            continue


if __name__ == '__main__':
    main()