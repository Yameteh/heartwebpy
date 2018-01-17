import time

from datetime import datetime

from django.http import FileResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from polls import plog
from polls.protocal.clientreq import ImageRsp
from smartlib import smartfile
from smartlib import smartstring

IM_IMAGE_DIR = '/home/yaoguoju/heartweb/im/images/'
IM_AUDIO_DIR = '/home/yaoguoju/heartweb/im/audios/'

MIME_TYPE_JPG = 'image/jpeg'
MIME_TYPE_PNG = 'image/png'

MIME_TYPE_AMR = "audio/amr"

@csrf_exempt
def images(request,imagefile):
    print('images')
    if smartstring.equals_ingorecase(request.method,"POST"):
        smartfile.make_dirs(IM_IMAGE_DIR)
        contentType = request.META['CONTENT_TYPE']
        f = "image_"+str(int(time.time()))
        if smartstring.equals_ingorecase(contentType,MIME_TYPE_JPG):
            f = f + '.jpg'
        elif smartstring.equals_ingorecase(contentType,MIME_TYPE_PNG):
            f = f + '.png'
        with open(IM_IMAGE_DIR + f,"w") as image:
            image.write(request.body)
        rsp = ImageRsp(request.build_absolute_uri(request.get_full_path())+f)
        return HttpResponse(rsp.toJson())
    elif smartstring.equals_ingorecase(request.method, "GET"):
        file = IM_IMAGE_DIR + imagefile
        return FileResponse(open(file), "rb")



@csrf_exempt
def audios(request,audiofile):
    print('audios')
    if smartstring.equals_ingorecase(request.method, "POST"):
        smartfile.make_dirs(IM_AUDIO_DIR)
        contentType = request.META['CONTENT_TYPE']
        f = "audio_" + str(int(time.time()))
        if smartstring.equals_ingorecase(contentType, MIME_TYPE_AMR):
            f = f + '.amr'
        with open(IM_AUDIO_DIR + f, "w") as audio:
            audio.write(request.body)
        rsp = ImageRsp(request.build_absolute_uri(request.get_full_path()) + f)
        return HttpResponse(rsp.toJson())
    elif smartstring.equals_ingorecase(request.method, "GET"):
        file = IM_AUDIO_DIR + audiofile
        return FileResponse(open(file), "rb")


