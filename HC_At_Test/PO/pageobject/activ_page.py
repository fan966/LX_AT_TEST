# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
class ActivLocator:
    # 查询按钮
    search_btn = (By.XPATH,'//div[@class="form-group-inline"]/a[text()="查询"]')

    # 添加活动按钮
    add_activ = (By.XPATH,'//a[text()="添加活动"]')
    # 活动类型-签到活动
    sign_activ = (By.XPATH,'//div[@class="control-group"]/label[text()="活动类型："]/..//span[text()="签到活动"]/../input')
    # 红利活动类型-签到活动
    red_sign_avtiv = (By.XPATH,'//div[@class="control-group"]/label[text()="红利活动类型："]/..//span[text()="签到活动"]/../input')
    # 活动时间
    start_time = (By.XPATH,'//div[@class="control-group"]/label[text()="活动时间："]/../div/input[@id="start_date"]')
    end_time = (By.XPATH,'//div[@class="control-group"]/label[text()="活动时间："]/../div/input[@id="end_date"]')
    # 活动版本下拉框
    activ_select = (By.XPATH,'//div[@class="controls"]/select[@id="FVersion"]')
    # 审核内容复选框list
    audit_list = (By.XPATH,'//div[@class="control-group"]/label[text()="审核内容："]/../div/div[@class="ui-input-label-box"]/label[1]/input')
    # 选择游戏
    game = (By.XPATH,'//a[@class="btn btn-primary"][text()="选择游戏"]')
    # 选择游戏全选按钮
    game_pull_btn = (By.XPATH,'//div[contains(@data-bind,"isShowCompanyDialog()")][not(contains(@style,"display: none;"))]/div//div[@class="top"]/a[text()="全选"]')
    # 选择游戏确定按钮
    game_commit_btn = (By.XPATH,'//div[contains(@data-bind,"isShowCompanyDialog()")][not(contains(@style,"display: none;"))]/div//div[@class="foot"]/a[text()="确定"]')
    # 会员层级list
    vip_list = (By.XPATH,'//div[@class="controls"]/label/input[@class="fl mgc mgc-success"]')
    # 会员等级
    vip_lev = (By.XPATH,'//label[@class="control-label"][text()="会员等级："]/../select')
    # 活动保存按钮
    add_activ_btn = (By.XPATH,'//a[@id="btnAdd"][text()="保存"]')

    # test
    o = (By.XPATH,'//div[@class="d-content"]/span')








    @staticmethod
    def activ_type_loc(loc_name):
        '''
        活动类型/红利活动类型各活动按钮（除开签到活动）签到有两个
        :return:
        通用 == '//div[@class="controls"]//span[text()="红利活动"]/../input'
        '''
        locator = (By.XPATH,'//div[@class="controls"]//span[text()="{}"]/../input'.format(loc_name))
        return locator
    @staticmethod
    def activ_way_loc(loc_name):
        '''
        活动/参加/样式/领取/充值计算等方式，活动状态通用开关按钮
        活动图/内容图/手机活动图/手机活动内容图
        活动名称/申请时间间隔/领取次数限制/单个红利金额/单个红利投注流水/活动列表排序
        红包活动的红包总额/红包个数/单个红利投注流水
        :param loc_name:
        :return:
        '//div[@class="control-group"]/label[text()="参加方式："]/../div/input'
        '''
        locator = (By.XPATH,'//div[@class="control-group"]/label[text()="{}："]/../div/input'.format(loc_name))
        return locator

    @staticmethod
    def content_input(type_name,temp):
        '''
        审核内容7/8的累计金额/累计笔数通用
        :return:
        '''
        locator = (By.XPATH,'//div[@class="ui-input-label-box"]/label/span[text()="{}"]/../following-sibling::label//span[text()="累计"]/..//span[text()="{}"]/..//input'.format(type_name,temp))
        return locator
    @staticmethod
    def get_top_bet_redamount_input_loc(num,sub_num):
        '''
        充值流水活动/投注活动单个红利金额字段各个输入框定位 和chexkbox输入框
        :param num: 每行输入框list数值
        :param sub_num: input输入框的下标数值
        :return: 返回locator
        '//ul[@data-bind="foreach:list"]/li[1]/div/input'
        '''
        locator = (By.XPATH,'//ul[@data-bind="foreach:list"]/li[{}]/div/input[{}]'.format(num,sub_num))
        return locator
    @staticmethod
    def get_top_bet_activ_addbtn_loc(num):
        '''
        获取充值流水/投注活动每行的新增按钮
        :param num: 每行list数值
        :return:
        '//ul[@data-bind="foreach:list"]/li[2]//span/a[@class="btn btn-success"]'
        '''
        locator = (By.XPATH,'//ul[@data-bind="foreach:list"]/li[{}]//span/a[@class="btn btn-success"]'.format(num))
        return locator
# 充值流水活动多了一个充值计算方式
# 锦上添花没有活动名称输入框