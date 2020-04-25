# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
class AgOfflinePaylocator:
    # 查询条件
    # 账号
    account = (By.XPATH,'//div[@class="reese clear"]/div[4][@class="form-group-inline"]//input[@id="account"]')
    # 订单号
    order_num = (By.XPATH,'//input[@title="订单号"]')
    # 姓名
    name = (By.XPATH,'//input[@title="姓名"]')
    # 查询按钮
    quire_btn = (By.XPATH,'//a[@class="btn btn-warning"][@onclick="RechargeCheck.search();"]')
    # 导出按钮
    dc_btn = (By.XPATH,'//a[@class="btn btn-primary"][@onclick="RechargeCheck.exportExcel();"][text()="导出"]')


    # table表格
    table = (By.XPATH,'//table[@class="datagrid-btable"]')

    # table第一行第三列订单号文本元素 keyong
    table_order_num = (By.XPATH,'//table[@class="datagrid-btable"]//tr[1][@datagrid-row-index="0"]//td[4][@field="fserialnumber"]//span[1]')
    # table14锁定按钮
    table_lock = (By.XPATH,'//table[@class="datagrid-btable"]//tr[@datagrid-row-index="0"]//td[@field="fstatus"]//input[@name="okBtnLock"]')
    # table14确定按钮
    table_submit_btn = (By.XPATH,'//table[@class="datagrid-btable"]//tr[1][@datagrid-row-index="0"]//td[@field="fstatus"]//input[@name="okBtn"]')
    # table14取消按钮
    table_cell_btn = (By.XPATH,'//table[@class="datagrid-btable"]//tr[@datagrid-row-index="0"]//td[@field="fstatus"]//input[@name="noBtn"]')
    # table13行状态 keyong
    table_stauas = (By.XPATH,'//table[@class="datagrid-btable"]//tr[1][@datagrid-row-index="0"]/td[@field="ddd"]/div/lable')



