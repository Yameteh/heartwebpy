from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.utils.deprecation import MiddlewareMixin

from polls import plog
from polls.models import User
from smartlib import smartstring
import base64


class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        plog.i(request.get_host())

        path_info = request.META['PATH_INFO']
        plog.i(path_info)
        no_auth = path_info.endswith("backend/account/login") or \
                  path_info.endswith("backend/account/register")
        if not no_auth:
            authorization = request.META['HTTP_AUTHORIZATION']
            auth_info = base64.b64decode(authorization[5:])
            print(auth_info)
            pos = auth_info.index(':')
            if user_not_exist(auth_info[:pos],auth_info[pos+1:]):
                return HttpResponseNotFound(auth_info[:pos])



def user_not_exist(user_id,token):
    try:
        u = User.objects.get(id=user_id, token=token)
        return False
    except:
        return True
