"""
__time__:2021/2/3 15:19
__author__:songshijie
"""

import pymysql
import pymysql.cursors
import json
import operator

class Operation_MYSQL:
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='',
            db='python',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        #创建游标
        self.cur = self.conn.cursor()

    def search_one(self, sql):
        # 执行语句
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result

    def is_equal_dict(self, dict_first, dict_second):
        if isinstance(dict_first, str):
            dict_first = json.loads(dict_first)
        if isinstance(dict_second, str):
            dict_second = json.loads(dict_second)
        result = operator.eq(dict_first, dict_second)
        return result
