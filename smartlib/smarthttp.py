import httplib


def post(host,url,body=None,headers={}):
    conn = httplib.HTTPConnection(host)
    conn.request("POST",url,body,headers)
    return conn.getresponse()