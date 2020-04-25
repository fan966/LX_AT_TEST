# -*-coding:utf-8-*-

"""
根据table的id属性和table中的某一个元素定位其在table中的位置
table包括表头，位置坐标都是从1开始算
tableId：table的id属性
queryContent：需要确定位置的内容
"""
from selenium.webdriver.common.by import By
def get_table_content(tableId, queryContent):
    arr = []
    arr1 = []
    table_loc = (By.ID, tableId)
    # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
    table_tr_list = driver.find_element(*table_loc).find_elements(By.TAG_NAME, "tr")
    for tr in table_tr_list:
        arr1 = (tr.text).split(" ")  # 以空格拆分成若干个(个数与列的个数相同)一维列表
        # print(tr.text)
        # print(arr1)
        arr.append(arr1)  # 将表格数据组成二维的列表

    # 循环遍历table数据，确定查询数据的位置
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if queryContent == arr[i][j]:
                print("%r坐标为(%r,%r)" % (queryContent, i + 1, j + 1))

if __name__ == "__main__":
    get_table_content("myTable", "第二行第二列")
