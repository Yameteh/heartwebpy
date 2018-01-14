import json
import hashlib
import os

import redis
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse,FileResponse

from polls.models import User
from polls.protocal.clientreq import RegMsg, RegRsp, ProfileRsp, ProfileReq,SearchRsp, LogRsp
from smartlib import smartstring

@csrf_exempt
def regUser(request):
    rsp = RegRsp(200, -1)
    if smartstring.equals_ingorecase(request.method,"POST"):
        regmsg = RegMsg()
        regmsg.parse(request.body)
        if not hasUser(regmsg.account):
            u = User()
            u.account = regmsg.account
            u.password = regmsg.password
            u.token = hashlib.sha1(os.urandom(24)).hexdigest()
            u.save()
            rsp.Code = 0
            rsp.Userid = u.id
            return HttpResponse(rsp.toJson())
        else:
            rsp.Code = 100
            rsp.Userid = -1
            return HttpResponse(rsp.toJson())
    else:
        return HttpResponse(rsp.toJson())


@csrf_exempt
def logUser(request):
    rsp = LogRsp(200,-1,"")
    if smartstring.equals_ingorecase(request.method,"POST"):
        logMsg = RegMsg()
        logMsg.parse(request.body)
        u = checkUser(logMsg.account,logMsg.password)
        if u is not None:
            rsp.code = 0
            rsp.userid = u.id
            rsp.token = u.token
            saveUserToRedis(rsp.userid,rsp.token)
        return HttpResponse(rsp.toJson())
    else:
        return HttpResponse(rsp.toJson())


@csrf_exempt
def profile(request):
    rsp = ProfileRsp()
    if smartstring.equals_ingorecase(request.method,"POST"):
        req = ProfileReq()
        req.parse(request.body)
        u = getUserById(req.id)
        if u is not None:
            u.nick = req.nick
            u.sex = req.sex
            u.signature = req.signature
            u.save()
            rsp.account = u.account
            rsp.code = 0
            rsp.nick = u.nick
            rsp.sex  = u.sex
            rsp.signature = u.signature
            rsp.curbind = u.curbind
        return HttpResponse(rsp.toJson())
    elif smartstring.equals_ingorecase(request.method,"GET"):
        id = request.GET.get("user",-1)
        u = getUserById(id)
        if u is not None:
            rsp.code = 0
            rsp.nick = u.nick
            rsp.signature = u.signature
            rsp.sex = u.sex
            rsp.curbind = u.curbind
            rsp.account = u.account
        return HttpResponse(rsp.toJson())

@csrf_exempt
def photo(request):
    if smartstring.equals_ingorecase(request.method,"POST"):
        userid =  request.POST["user"]
        headphoto = request.FILES["headphoto"]
        handleUploadFile(userid,headphoto)
        return HttpResponse("")
    elif smartstring.equals_ingorecase(request.method,"GET"):
        userid = request.GET["user"]
        filename = "headphoto/"+userid+"_head.png"
        return FileResponse(open(filename),"rb")

@csrf_exempt
def search(request):
    if smartstring.equals_ingorecase(request.method,"POST"):
        userid = request.body
        users = User.objects.all()
        searchs = [SearchRsp(u.id,u.account,u.nick,u.sex,u.signature) for u in users]
        rsp = json.dumps([s.__dict__ for s in searchs])
        return HttpResponse(rsp)



def handleUploadFile(userid,headphoto):
    with open("headphoto/"+userid+"_head.png",'wb+') as destination:
        for chunk in headphoto.chunks():
            destination.write(chunk)
        

def saveUserToRedis(userid,usertoken):
    r = redis.StrictRedis("127.0.0.1")
    key = "access_token_"+usertoken
    field = {"user_id":"","app_id":1}
    field["user_id"] = userid
    r.hmset(key,field)

def getUserById(id):
    try:
        u = User.objects.get(id=id)
        return u
    except:
        return None

def hasUser(account):
    try:
        User.objects.get(account=account)
        return True
    except :
        return False

def checkUser(account,password):
    try:
       u = User.objects.get(account=account,password=password)
       return u
    except:
       return None