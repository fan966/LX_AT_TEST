# -*- coding:utf-8 -*-
import logging
from PO.pageaction.ag_home_action import *
from PO.pageobject.ag_yuebao_page import AgYueBaolocator
from PO.common.common_util import *
class AgYueBao(AgHome):

    def add_yuebao_activ(self,datas):
        #try:

            activ_name = get_random_info_str(5) + datas['activ_name']
            img1_path = get_project_path() + '\\Data\\activ\\image\\images1.jpg'  # 活动图片
            img2_path = get_project_path() + '\\Data\\activ\\image\\images2.jpg'  # 活动内容图片
            num = datas['input_data'].split('|')[0]
            input_value = util_str_convert_tupledata(datas['input_data'].split('|')[1])

            self.click_element(AgYueBaolocator.add_yuebao_btn)
            time.sleep(1)
            if self.check_element_displayed(AgYueBaolocator.yeb_activ_name):
                self.send_value(AgYueBaolocator.yeb_activ_name,activ_name)
            # 活动状态
            self.is_check_box(AgYueBaolocator.activ_status,datas['activ_temp'])

            self.driver.execute_script("arguments[0].removeAttribute('readonly')",self.find_element(AgYueBaolocator.start_time))
            self.driver.execute_script("arguments[0].removeAttribute('readonly')",self.find_element(AgYueBaolocator.end_time))
            self.find_element(AgYueBaolocator.start_time).clear()
            time.sleep(1)
            self.find_element(AgYueBaolocator.start_time).send_keys(datas['start_time'])
            time.sleep(1)
            self.find_element(AgYueBaolocator.end_time).clear()
            time.sleep(1)
            self.find_element(AgYueBaolocator.end_time).send_keys(datas['end_time'])
            time.sleep(1)
            # version
            self.get_drop_down_list(AgYueBaolocator.activ_version_select,datas['version'])
            self.find_element(AgYueBaolocator.activ_img).click()
            time.sleep(1)
            self.upload_file(img1_path)
            time.sleep(1)
            self.find_element(AgYueBaolocator.l_btn).click()
            self.find_element(AgYueBaolocator.phone_activ_img).click()
            time.sleep(1)
            self.upload_file(img2_path)
            time.sleep(1)
            if self.find_element(AgYueBaolocator.img_text):
                html_vale = self.find_element(AgYueBaolocator.img_text).get_attribute('innerHTML')
                if '完毕' or '成功' in html_vale:
                    logging.info('图片上传成功')
                else:
                    logging.error('图片上传失败，请检查')
            self.click_element(AgYueBaolocator.l_btn)
            # 选择代理
            self.click_element(AgYueBaolocator.activ_content)
            time.sleep(1)
            self.click_element(AgYueBaolocator.pull_btn)
            self.click_element(AgYueBaolocator.activ_content_btn)
            el = self.find_elements(AgYueBaolocator.vip_lev)
            for i in range(len(el)):
                el[i].click()

            # table输入
            for item,value in input_value:
                element_list = self.find_elements(AgYueBaolocator.get_table_list(item))
                for j in range(len(value)):
                    element_list[j].clear()
                    element_list[j].send_keys(value[j])
                if num > item:
                    self.click_element(AgYueBaolocator.get_table_addbtn(item))
            #富文本-域名限制
            #self.send_value(AgYueBaolocator.f_text,'test')
            # 电脑活动说明
            self.driver.switch_to.frame(self.find_element(AgYueBaolocator.activ_discription))
            self.send_value(AgYueBaolocator.activity_remark,datas['activ_discription'])
            self.swith_parent_iframe()
            # 手机活动说明
            self.driver.switch_to.frame(self.find_element(AgYueBaolocator.phone_activ_discription))
            self.send_value(AgYueBaolocator.activity_remark,datas['phone_activ_discription'])
            self.swith_parent_iframe()
            # 保存活动
            self.scroll_element(AgYueBaolocator.add_activ_btn)
            time.sleep(0.5)
            # 判断文本
            if self.find_element(AgYueBaolocator.img_text):
                html_vale = self.find_element(AgYueBaolocator.img_text).get_attribute('innerHTML')
                if '完毕' or '成功' in html_vale:
                    logging.info(html_vale)
                else:
                    logging.error(html_vale)
            time.sleep(3)
            return activ_name

        #except Exception as err:
            #logging.error(err)


