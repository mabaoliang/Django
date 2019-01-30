from django.shortcuts import render
from django.http import HttpResponse   #需要导入HttpResponse模块
from  django.http import  JsonResponse
from  Firstapp import sql
import datetime
import  time
import  json
from  django.core import serializers

from django.db import models
from django.core.paginator import Paginator




def hello(request):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    return HttpResponse("Hello world ! ")    #不能直接字符串，必须是由这个类封装，此为Django规则




#登录方法
def loginWay(request):

     if request.method=='GET':
      # name=request.GET.get('userName','ooo')  #["userName"]
      # password=request.GET.get('password','kkk')#['password']
      # data = sql.user.objects.filter(userName='root',password='123456').values()
      # listA={}
      # listA["data"]=list(data) #json.loads(serializers.serialize("json", data))

      return HttpResponse('{"msg":"登录失败","status":"fail"}') #HttpResponse('请求方式错误') # #HttpResponse(data[0].imgUrl)

     if request.method=="POST":

         # data =sql.messageInfo.objects.values() #sql.user.objects.values("id","userName")
          nameA =request.POST.get('userName','')
          passwordA =request.POST.get('password','')
          if len(nameA)>0 and len(passwordA)>0:

             data=sql.User.objects.filter(userName=nameA,password=passwordA).values()


             if data.count()==1 :
                 listB={}
                 #序列化成json数据
                 listB["data"]=list(data)#json.loads(serializers.serialize("json", data))
                 listB["msg"]="登录成功"
                 listB["status"]="success"
                 return JsonResponse(listB)
             else:
                return HttpResponse('{"msg":"登录失败","status":"fail"}')
          else:
            return HttpResponse('{"msg":"登录失败","status":"fail"}')


#创建用户信息
def creatUser(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"用户创建失败","status":"fail"}')

    if request.method=="POST":

        username=request.POST.get('userName','')
        password=request.POST.get('password','123456')
        name=request.POST.get('name','')
        tele=request.POST.get('tele','')
        power=request.POST.get('power',0)
        superIds = request.POST.get('superiorIds', '')
        if len(username)>0 and len(name)>0 and len(tele)>0 and len(superIds)>0:

            sql.User.objects.create(userName=username,password=password,name=name,tele=tele,power=power,superiorIds=superIds)
            listA={}
            data=sql.User.objects.values()
            listA["msg"]="用户创建成功"
            listA["status"]="success"
            listA["data"]=list(data)

            return JsonResponse(listA) #HttpResponse('{"msg":"用户创建成功","status":"success"}')
        else:
          return HttpResponse('{"msg":"用户创建失败","status":"fail"}')
#查询用户信息
def selectUser(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"查询失败","status":"fail"}')

    if request.method=="POST":
            listA={}
            data=sql.User.objects.values()
            listA["msg"]="查询成功"
            listA["status"]="success"
            listA["data"]=list(data)
            return JsonResponse(listA) #HttpResponse('{"msg":"用户创建成功","status":"success"}')

#修改用户信息
def updateUser(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"修改用户失败","status":"fail"}')

    if request.method=="POST":
         username = request.POST.get('userName', '')
         password = request.POST.get('password', '')
         userId=request.POST.get('userId',0)
         name = request.POST.get('name', '')
         tele = request.POST.get('tele', '')
         power = request.POST.get('power', 0)
         superIds=request.POST.get('superiorIds','')
         if userId!=0:

            try:
             obj=sql.User.objects.get(userId=userId)
             if len(username):
                 obj.userName=username
             if len(name):
                 obj.name=name
             if len(password):
                 obj.password=password
             if len(tele):
                 obj.tele=tele
             if len(superIds):
                 obj.superiorIds = superIds
             obj.power=power
             obj.save()
             listA = {}
             data = sql.User.objects.values()
             listA["msg"] = "更新成功"
             listA["status"] = "success"
             listA["data"] = list(data)

             return JsonResponse(listA)  # HttpResponse('{"msg":"用户创建成功","status":"success"}')
            except Exception as e:
                return HttpResponse('{"msg":"修改用户失败","status":"fail"}')

         else:
             return HttpResponse('{"msg":"修改用户失败","status":"fail"}')
#删除用户
def deleteUser(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"用户权限获取失败","status":"fail"}')
    if request.method=="POST":
        userId=request.POST.get('userId',0)
        if userId !=0:

            try:
               sql.User.objects.filter(userId=userId).delete()
               listA = {}
               data = sql.User.objects.values()
               listA["msg"] = "删除成功"
               listA["status"] = "success"
               listA["data"] = list(data)
               return JsonResponse(listA)  #
            except Exception as e:

                return HttpResponse('{"msg":"用户下有项目有反馈所以用户删除失败","status":"fail"}')

        else:
            return HttpResponse('{"msg":"用户删除失败","status":"fail"}')


#人员的树
def  peopleTree(request):
       if request.method == "GET":
               return HttpResponse('{"msg":"创建项目失败","status":"fail"}')
       if request.method=="POST":

             data=sql.User.objects.all()
             listA={}
             listA["status"]="success"
             listA["msg"]="获取成功"
             for item in data:

                   dataA=sql.User.objects.filter(superiorIds=item.userId)#.values() #child
                   dataB=sql.User.objects.filter(userId=item.superiorIds)#.values() #super
                   # print(dataA)
                   # print(dataB)
                   if dataA.count()!=0 and dataB.count()==0:  #根节点
                       dic={}
                       dic["name"]=item.name
                       dic["userId"]=item.userId
                       arr=parsePople(dataA)
                       dic["data"]=arr
                       listA["data"]=dic
                       return JsonResponse(listA)
                       # for kkk in dataA:
                       #     dataC = sql.User.objects.filter(superiorIds=kkk.userId)  # .values() #child
                       #     for hhh in dataC:
                       #         dataD = sql.User.objects.filter(superiorIds=kkk.userId)  # .values() #child
                       #




             return HttpResponse('{"msg":"创建项目失败","status":"fail"}')


#解析组织架构
def parsePople(data):

      arr=[]
      for (i,item) in  enumerate(data):
            dic={}
            dic["name"]=item.name
            dic["userId"]=item.userId
            arr.append(dic)
            dataC = sql.User.objects.filter(superiorIds=item.userId)  # .values() #child
            if dataC.count()!=0:
                  dic["data"]=parsePople(dataC)
            if i==data.count()-1:

               return  arr




#添加项目
def creatProject(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"创建项目失败","status":"fail"}')
    if request.method=="POST":
        #(time.strptime('2019-09-18 16:48:09', '%Y-%m-%d %H:%M:%S'))
         projectName=request.POST.get('projectName','')
         projectStart=request.POST.get('projectStartTime','')
         projectEnd=request.POST.get('projectEndTime','')
         projectOn=request.POST.get('projectOnTime','')
         projectSiginId=request.POST.get('projectSingleId','')
         projectFunction=request.POST.get('projectFunction','')
         projectStatus=request.POST.get('projectStatus',0)
         if len(projectName)>0 and len(projectStart)>0 and len(projectEnd)>0 and len(projectOn)>0 and len(projectSiginId)>0 :
             # projectStart = time.strptime(projectStart, '%Y-%m-%d %H:%M:%S')
             # projectEnd = time.strptime(projectEnd, '%Y-%m-%d %H:%M:%S')
             # projectOn = time.strptime(projectOn, '%Y-%m-%d %H:%M:%S')
             # print(projectStart)
             sql.Project.objects.create(projectName=projectName,projectStartTime=projectStart,projectEndTime=projectEnd,projectOnTime=projectOn,projectSingleId=projectSiginId,projectFunction=projectFunction,projectStatus=projectStatus,user_id=int(projectSiginId))
             return HttpResponse('{"msg":"创建项目成功","status":"success"}')
         else:
            return HttpResponse('{"msg":"创建项目失败","status":"fail"}')


#修改项目
def updateProject(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"修改项目失败","status":"fail"}')
    if request.method=="POST":
        projectId=request.POST.get('projectId',0)
        projectName = request.POST.get('projectName', '')
        projectStart = request.POST.get('projectStartTime', '')
        projectEnd = request.POST.get('projectEndTime', '')
        projectOn = request.POST.get('projectOnTime', '')
        projectSiginId = request.POST.get('projectSingleId', '')
        projectFunction = request.POST.get('projectFunction', '')
        projectStatus = request.POST.get('projectStatus', 0)
        print(1313)
        if projectId!=0:

            try:
                obj=sql.Project.objects.get(projectId=projectId)
                if len(projectName)>0:
                  obj.projectName=projectName
                if len(projectStart)>0:
                  obj.projectStartTime=projectStart
                if len(projectEnd)>0:
                  obj.projectEndTime=projectEnd
                if len(projectOn)>0:
                  obj.projectOnTime=projectOn
                if len(projectSiginId)>0:
                     #项目添加人员
                  obj.projectSingleId=projectSiginId
                  obj.user_id=int(projectSiginId)
                if len(projectFunction)>0:
                  obj.projectFunction=projectFunction
                obj.projectStatus=projectStatus
                obj.save()
                return  HttpResponse('{"msg":"修改项目成功","status":"success"}')
            except Exception as e:

               return  HttpResponse('{"msg":"修改项目失败","status":"fail"}')
        else:
            return HttpResponse('{"msg":"修改项目失败","status":"fail"}')

#查询项目
def selectProject(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"查询项目失败","status":"fail"}')
    if request.method == "POST":
        userId=request.POST.get("userId",0)
        sendUserId=request.POST.get("projectSingleId",'0')
        if userId!=0 or len(sendUserId)>0:
            if userId!=0:
               data=sql.AssociatedPU.objects.filter(userId=userId) #sql.Project.objects.filter(user_id=userId).values()
               listA={}
               listA["msg"] = "获取成功"
               listA["status"] = "success"
              # listA["data"] = list(data)
               arrA=[]
               for item  in data:
                  dic={}
                  dic["projectId"]=item.project.projectId
                  dic["projectName"]=item.project.projectName
                  dic["projectSingleId"]=item.project.projectSingleId
                  dic["projectStatus"]=item.project.projectStatus
                  arrA.append(dic)


               listA["data"]=arrA

               return JsonResponse(listA)
            else:# HttpResponse('{"msg":"用户权限获取失败","status":"fail"}')
                data = sql.Project.objects.filter(projectSingleId=sendUserId).values()
                listA = {}
                listA["msg"] = "获取成功"
                listA["status"] = "success"
                listA["data"] = list(data)
                return JsonResponse(listA)
        else:
            return HttpResponse('{"msg":"查询项目失败","status":"fail"}')


#删除项目
def deleteProject(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"删除项目失败","status":"fail"}')
    if request.method == "POST":
        # userId=request.POST.get('projectSingleId','')
        projectId=request.POST.get('projectId',0)
        if projectId!=0:
             try:
                 sql.Project.objects.filter(projectId=projectId).delete()
                 return HttpResponse('{"msg":"项目删除成功","status":"success"}')
             except Exception as e:
                 return HttpResponse('{"msg":"项目已有开发人员无法删除","status":"fail"}')

        else:
            return HttpResponse('{"msg":"删除项目失败","status":"fail"}')


#用户添加回执
def creatFeek(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"添加回执失败","status":"fail"}')
    if request.method=="POST":
        userId=request.POST.get("userId",0)
        feedTime=datetime.datetime.now()
        projectId=request.POST.get("projectId",0)
        feedcom=request.POST.get("feedComplete","")
        feedunfinished=request.POST.get("feeedUnfinished","")
        feedConclusion=request.POST.get("feedConclusion","")
        feedProblem=request.POST.get("feedProblem","")
        sendUserId=request.POST.get("sendUserId",0)
        status=request.POST.get("status",0)
        if  userId!=0 and projectId!=0 and sendUserId!=0 :
            sql.Feedback.objects.create(userId=userId,user_id=userId,feedTime=feedTime,project_id=projectId,projectId=projectId,feedComplete=feedcom,feedUnfinished=feedunfinished,feedConclusion=feedConclusion,feedProblem=feedProblem,sendUserId=sendUserId,status=status)
            return HttpResponse('{"msg":"添加回执成功","status":"success"}')


#管理员添加反馈

def updateFeek(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"添加回执失败","status":"fail"}')

    if request.method=="POST":
         feekId=request.POST.get("feekId",0)
         userId = request.POST.get("userId", 0)
         feedTime =datetime.datetime.now()  #request.POST.get("feedSendTime", "")
         projectId = request.POST.get("projectId", 0)
         sendUserId = request.POST.get("sendUserId", 0)
         feedProblem = request.POST.get("feedProblem", "")
         status=request.POST.get("status",0)
         projectStatus=request.POST.get("projectStatus",0) #项目的完成情况

         if int(feekId)!=0 and int(userId)!=0  and int(projectId)!=0 and int(sendUserId)!=0 and len(feedProblem)>0 and int(status)==0:
              try:

                     obj=sql.Feedback.objects.get(feedId=feekId)
                     obj.feedProblem=feedProblem
                     obj.feedSendTime=feedTime
                     obj.status=1
                     obj.project.projectStatus=projectStatus
                     obj.save()
                     return HttpResponse('{"msg":"添加回执成功","status":"success"}')
              except Exception as e:

                       return HttpResponse('{"msg":"添加回执失败","status":"fail"}')


         else:
          return HttpResponse('{"msg":"添加回执失败","status":"fail"}')






#查询回执
def selectFeek(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"查询失败","status":"fail"}')
    if request.method=="POST":
        userId=request.POST.get("userId",0)
        sendUserId=request.POST.get("sendUserId",0)
        if userId!=0 or sendUserId!=0:

            if userId!=0: #普通用户
                 data=sql.Feedback.objects.filter(userId=userId)#values()
                 listA={}
                 listA["msg"] = "查询回执成功"
                 listA["status"] = "success"
                 arrA=[]
                 for item in data:
                      dic={}
                      objA = sql.User.objects.get(userId=item.sendUserId)
                      dic["sendName"] = objA.name
                      dic["sendUserId"]=objA.userId
                      dic["Name"]=item.user.name
                      dic["userId"]=item.user.userId
                      dic["feedId"]=item.feedId
                      dic["feedTime"]=item.feedTime
                      dic["projectId"]=item.project.projectId
                      dic["projectName"]=item.project.projectName
                      dic["projectStartTime"]=item.project.projectStartTime
                      dic["projectEndTime"]=item.project.projectEndTime
                      dic["projectOnTime"]=item.project.projectOnTime
                      dic["projectStatus"]=item.project.projectStatus
                      dic["projectFunction"]=item.project.projectFunction
                      dic["feedComplete"]=item.feedComplete
                      dic["feedUnfinished"]=item.feedUnfinished
                      dic["feedConclusion"]=item.feedConclusion
                      dic["feedProblem"]=item.feedProblem
                      dic["feedSendTime"]=item.feedSendTime
                      dic["status"]=item.status
                      arrA.append(dic)
                 listA["data"]=arrA
                 return  JsonResponse(listA)
            else: #管理员
             dataA=sql.Feedback.objects.filter(sendUserId=sendUserId)#.values()
             listB = {}
             listB["msg"] = "查询回执成功"
             listB["status"] = "success"
             arrB=[]
             for item in dataA:
                 dic={}
                 objA = sql.User.objects.get(userId=sendUserId)
                 dic["sendName"] = objA.name
                 dic["sendUserId"] = objA.userId
                 dic["Name"] = item.user.name
                 dic["userId"] = item.user.userId
                 dic["feedId"] = item.feedId
                 dic["feedTime"] = item.feedTime
                 dic["projectId"] = item.project.projectId
                 dic["projectName"] = item.project.projectName
                 dic["projectStartTime"] = item.project.projectStartTime
                 dic["projectEndTime"] = item.project.projectEndTime
                 dic["projectOnTime"] = item.project.projectOnTime
                 dic["projectStatus"] = item.project.projectStatus
                 dic["projectFunction"] = item.project.projectFunction
                 dic["feedComplete"] = item.feedComplete
                 dic["feedUnfinished"] = item.feedUnfinished
                 dic["feedConclusion"] = item.feedConclusion
                 dic["feedProblem"] = item.feedProblem
                 dic["feedSendTime"] = item.feedSendTime
                 dic["status"] = item.status
                 arrB.append(dic)
             listB["data"] = arrB #list(dataA)
             return JsonResponse(listB)

        else:
         return HttpResponse('{"msg":"查询失败","status":"fail"}')

#删除反馈

def  deleteFeek(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"删除反馈信息失败","status":"fail"}')


    if  request.method=="POST":
        feekId = request.POST.get("feekId", 0)

        if feekId!=0:
             try:
                  sql.Feedback.objects.get(feedId=feekId).delete()
                  return HttpResponse('{"msg":"删除反馈信息成功","status":"success"}')

             except Exception as e:
                 return HttpResponse('{"msg":"删除反馈信息失败","status":"fail"}')

        else:

            return HttpResponse('{"msg":"删除反馈信息失败","status":"fail"}')




#派单
def sendSingleWay(request):
     if request.method=="GET":

         return  HttpResponse('{"msg":"派单失败","status":"fail"}')

     if request.method=="POST":
          userId=request.POST.get("userIds",'')
          projectId=request.POST.get("projectId",0)
          status=request.POST.get("status",0)
          type=request.POST.get("type",0)
          time=datetime.datetime.now()
          sendyuserId=request.POST.get("sendUserId",0)
          if len(userId)>0 and projectId!=0 and sendyuserId!=0:

              arr=[]
              arrId=userId.split(',')
              for c in arrId:
                  if c!=",":
                    arr.append(c)

              for item in arr :
                  iid=int(item)
                  sql.AssociatedPU.objects.create(userId=iid,user_id=iid,project_id=projectId,projectId=projectId,type=type,statuse=status,sendUserId=sendyuserId,orderTime=time)
              return  HttpResponse('{"msg":"派单成功","status":"success"}')
          else:
           return HttpResponse('{"msg":"派单失败","status":"fail"}')

    #查询派单
def seledctSendsing(request):
    if request.method == "GET":
        return HttpResponse('{"msg":"查询派单失败","status":"fail"}')
    if request.method=="POST":
        userId=request.POST.get("userId",0)
        sendUserId=request.POST.get("sendUserId",0)
        #print((time.strptime('2019-09-18 16:48:09', '%Y-%m-%d %H:%M:%S')))
        if int(userId)!=0 or int(sendUserId)!=0:

          if userId!=0:  #普通用户查询
             dataA=sql.AssociatedPU.objects.filter(userId=userId)
             listA={}
             arrA=[]
             for item in dataA:
                 dic={}
                 objA=sql.User.objects.get(userId=item.sendUserId)
                 dic["sendName"]=objA.name
                 dic["type"]=item.type
                 dic["status"]=item.statuse
                 dic["userName"]=item.user.userName
                 dic["name"]=item.user.name
                 dic["userId"]=item.user.userId
                 dic["tele"]=item.user.tele
                 dic["superiorIds"]=item.user.superiorIds
                 dic["projectId"]=item.project.projectId
                 dic["projectName"]=item.project.projectName
                 dic["projectStartTime"]=item.project.projectStartTime.strftime("%Y-%m-%d %H:%M:%S")
                 dic["projectEndTime"]=item.project.projectEndTime.strftime("%Y-%m-%d %H:%M:%S")
                 dic["projectOnTime"]=item.project.projectOnTime.strftime("%Y-%m-%d %H:%M:%S")
                 dic["projectSingleId"]=item.project.projectSingleId
                 dic["projectStatus"]=item.project.projectStatus
                 arrA.append(dic)


             listA["data"]=arrA
             listA["msg"]="获取成功"
             listA["status"]="success"
             # print(listA)
             return JsonResponse(listA)
          else: #管理员查询
              dataA = sql.AssociatedPU.objects.filter(sendUserId=sendUserId)
              listA = {}
              arrA = []
              for item in dataA:
                  dic = {}
                  objB=sql.User.objects.get(userId=sendUserId)
                  dic["sendName"]=objB.name
                  dic["type"] = item.type
                  dic["status"] = item.statuse
                  dic["userName"] = item.user.userName
                  dic["name"] = item.user.name
                  dic["userId"] = item.user.userId
                  dic["tele"] = item.user.tele
                  dic["superiorIds"] = item.user.superiorIds
                  dic["projectId"] = item.project.projectId
                  dic["projectName"] = item.project.projectName
                  dic["projectStartTime"] = item.project.projectStartTime.strftime("%Y-%m-%d %H:%M:%S")
                  dic["projectEndTime"] = item.project.projectEndTime.strftime("%Y-%m-%d %H:%M:%S")
                  dic["projectOnTime"] = item.project.projectOnTime.strftime("%Y-%m-%d %H:%M:%S")
                  dic["projectSingleId"] = item.project.projectSingleId
                  dic["projectStatus"] = item.project.projectStatus
                  arrA.append(dic)


              listA["data"] = arrA
              listA["msg"] = "获取成功"
              listA["status"] = "success"
              # print(listA)
              return JsonResponse(listA)
        else:
          return HttpResponse('{"msg":"查询派单失败","status":"fail"}')



#转移派单
def modefiedOrder(request):

    if request.method=="GET":
             return HttpResponse('{"msg":"转移失败","status":"fail"}')


    if request.method=="POST":

         auId=request.POST.get('id',0)
         userId=request.POST.get('userId',0)
         if auId!=0 and userId!=0:
             try:
                 obj=sql.AssociatedPU.objects.get(associateId=auId)
                 obj.userId=userId
                 obj.user_id=userId
                 obj.statuse=1
                 return HttpResponse('{"msg":"转移成功","status":"success"}')
             except Exception as e:
                 return HttpResponse('{"msg":"转移失败","status":"fail"}')

         else:
            return HttpResponse('{"msg":"转移失败","status":"fail"}')



