# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
class AgHomeLocator:
    # 首页iframe(包含登录页面)
    top_iframe = (By.XPATH,'//frame[@name="topFrame"]')
    # table页iframe
    tab_iframe = (By.XPATH,'//div[@class="panel"]//div[@class="bread-crumbs"]/following-sibling::iframe[1][@class="tabBar_iframe"]')

    # 一级菜单//替换文本即可
    cw = (By.XPATH,'//span[@class="tree-title"][text()="财务管理"]')
    zh = (By.XPATH,'//span[@class="tree-title"][text()="账户管理"]')
    # 二级菜单/通用
    gs = (By.XPATH,'//span[@class="tree-title"][text()="公司入款"]')


    # table菜单通用定位/替换文本即可
    table = (By.XPATH,'//span[@class="tabs-title tabs-closable"][text()="出款审核"]')
    # table菜单通用刷新按钮
    table_refresh= (By.XPATH,'//span[@class="tabs-title tabs-closable"][text()="出款审核"]/../following-sibling::span/a[@class="icon-mini-refresh"]')
    # table菜单通用关闭按钮
    table_close = (By.XPATH,'//span[@class="tabs-title tabs-closable"][text()="推广管理"]/../following-sibling::a[1]')


    # 系统公告弹窗
    sys_pop = (By.XPATH,'//div[@id="companyNoticeRoot"]')
    # 系统公告弹窗关闭按钮
    sys_pop_btn = (By.XPATH,'//div[@id="companyNoticeRoot"]//a[@class="close"]')


    # 财务操作提示框/通用
    financia_pop = (By.XPATH, '//table[@class="d-dialog"]')
    # 财务操作提示文本
    financia_pop_text = (By.XPATH, '//table[@class="d-dialog"]//tr[2]//div[contains(@id,"d-content")]')
    # 财务操作确认按钮
    financia_pop_btn = (By.XPATH, '//input[@type="button"][@value="确定"]')
    # 财务操作取消按钮
    financia_pop_cenbtn = (By.XPATH, '//table[@class="d-dialog"]//tr[3]//input[@value="取消"]')

    # 相同金额提示信息
    # 消息提示框
    mag_panel = (By.XPATH, '//div[@class="panel window messager-window"]')
    # 消息提示文本
    mag_panel_text = (By.XPATH, '//div[@class="messager-body panel-body panel-body-noborder window-body"]/div[2]')
    # 消息提示框确定按钮
    mag_panel_btn = (By.XPATH, '//span[@class="l-btn-left"]/span[@class="l-btn-text l-btn-focus"][text()="确定"]')


    # 操作提示通用弹窗文本
    pop_text = (By.XPATH,'//div[@class="d-content"]/span')
    # 操作提示tc通用确定按钮
    pop_btn = (By.XPATH,'//div[@class="d-buttons"]/input[@type="button"]')


    # 条件配置按钮
    set_btn = (By.XPATH, '//div[@class="form-group-inline"]/a[text()="条件配置"]')
    # 条件配置弹窗复选框选项list
    check_box_list = (By.XPATH, '//div[@class="filter-list"]//li//input[@type="checkbox"]')
    # 条件配置确定按钮
    check_box_commit = (By.XPATH,'//div[@class="btn_confirm"]/button')

    @staticmethod
    def get_menu_loc(menu_name):
        '''
        获取菜单的locator
        :param menu_name:菜单名称
        :return:
        '''
        locator = (By.XPATH,'//span[@class="tree-title"][text()="{}"]'.format(menu_name))
        return locator

    @staticmethod
    def get_table_loc(table_name):
        '''
        获取table的locator
        :param table_name:
        :return:
        '''
        locator = (By.XPATH,'//span[@class="tabs-title tabs-closable"][text()="{}"]'.format(table_name))
        return locator

    @staticmethod
    def get_table_close_btn_loc(table_name):
        '''
        获取tanle栏目关闭按钮
        :param table_name:
        :return:
        '''
        locator = (By.XPATH,'//span[@class="tabs-title tabs-closable"][text()="{}"]/../following-sibling::a[1]'.format(table_name))
        return locator

    @staticmethod
    def get_table_refresh_loc(table_name):
        '''
        获取table栏目刷新按钮
        :param table_name:
        :return:
        '''
        locator = (By.XPATH,'//span[@class="tabs-title tabs-closable"][text()="{}"]/../following-sibling::span/a[@class="icon-mini-refresh"]'.format(table_name))
        return locator
