from django.db import models
import pymysql


class user(models.Model):
     userID=models.BigIntegerField
     userName=models.CharField(max_length=255)
     password=models.CharField(max_length=255)


class messageInfo(models.Model):
     title=models.TextField()
     context=models.TextField()
     userName=models.CharField(max_length=255)
     userID=models.BigIntegerField
     acceptPeople=models.TextField()
     acceptPeopleIds=models.TextField()


    # # 数据库查询
    # def sql_select(self, sql):
    #
    #     try:
    #
    #         # 连接数据库
    #         conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='test',
    #                                charset='utf8')
    #         # 获取游标
    #         cur = conn.cursor()
    #         # 执行sql查询语句
    #         cur.execute(sqldjango_migrations)
    #         # 获取数据
    #         data = cur.fetchall()
    #
    #         # 关闭数据库连接
    #         cur.close()
    #         conn.close()
    #         # 数据返回
    #         return data
    #     except Exception as e:
    #         print(e)
    #         return "查询数据失败"
    #     finally:
    #         print()
    #
    # def sql_creat(self, sql):
    #
    #     try:
    #         # 连接数据库
    #         conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='test',
    #                                charset='utf8')
    #         # 获取游标
    #         cur = conn.cursor()
    #         # 执行sql查询语句
    #         cur.execute(sql)
    #         # 数据保存
    #         conn.commit()
    #         # 关闭数据库
    #         cur.close()
    #         conn.close()
    #         return "创建数据成功"
    #     except Exception as e:
    #         return "创建数据失败"
    #
    # def sql_update(self, sql):
    #
    #     try:
    #         # 连接数据库
    #         conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='test',
    #                                charset='utf8')
    #         # 获取游标
    #         cur = conn.cursor()
    #         # 执行sql查询语句
    #         cur.execute(sql)
    #         # 数据保存self,
    #         conn.commit()
    #         # 关闭数据库
    #         cur.close()
    #         conn.close()
    #         return "修改数据成功"
    #     except Exception as e:
    #         return "修改数据失败"
    #
    # def sql_delete(self, sql):
    #     try:
    #         # 连接数据库
    #         conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='test',
    #                                charset='utf8')
    #         # 获取游标
    #         cur = conn.cursor()
    #         # 执行sql查询语句
    #         cur.execute(sql)
    #         # 数据保存
    #         conn.commit()
    #         # 关闭数据库
    #         cur.close()
    #         conn.close()
    #         return "删除数据成功"
    #     except Exception as e:
    #         return "删除数据失败"