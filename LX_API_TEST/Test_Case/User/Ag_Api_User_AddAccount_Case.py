# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Libs.data_util import write_result_data_to_excel
from Libs.log_util import set_log
from Libs.data_util import get_case_from_excel
from ddt import ddt,data
from Verify.User.UserVerify import *
from Libs.Random_util import RandomUtil
from Libs.CheckRresult_Util import *
@ddt
class Ag_Api_User_AddAccount(unittest.TestCase):
    r = RandomUtil()
    run_rules_dic = Config().get_run_rules_config()
    run_rules_dic.update({'ScriptName': os.path.basename(__file__)})
    datas = get_case_from_excel(Config().case_data_file_path, ['User'], run_rules_dic, 'User')

    def setUp(self) -> None:
        logging.info('启动脚本文件 :  {}'.format(os.path.basename(__file__)))
        self.account = Config().get_ini_value('Global_ini', 'AgUserName')
        self.password = Config().get_ini_value('Global_ini', 'AgPwd')
        self.account_name = 'AGatuotest' + self.r.get_random_info_int(4)

    @data(*datas)
    def test_AG_uesr_login(self, datas):
        self._testMethodDoc = datas['CaseName']
        logging.info('开始执行用例： {} ( {} )'.format(self._testMethodDoc, self._testMethodName))
        logging.info('=======================调用【后台用户登录】接口====================================')
        LoginSessionID = ag_login_api(self.account,self.password)
        if not LoginSessionID:
            logging.error('后台登录失败，请检查！')
            raise
        logging.info('=======================调用【后台添加账户】接口====================================')
        datas['NewVerifParmsData'].update({"password":self.password})
        datas['NewVerifParmsData'].update({"accountName":self.account_name})
        datas['NewVerifParmsData'].update({"jsonlist":'[{"Key":"AccountRemark","Title":"用户备注","Value":""}]'})
        datas['NewVerifParmsData'].update({"UserKickbacks":'[{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09}]'})
        self.actual_result = http_api_requests('后台相关.添加账户',Headers={"LoginSessionID":LoginSessionID},server_host=Config().ag_host,
                                               NewVerifParmsData=datas['NewVerifParmsData'])
        self.expected_result = datas['ExpectResult']
        result = None
        try:
            check_result(self.expected_result, self.actual_result)
            result = 'pass'
            logging.info('新增用户（{}）成功'.format(self.account_name))
        except InterfaceVerifyError:
            result = 'false'
        finally:
            write_result_data_to_excel(Config().case_data_file_path, 'User', 'ID', datas['ID'], result)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    set_log()
    unittest.main()
    t = {"parentId":535658,"isAgent":True,"isBet":True,"isCommission":False,"agentType":2,"isVisitor":False,"hasContact":False,"accountName":"替换参数","nickName":"tt","password":"替换参数","status":1,"odds":-1,"hasUserContact":False,"FTransferAccountsType":0,"UseParentOdds":False,"IsTransferAccounts":0,"jsonlist":[{"Key":"AccountRemark","Title":"用户备注","Value":""}],"homeView":"haocai","agentAddBankCardConditions":"","memberAddBankCardConditions":"","UserKickbacks":[{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09},{"FKickback":0.09}]}
