# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
class TopUpLocator:
    @staticmethod
    def pmt_platform(platform_name_):
        """
        支付平台
        :param platform_name_:
        :return:
        """
        locator = (By.XPATH, r'//a[@href][text()="%s"]' % platform_name_)
        return locator

    # 未开通在线支付功能
    no_pay = (By.XPATH, '//div[@class="no-act-bg"]/p')

    # 银行卡支付通道
    pay_bank = (By.XPATH,'//a[text()="银行卡转账"]')
    # 支付宝通道
    pay_zfb = (By.XPATH,'//a[text()="支付宝"]')

    # 支付通道通用格式
    util = (By.XPATH,'//*[text()="{支付通道名称}"]')

    # 银行卡入款提示框
    tc_info = (By.XPATH,'//div[@i="title"][text()="提示"]')
    tc_button = (By.XPATH,'//button[@i="close"][@title="取消"]')
    # 充值指引提示框
    top_gui = (By.XPATH,'//div[@class="close"][contains(@data-bind,"click:showHelp")]')
    # 组合银行账号元素
    bank_list = (By.XPATH,'//a[@class="clo-item"][contains(@data-bind,"click: $parent.currentItemClick")]')

    # 存入金额
    amount1 = (By.XPATH,'//div[contains(@data-bind,"visible: currentStep()")][@style != "display: none;"]//input[contains(@data-bind,"textinput:amount")]')# $x('//input[contains(@data-bind,"textinput:amount, enable:")]')
    # 入款姓名
    dep_person1 =(By.XPATH,'//div[contains(@data-bind,"visible: currentStep()")][@style != "display: none;"]//input[contains(@data-bind,"realName,enable:")]')
    # 组合转账类型 （入款姓名2-如款金额2才会有选择转账类型）
    pay_type = (By.XPATH,'//div[@class="rbank-info other-info"]/div[@class="top clear"]/a[@class="clo-item"]')
    # 银行柜台
    bank_counter = (By.XPATH,'//input[@data-bind="textinput: belongsBank,enable: !hasSubmited(),"]')
    # 微信转账类型-弹窗处理
    weixin_tc = (By.XPATH,'//button[@class="ui-dialog-close"]')
    # 提交按钮
    submit_button = (By.XPATH,'//div[contains(@data-bind,"visible: currentStep()")][@style != "display: none;"]//div[@class="main-l"]//a[@class="rbank-btn"][text()="提交"]')

    # 线上支付 QQ钱包 百度 支付宝 京东 在线支付
    # 一组线上支付通道
    online_pay = (By.XPATH,'//a[@class="clo-item"]') # $x('//a[@class="clo-item"]')
    # 付款码数字
    pay_for_code = (By.XPATH,'//input[@data-bind="textinput:barCode"]') # $x('//input[@data-bind="textinput:barCode"]')
    # 充值金额
    online_amount = (By.XPATH,'//input[contains(@data-bind,"textinput: amount")]') # $x('//input[contains(@data-bind,"textinput: amount")]')
    # 获取快捷金额
    get_amount_val = (By.XPATH, '//a[contains(@data-bind,"parent.getAmountVal")]')# $x('//a[contains(@data-bind,"parent.getAmountVal")]')
    # 立即充值
    rbank_btn = (By.XPATH,'//a[@class="rbank-btn"]')# $x('//a[@class="rbank-btn"]')


    # 线下转账 【QQ钱包转账，云闪付转账，微信转账，支付宝转账】
    # 存入金额
    amount3 = (By.XPATH,'//input[contains(@data-bind,"textinput:offAmount, enable:!hasSubmit()")]')
    # 存入姓名
    dep_person3 = (By.XPATH,'//input[contains(@data-bind,"textinput: offRealName")]')
    # 立即充值按钮通用
    # 组合支付通道和线上通用


    # 存款优惠
    # 一组存款优惠按钮
    get_Preference = (By.XPATH,'//input[@name="getPreference1"]')
    # 获取存款优惠
    getPreference = (By.XPATH,'//label[@for="GetPreference"]')
    # 放弃存款优惠
    giveupPreference = (By.XPATH,'//label[@for="GetPreference"]')
    # 存款优惠文本
    preferenc_text = (By.XPATH,'//div[@i="content"]/p')





