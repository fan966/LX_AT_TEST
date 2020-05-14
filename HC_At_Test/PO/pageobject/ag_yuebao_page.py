# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
class AgYueBaolocator:
    # 添加余额宝按钮
    add_yuebao_btn = (By.XPATH,'//a[@class="btn"][text()="余额宝"]')
    # 活动名称
    yeb_activ_name = (By.XPATH,'//div[@class="product"]/input')
    # 选择公司
    # 活动状态
    activ_status = (By.XPATH, '//div/span[@class="label-title"][text()="活动状态："]/../input')
    # 参与时间
    start_time = (By.XPATH,'//div/span[@class="label-title"][text()="参与时间："]/../input[1]')
    end_time = (By.XPATH,'//div/span[@class="label-title"][text()="参与时间："]/../input[2]')
    # 活动版本下拉框
    activ_version_select = (By.XPATH,'//div/span[@class="label-title"][text()="活动版本："]/../select')
    # 活动图
    activ_img = (By.XPATH,'//div/span[@class="label-title"][text()="活动图："]/../form/input')
    # 手机活动图
    phone_activ_img = (By.XPATH,'//div/span[@class="label-title"][text()="手机活动图："]/../form/input')
    # 上传图片文本定位
    img_text = (By.XPATH,'//div[@class="panel window messager-window"]/div[2]/div[2]')
    # 上传图片确定按钮
    l_btn = (By.XPATH,'//a[@class="l-btn"]')
    # 选择代理
    activ_content = (By.XPATH,'//a[@class="btn btn-primary"][text()="选择代理"]')
    # 选择代理弹窗页所有页全选按钮
    pull_btn = (By.XPATH,'//a[@class="btn btn-success"][text()="所有页全选"]')
    # 选择代理确定按钮
    # 会员层级
    vip_lev = (By.XPATH,'//div/span[@class="label-title"][text()="会员层级："]/..//input')
    activ_content_btn = (By.XPATH,'//div[contains(@data-bind,"isShowCompanyDialog()")][not(@style="display: none;")]//a[@class="btn btn-success"][text()="确定"]')
    # 选择游戏
    game = (By.XPATH,'//a[@class="btn btn-primary"][text()="选择游戏"]')
    # 选择游戏弹窗全选按钮
    pull_game_btn = ('//div[@class="top"]/a[@class="btn btn-success"]')
    # 选择游戏确定按钮
    game_commit_btn = (By.XPATH,'//div[contains(@data-bind,"isShowCompanyDialog()")][not(@style="display: none;")]//a[@class="btn btn-success"][text()="确定"]')

    # 富文本框-域名限制
    f_text = (By.XPATH,'//div/span[@class="label-title"][text()="域名限制："]/../textarea[contains(@style,"width:")]')

    # 活动说明iframe
    activ_discription = (By.XPATH,'//iframe[@id="ueditor_0"]')
    # 手机活动说明iframe
    phone_activ_discription = (By.XPATH,'//iframe[@id="ueditor_1"]')
    # 电脑/手机活动说明富文本
    activity_remark = (By.XPATH,'//body')

    # 保存活动按钮
    add_activ_btn = (By.XPATH, '//a[@class="btn btn-primary"][text()="保存"]')



    # 样式方式
    @staticmethod
    def get_activ_ysloc(loc_name):
        '''
        活动样式/发放方式checkbox通用
        :param loc_name:
        :return:
       '//label/span[text()="手工发放"]/../input'
        '''
        locator = (By.XPATH,'//label/span[text()="{}"]/../input'.format(loc_name))
        return locator

    @staticmethod
    def get_table_list(item):
        '''
        获取列表每行的input输入list
        :param item:
        :return:
        '''
        locator = (By.XPATH,'//table[@class="table-list"]/tbody/tr[{}]/td//input'.format(item))
        return locator
    @staticmethod
    def get_table_addbtn(item):
        '''
        获取列表每行的新增按钮
        :param item:
        :return:
        '''
        locator = (By.XPATH,'//table[@class="table-list"]/tbody/tr[{}]/td/a[text()="新增"]'.format(item))
        return locator