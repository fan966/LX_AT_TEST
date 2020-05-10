# -*- coding:utf-8 -*-
from PO.pageaction.ag_home_action import *
from PO.pageobject.activ_page import ActivLocator
from PO.common.common_util import *
from selenium.webdriver.common.by import By
import logging
class AgActiv(AgHome):




    def test_activ(self,datas):
        logging.info('【INFO】【功能检查】【{}】'.format(datas['red_sign_avtiv']))
        activ_name =get_time_str()+'自动化' + datas['activ_name'] # 活动名称
        activ_type = datas['activ_type'] # 活动类型
        red_sign_avtiv = datas['red_sign_avtiv'] # 红利活动类型
        img1_path = get_project_path() + '\\Data\\activ\\image\\images1.jpg' # 活动图片
        img2_path = get_project_path() + '\\Data\\activ\\image\\images2.jpg' # 活动内容图片
        content = datas['content'].split(',') # 审核内容
        # 条件配置勾选方法
        AgHome(self.driver).condition_set()
        # 添加活动按钮
        time.sleep(1)
        self.find_element(ActivLocator.add_activ).click()
        # 活动类型
        self.is_check_box(ActivLocator.activ_type_loc(activ_type),'on')
        # 红利活动类型
        self.is_check_box(ActivLocator.activ_type_loc(red_sign_avtiv),'on')
        # 活动方式
        self.is_check_box(ActivLocator.activ_way_loc('活动方式'),datas['type'])
        # 充值计算方式
        if '充值流水活动' in datas['red_sign_avtiv']:
            self.is_check_box(ActivLocator.activ_way_loc('充值计算方式'),datas['top_type'])
        # 领取方式
        self.is_check_box(ActivLocator.activ_way_loc('领取方式'),datas['recc_type'])
        # 参加方式
        if activ_type != '页面活动':
            self.is_check_box(ActivLocator.activ_way_loc('参加方式'),datas['partic_type'])
        # 活动名称
        self.send_value(ActivLocator.activ_way_loc('活动名称'),activ_name)
        # 活动状态
        self.is_check_box(ActivLocator.activ_way_loc('活动状态'),datas['activ_temp'])
        # 活动时间
        time.sleep(1)
        self.remove_readonly('id','start_date')
        self.remove_readonly('id','end_date')
        print(datas['start_time'])
        print(datas['end_time'])
        self.find_element(ActivLocator.start_time).clear()
        self.find_element(ActivLocator.start_time).send_keys(datas['start_time'])
        self.find_element(ActivLocator.end_time).clear()
        self.find_element(ActivLocator.end_time).send_keys(datas['end_time'])
        # 申请时间间隔
        self.send_value(ActivLocator.activ_way_loc('申请时间间隔'),datas['inter_time'])
        # 活动版本
        # 活动图片
        self.get_drop_down_list(ActivLocator.activ_select,datas['version'])
        if datas['version'] == '全部版':
            self.find_element(ActivLocator.activ_way_loc('活动图')).click()
            time.sleep(1)
            self.upload_file(img1_path)
            self.find_element(ActivLocator.activ_way_loc('活动内容图')).click()
            time.sleep(1)
            self.upload_file(img2_path)
            self.find_element(ActivLocator.activ_way_loc('手机活动图')).click()
            time.sleep(1)
            self.upload_file(img1_path)
            self.find_element(ActivLocator.activ_way_loc('手机活动内容图')).click()
            time.sleep(1)
            self.upload_file(img2_path)
        elif datas['version'] == '电脑版活动':
            self.find_element(ActivLocator.activ_way_loc('活动图')).click()
            time.sleep(1)
            self.upload_file(img1_path)
            self.find_element(ActivLocator.activ_way_loc('活动内容图')).click()
            time.sleep(1)
            self.upload_file(img2_path)
        elif datas['version'] == '手机版活动':
            self.find_element(ActivLocator.activ_way_loc('手机活动图')).click()
            time.sleep(1)
            self.upload_file(img1_path)
            self.find_element(ActivLocator.activ_way_loc('手机活动内容图')).click()
            time.sleep(1)
            self.upload_file(img2_path)

        # 样式方式
        self.is_check_box(ActivLocator.activ_way_loc('样式方式'),datas['style'])
        # 审核内容
        el = self.find_elements(ActivLocator.audit_list)
        #审核附加值
        contrnt_value = datas['content_input'].split(',')
        for i in range(len(content)):
            el[int(content[i])-1].click()
            if int(content[i])-1 == 6:
                self.send_value(ActivLocator.content_input('当日有充值','金额'),contrnt_value[0])
                self.send_value(ActivLocator.content_input('当日有充值', '笔数'), contrnt_value[1])
            elif int(content[i])-1 == 7:
                self.send_value(ActivLocator.content_input('历史有充值', '金额'), contrnt_value[0])
                self.send_value(ActivLocator.content_input('历史有充值', '笔数'), contrnt_value[1])
        # 判断活动类型
        if red_sign_avtiv in "充值流水活动,投注活动":
            self.top_bet_activ_input_util(datas)
        if red_sign_avtiv in "注册活动,登录活动":
            self.register_login_activ_input_util(datas)

        # 选择游戏
        self.click_element(ActivLocator.game)
        time.sleep(1)
        self.click_element(ActivLocator.game_pull_btn)
        self.click_element(ActivLocator.game_commit_btn)
        # 会员层级
        element = self.find_elements(ActivLocator.vip_list)
        for i in range(len(element)):
            if i % 3 == 0:
                element[i].click()
        # 会员等级
        self.get_drop_down_list(ActivLocator.vip_lev,datas['vip_lev'])
        # 活动列表排序
        self.send_value(ActivLocator.activ_way_loc('活动列表排序'),datas['activ_list'])
        # 保存按钮
        self.scroll_element(ActivLocator.add_activ_btn)
        # 判断文本
        flag = self.utli_pop_tc('成功')
        return flag

    def top_bet_activ_input_util(self,datas):
        '''
        充值流水活动/投注活动公共输入方法
        :param datas:excel读取数据
        :return:
        '''
        num_value = datas['top_bet_activ'].split('|')[0] # 获取输入总行数
        # [('1', ['100', '1000', '2', '5']), ('2', ['1000', '10000', '2', '10']), ('3', ['10000', '100000', '2', '15'])] 输入数据
        input_value = util_str_convert_tupledata(datas['top_bet_activ'].split('|')[1])
        for item_num,value in input_value:
            num = 0
            for j in range(len(value)):# changdu 6
                num += 1
                self.send_value(ActivLocator.get_top_bet_redamount_input_loc(item_num,num),value[j])
                # 判断下个input是否为checkbox，是则点击
                if self.check_element_displayed(ActivLocator.get_top_bet_redamount_input_loc(item_num,num+1)):
                    # 获取属性type是否为chenkbox，是则click
                    attr = self.find_element(ActivLocator.get_top_bet_redamount_input_loc(item_num,num+1)).get_attribute('type')
                    if attr == 'checkbox':
                        self.is_check_box(ActivLocator.get_top_bet_redamount_input_loc(item_num,num+1),'on')
                        num += 1

            # 判断总行数大于行数则根据行数点击新增按钮
            if int(num_value) > int(item_num):
                self.click_element(ActivLocator.get_top_bet_activ_addbtn_loc(item_num))
        time.sleep(3)

    def register_login_activ_input_util(self,datas):
        '''
        注册活动/登录活动公共输入方法
        :return:
        '''
        self.send_value(ActivLocator.activ_way_loc('领取次数限制'),datas['rec_num'])
        self.send_value(ActivLocator.activ_way_loc('单个红利金额'),datas['red_amount'])
        self.send_value(ActivLocator.activ_way_loc('单个红利投注流水'),datas['run_water'])





