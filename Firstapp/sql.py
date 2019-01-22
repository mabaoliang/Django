from django.db import models
import pymysql
import datetime


class user(models.Model):

     userName=models.CharField(max_length=255)
     password=models.CharField(max_length=255)


class messageInfo(models.Model):
     title=models.TextField()
     context=models.TextField()
     userName=models.CharField(max_length=255)
     acceptPeople=models.TextField()
     acceptPeopleIds=models.TextField()

class Image(models.Model):
    # url = models.TextField(null=True)
    image = models.ImageField(upload_to=str('image/{time}'.format(time=str(datetime.date.today().strftime("%Y%m/%d")))))
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    external_id=models.CharField(max_length=255,null=True)



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
    #         # 获取游标rn
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
    #         retu "删除数据失败"