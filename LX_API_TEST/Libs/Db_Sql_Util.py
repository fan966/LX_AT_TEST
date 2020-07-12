#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from DBUtils.PooledDB import PooledDB
import logging
from Config.Config import *
import pymysql
import pymssql
import decimal
class DB_Util:

    def __init__(self,db_sections):
        self.config = configparser.ConfigParser()
        self.config.read(Config().db_config_path,encoding='utf-8')
        self.db_host = self.config.get(db_sections,'db_host')
        self.db_port = self.config.get(db_sections, 'db_port')
        self.db_user = self.config.get(db_sections, 'db_user')
        self.db_password = self.config.get(db_sections, 'db_password')
        self.db_name = self.config.get(db_sections, 'db_name')
        try:
            if db_sections.startswith('MSSQL'):

                self.db_pool = PooledDB(creator=pymssql,mincached=2, maxcached=40,host=self.db_host,port=self.db_port,user=self.db_user,password=self.db_password,database=self.db_name,charset='utf8')

            elif db_sections.startswith('MYSQL'):
                self.db_pool = PooledDB(creator=pymysql, mincached=2, maxcached=40, host=self.db_host,port=self.db_port, user=self.db_user, password=self.db_password,database=self.db_name, charset='utf8')
            else:
                raise
        except Exception as err:
            logging.error('数据库类型暂不支持！{}'.format(err))

    def excute_sql(self,sql):
        conn = self.db_pool.connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        return data

    @staticmethod
    def sql_result_to_json(sql_result, fill_field_list, decimal_type_convert_to=1):
        """
        数据库查询结果转json
        :param sql_result: 数据库查询结果
        :param fill_field_list: 填充的json字段列表  如：["SessionId", "IsAgent"]
        :param decimal_type_convert_to: decimal类型的字段转换后的类型 (默认1: 转成float类型 2：int类型)
        """
        result_json_list = []

        if isinstance(sql_result, list) and isinstance(fill_field_list, list):

            for result in sql_result:
                json_dic = {}
                if len(fill_field_list) != len(result):
                    raise ValueError('查询结果和填充参数不匹配，无法转化！')
                for i in range(len(result)):
                    fill_field_value = result[i]
                    if isinstance(result[i], decimal.Decimal) and decimal_type_convert_to == 1:

                        fill_field_value = float(result[i])
                    if isinstance(result[i], decimal.Decimal) and decimal_type_convert_to == 2:

                        fill_field_value = int(result[i])
                    if isinstance(result[i], datetime.datetime):  # 如果数据库查询返回的值为时间类型，则需要转换

                        fill_field_value = str(result[i])

                    json_dic.update({fill_field_list[i]: fill_field_value})
                result_json_list.append(json_dic)
        else:
            raise TypeError('查询结果和填充参数必须为列表类型！')

        return result_json_list




if __name__ == '__main__':
    sql = '''select a.FID,a.FAccount,a.FCompanyID from TAccounts as a where a.FAccount='ttt11' and a.FCompanyID in (select a.FCompanyID from TAccounts as a where a.FAccount='csdqt')'''
    data = DB_Util(Config().db_config_name).excute_sql(sql)
    data = DB_Util.sql_result_to_json(data,['id','name','cid'])
    print(data)