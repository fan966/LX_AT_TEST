#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

def main():
    try:
        # 建立数据库连接
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='aaaa2222',database='jing_dong',charset='utf8')
        # 建立游标对象
        cursor = conn.cursor()


        # 游标对象执行sql语句
        cursor.execute('select name from goods where id = 1')
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