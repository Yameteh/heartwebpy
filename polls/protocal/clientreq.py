import json

class RegMsg(object):

    def __init__(self):
        self.account = ""
        self.password = ""

    def parse(self,data):
        d = json.loads(data)
        self.account = d['account']
        self.password = d['password']


class RegRsp(object):

    def __init__(self,code,uid):
        self.code = code
        self.userid = uid

    def toJson(self):
        return json.dumps(self.__dict__)

class LogRsp(object):

    def __init__(self,code,uid,token):
        self.code = code
        self.userid = uid
        self.token = token

    def toJson(self):
        return json.dumps(self.__dict__)

class ProfileReq(object):

    def parse(self,data):
        d = json.loads(data)
        self.id = d['userid']
        self.nick = d['nick']
        self.signature = d['signature']
        self.sex = d['sex']

class ProfileRsp(object):

    def __init__(self,code=200,nick="",sign="",sex="",curbind=-1,account=""):
        self.code = code
        self.nick = nick
        self.signature = sign
        self.sex = sex
        self.curbind = curbind
        self.account = account

    def toJson(self):
        return json.dumps(self.__dict__)

class SearchRsp(object):

    def __init__(self,id,account,nick,sex,sign):
        self.userid = id
        self.account = account
        self.nick = nick
        self.sex = sex
        self.sign = sign


class ImageRsp(object):

    def __init__(self,url):
        self.src_url = url


    def toJson(self):
        return json.dumps(self.__dict__)


