from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^backend/account/register',views.regUser),
    url(r'^backend/account/login',views.logUser),
    url(r'^backend/account/profile',views.profile),
    url(r'^backend/account/photo',views.photo),
    url(r'^backend/account/search',views.search)


]