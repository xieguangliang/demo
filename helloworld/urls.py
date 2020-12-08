from django.urls import re_path
from helloworld import views

urlpatterns = [
    re_path(r'^helloworld/$', views.first_view_func)
               ]

