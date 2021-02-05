"""
__time__:2021/2/3 15:19
__author__:songshijie
"""

import pymysql

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
        )
        #创建游标
        self.cur = self.conn.cursor()

    def search_one(self, sql):
        # 执行语句
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

if __name__ == "__main__":
    opera = Operation_MYSQL()
    #insert into user_message(id,user,age,message) values (2,'zhangsan',16,'elsssss')
    result = opera.search_one("SELECT Host,User FROM mysql.user;")
    print(result)
