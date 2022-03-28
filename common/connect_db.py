import pymysql
from common.read_config import config



#从配置文件读取数据库连接信息
baseurl='/conf/product_center/env.ini'
config=config(baseurl)
user=config['DB']['USER']
port=int(config['DB']['PORT'])
host=config['DB']['HOST']
password=config['DB']['PASSWORD']


class Dbconnect():
    def __init__(self, database):
        self.db = pymysql.connect(database=database,host=host,port=port,user=user,password=password)
        self.cursor = self.db.cursor()

    def select(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # 删除，提交，修改语句
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        self.db.close()


if __name__ == '__main__':

    db = Dbconnect('product_center_2021')
    id = '226'

    result = db.select('SELECT * FROM `product` WHERE `id` = %s ' % id)
    print(result)
    db.close()
