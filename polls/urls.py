from django.conf.urls import url
from polls import views
from polls import views_im

urlpatterns = [
    url(r'^backend/account/register',views.regUser),
    url(r'^backend/account/login',views.logUser),
    url(r'^backend/account/profile',views.profile),
    url(r'^backend/account/photo',views.photo),
    url(r'^backend/account/search',views.search),
    url(r'^backend/message/images/(?P<imagefile>\w*.?\w*)',views_im.images),
    url(r'^backend/message/audios/(?P<audiofile>\w*.?\w*)',views_im.audios)
]