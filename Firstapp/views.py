from django.shortcuts import render
from django.http import HttpResponse   #需要导入HttpResponse模块
from  django.http import  JsonResponse
from  Firstapp import sql
from django.db import models


def hello(request):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    return HttpResponse("Hello world ! ")    #不能直接字符串，必须是由这个类封装，此为Django规则



def loginWay(request):

     if request.method=='GET':
      name=request.GET.get('userName','ooo')  #["userName"]
      password=request.GET.get('password','kkk')#['password']
      print(name,password)
      # print(request)
      data=sql.messageInfo.objects.all()
      # area=sql.user.objects.create(userName='admin',password='123456')
      # print(data)
      return  HttpResponse(data[0].imgUrl)

     if request.method=="POST":

          data =sql.messageInfo.objects.values() #sql.user.objects.values("id","userName")
          nameA =request.POST.get('userName','ooo')
          passwordA =request.POST.get('password','kkk')#request.GET['password']   #
          # print(nameA,passwordA)

          #数据库中的数据转为json后传递给前端
          listA={}
          listA['list']=list(data)
          print(listA)
          return  JsonResponse(listA) #HttpResponse('{"name":"zhangsan","age":23,"email":"chentging@aliyun.com"}')

