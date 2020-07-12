#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymssql
def main():
    try:
        # 建立数据库连接

        conn = pymssql.connect(host='172.29.173.13',port=14332,user='user_query',password='lixin666',database='OfficialCash',charset='utf8')
        # 建立游标对象
        cursor = conn.cursor()


        # 游标对象执行sql语句
        cursor.execute('select * from TSecuritySettings as t where FAccountID=598059')
        # 获取值
        temp = cursor.fetchall()
        print(temp)
    except Exception as err:
        print(err)
    finally:
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()


if __name__ == '__main__':
    main()