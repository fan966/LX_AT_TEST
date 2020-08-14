#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json,jsonpatch,jsonpointer
from Config.Config import *
from Libs.excel_util import ExcelUtil
import hashlib
import logging
import json
from Libs.common import *
def http_api_requests(interface_name,return_result = True,server_host = Config().ag_api_host,**replace_params):
    '''
    发送api请求
    :param interface_name: 接口模板匹配名称 如：登录注册.获取全局Token值
    :param server_host: api请求地址
    :param replace_params: 接口替换参数
    :return:
    '''

    # 根据传参接口名称获取接口模板
    if Config().case_data_from_type:
        interface_temp = get_interface_info_from_excel(interface_name)
    else:
        pass

    url = server_host + interface_temp['url']
    method = interface_temp['method']
    is_sing = interface_temp['is_sing']
    api_type = interface_temp['api_type']
    headers =  interface_temp['headers']
    cookies = {}
    body = interface_temp['body']
    is_encode = interface_temp['is_encode']


    if 'Headers' in replace_params:
        headers.update(replace_params['Headers'])
        cookies.update(replace_params['Headers'])

    # 循环替换接口模板中的值
    for key in replace_params['NewVerifParmsData'].keys():
        if key in body.keys():
            body = set_json_value(body,'/'+key,replace_params['NewVerifParmsData'][key])
        if replace_params['NewVerifParmsData'][key] == 'del':
            body.pop(key)

    # 判断是否需要签名
    if is_sing == 'yes':
        body = gen_common_sign(body)
    # 根据不同接口类型设置传入参数格式
    if api_type == 'HC':
        body = {'param':json.dumps(body)} if body else {}
    elif api_type == 'WEB':
        pass
    elif api_type == 'AG':
        pass
        #body = json.dumps(body) if body else {}
    else:
        body = json_convert_to_key_value(body) if body else {}  # 键值对
        headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
    # 判断接口传参是否需要转码
    encode = True
    if '后台相关添加账户' == is_encode:
        encode = True

    # 请求重试机制
    for retry_num in range(Config().requests_retry_num):
        if requests == Config().requests_retry_num - 1:
            logging.error('接口连续请求次数超过限制，请检查系统.....')
            raise ('接口连续请求次数超过限制，请检查系统.....')
        logging.info('调用： ' + interface_name)
        res_msg,http_res = base_requests_actions(url,method,body,headers=headers,cookies=cookies,encode=encode)

    # 判断url地址内是否附带Image 之类的图片请求字符，将接口返回的图片流保存为图片
    if "ImageCode" in url:
        from PIL import Image
        from io import BytesIO
        image = Image.open(BytesIO(http_res.content))
        image.save('randomImageCode.bmp')
    if return_result:
        return res_msg
    else:
        return http_res



def get_interface_info_from_excel(interface_name):
    '''
    excel获取接口模板
    :param interface_name: 匹配模板信息 如：登录注册.获取全局Token值
    :return:
    '''
    interface_list = interface_name.split('.')
    ModuleName = interface_list[0]

    InterfaceName = interface_list[1]

    interface_info = ExcelUtil(Config().interface_path,'interface').read_excel_addlist()


    if interface_info:
        for interface in interface_info:

            if interface['ModuleName'] == ModuleName and interface['InterfaceName'] == InterfaceName:
                #logging.info('获取匹配接口模板 ： ' + interface_info)

                interface_temp = {
                    "is_encode":interface['ModuleName']+interface['InterfaceName'],
                    "url":interface['URL'],
                    "method":interface['Method'],
                    "is_sing":interface['IsSign'],
                    "api_type":interface['ApiType'],
                    "headers":json.loads(interface['Headers']) if interface['Headers'] else {},
                    "body":json.loads(interface['Body']) if interface['Body'] else {}
                }
                logging.info('获取接口模板信息 ： '+' \n' + json.dumps(interface_temp,ensure_ascii=False,indent=4))

                return interface_temp
    else:
        logging.error('未匹配到任何模板数据，请检查')
        raise ('模板数据获取异常')


def set_json_value(json_string, json_pointer, json_value):
    """
    设置json值
    :param json_string:
    :param json_pointer:
    :param json_value:
    :return:
    """

    if isinstance(json_string, str):
        json_dict = json.loads(json_string)
    else:
        json_dict = json_string
    data = jsonpatch.apply_patch(json_dict, [{
                                           'op': 'add',
                                           'path': json_pointer,
                                           'value': json_value
                                               }])
    return data

def get_json_value(json_string, json_pointer, error_msg=''):
    """
    根据路径获取json值，路径为： / + key
    :param json_string: 获取值原体
    :param json_pointer: 获取路径 如：/code
    :param error_msg:
    :return:
    """
    if isinstance(json_string, str):
        json_dict = json.loads(json_string)
    else:
        json_dict = json_string

    try:
        result = jsonpointer.resolve_pointer(json_dict, json_pointer)
        return result
    except Exception:
        raise Exception('获取json信息异常: 【%s】' % error_msg)


def gen_common_sign(data):
    """
    生成接口签名
    :param data: 待签名的参数字典
    :return:
    """
    keys = data.keys()
    #keys.remove('Sign')
    keys = sorted(keys)
    signature = ''
    for k in keys:

        signature += k
    signature += Config().key

    m5 = hashlib.md5()
    m5.update(signature.encode('utf-8'))
    signature = m5.hexdigest()

    data['Merchantkey'] = signature

    return data

def base_requests_actions(url,method,body=None,  headers=None, cookies=None,encode=True):

    try:
        if encode:
            pass
        else:
            # 接口数据转码
            body = json.dumps(body)
            body = body.encode('utf-8')

        logging.info('请求url： ' + url)
        logging.info('请求消息体： ' + '\n' + json.dumps(body,ensure_ascii=False, indent=4))
        if method == 'GET':
            http_res = requests.get(url,params=body,headers=headers,cookies=cookies,verify=False)
        elif method == 'POST':
            http_res = requests.post(url=url,data=body,headers=headers,cookies=cookies,verify=False)
        else:
            logging.error('请求方法有误，请确认接口请求方式')
        if 'application/json' in http_res.headers['Content-Type']:
            res_msg = http_res.json()
            res_code = http_res.status_code
            res_msg = json.dumps(res_msg,ensure_ascii=False,indent=4)
        else:
            res_msg = http_res.text
            res_code = http_res.status_code
        logging.info('请求返回码 ： ' + str(res_code))
        logging.info('请求返回体 ： ' + '\n' + res_msg)
        # 次数返回体为text格式
        return res_msg,http_res
    except Exception as err:
        logging.error(err)







if __name__ == '__main__':
    #http_api_requests('密码相关.设置资金密码', NewVerifParmsData = {'IsReset':'true'})

    # body = {'age':'18','test':'11111'}
    # print(set_json_value(body,'/test','tihuan'))
    # body = {'Cache-Control': 'private', 'Content-Type': 'application/json; charset=utf-8', 'Server': 'Microsoft-IIS/10.0'}
    # temp = get_json_value(body,'/Contee','没有此key')
    # print(temp)
    url = 'http://gshcweb.add177.com/Home/login'
    #body = 'username=ttt1&password=8196658ecaeceb870d0ad3053dd579d2&validateCode='
    datas = {
        "username": "ttt1",
        "password": md5_encryption(md5_encryption('aaaa2222')),
        "validateCode": ""
    }
    headers = {"Content-Type":"application/json"}
    method = 'post'
    res,http_res = base_requests_actions(url,method,datas)
    print(res)
    print(type(res))
    #print(http_res)