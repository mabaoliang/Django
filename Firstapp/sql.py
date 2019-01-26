from django.db import models
import pymysql
import datetime


#用户表
class User(models.Model):

     userName=models.CharField(max_length=255)# 账号
     password=models.CharField(max_length=255)#密码
     name=models.CharField(max_length=255) #姓名
     userId=models.AutoField(primary_key=True) #id
     tele=models.CharField(max_length=255) #手机号
     superiorIds=models.CharField(max_length=255,null=True,blank=True) #上级ID
     power=models.IntegerField() #权限 1有 0无

#项目表
class Project(models.Model):
     projectId=models.AutoField(primary_key=True) #ID
     projectName=models.CharField(max_length=255) #项目名
     projectStartTime=models.DateTimeField(auto_now=True)#开始时间
     projectEndTime=models.DateTimeField(auto_now=True)#结束时间
     projectOnTime=models.DateTimeField(auto_now=True) #上线时间
     projectSingleId=models.CharField(max_length=255) #派单人
     projectFunction=models.TextField(null=True,blank=True) #功能模块
     projectStatus=models.IntegerField(default=0) #状态 0未完成 1完成
     user=models.ForeignKey('User',on_delete=models.CASCADE) #用户表

#反馈表
class Feedback(models.Model):
     feedId=models.AutoField(primary_key=True) #ID
     userId=models.IntegerField() #用户ID
     sendUserId = models.IntegerField(null=True)  # 派单人员id
     feedTime=models.DateTimeField(auto_now=True)#反馈时间
     projectId=models.IntegerField()#项目id
     feedComplete=models.TextField(null=True,blank=True)#完成
     feedUnfinished=models.TextField(null=True,blank=True) #未完成
     feedConclusion=models.TextField(null=True,blank=True) #工作总结
     feedProblem=models.TextField(null=True,blank=True) #问题
     user=models.ForeignKey('User',on_delete=models.CASCADE) #用户表
     project=models.ForeignKey('Project',on_delete=models.CASCADE) #项目表

#用户与项目的关联表
class AssociatedPU(models.Model):
     associateId=models.AutoField(primary_key=True) #id
     userId=models.IntegerField(null=True,blank=True) #用户ID
     sendUserId=models.IntegerField(null=True) #派单人员id
     projectId=models.IntegerField(null=True,blank=True) #项目
     statuse=models.IntegerField(default=0) #状态
     type=models.IntegerField(default=0) #类型
     user = models.ForeignKey('User',on_delete=models.CASCADE)  # 用户表
     project = models.ForeignKey('Project',on_delete=models.CASCADE)  # 项目表
















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