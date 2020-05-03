# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
from PO.common.common_util import *
class UserCenterPage:
    '''
    登录成功后页面元素
    '''
    # 公告弹窗
    user_ptgg = (By.XPATH,'//div[@i="title"][text()="平台公告"]')
    usercenter_board = (By.XPATH,'//div[@i="title"][text()="平台公告"]/../button[@i="close"]')
    # 签到活动弹窗
    user_actvi = (By.XPATH,'//div[@i="title"][text()="签到活动"]')
    usercenter_actviboard = (By.XPATH,'//div[@i="title"][text()="签到活动"]/../button[@i="close"]')
    # 彩票大厅
    lottery = (By.XPATH,'//a[@class= "lottery"]')
    # 综合游戏
    zhyx = (By.XPATH,'//a[@class= "zhyx-a"]')
    # 用户中心
    userCenter = (By.XPATH,'//a[@class= "UserCenter"]')
    #优惠活动
    activity = (By.XPATH,'//a[@class= "Activity"]')
    # 平台公告
    announncement = (By.XPATH,'//a[@class= "Announncement"]')
    # 手机下注
    mobile = (By.XPATH,'//a[@class= "mobile"]')
    # 首页充值
    home_deposit = (By.XPATH,'//a[contains(@class,"btn-navacc-deposit")]')
    # 首页提款
    home_withdraw = (By.XPATH,'//a[@class= "btn btn-navacc-withdraw"]')
    # 用户中心充值
    user_deposit = (By.XPATH, '//a[@title="在线存款"]')
    # 用户中心提款
    user_withdraw = (By.XPATH, '//a[@title="在线取款"]')
    # 登出
    log_out = (By.XPATH,'//a[@class= "btn btn-login-out"]')

    # 用户中心log
    usercenter_log = (By.XPATH,'//div[@class="logo-wrap"]')
    # 首页log
    home_log = (By.XPATH,'//div[@class="header-main"]')
    # 游戏页面通用-开奖结果
    game_reault = (By.XPATH,'//a[text()="开奖结果"]')



    #用户中心通用弹窗定位
    msg_prompt = (By.XPATH,'//table[@class="ui-dialog-grid"]')


    #通用弹窗文本定位/有span
    prompt_text = (By.XPATH,'//div[@i="content"]//span[@class]')

    # 通用弹窗文本定位/无span
    prompt_texts = (By.XPATH,'//div[@i="content"][@class="ui-dialog-content"]')


    #弹窗通用X按钮
    prompt_close = (By.XPATH,'//button[@class="ui-dialog-close"]')


    #弹窗通用确定 / 提交按钮
    msg_prompt_sbmit = (By.XPATH,'//button[@i-id="ok"]')

    # 线下转账弹窗文本
    offline_text = (By.XPATH,'//span[@class="succeed"][text()="您的订单已提交成功, 此公司没有提供二维码, "]')
    #银行卡转账文本/有转账类型的tc
    bank_tc_text = (By.XPATH,'//div[@i="content"]/span[@class]/div[contains(@style,"text-align")]/span[1]')


    @staticmethod
    def get_officialgame_url(id):
        '''
        根据官方游戏id获取url
        :param id:
        :return:
        '''
        url = ('http://csdqthcweb.lx901.com/OffcialOtherGame/Index/{}'.format(id))
        return url

    @staticmethod
    def get_traditiongame_url(id):
        '''
        根据信用游戏id获取url
        :param id:
        :return:
        '''
        url = ('http://csdqthcweb.lx901.com/OtherGame/Index/{}'.format(id))
        return url




if __name__ == "__main__":
    report_path = get_project_path() + '\\Report\\test_report\\Auto_test_reporting.html'
    print(report_path)













# following-sibling   随后的兄弟元素
# preceding-sibling  之前的兄弟元素