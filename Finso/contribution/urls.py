from django.conf.urls import url
from django.contrib import admin
from . import views


app_name='contribution_projet'
urlpatterns = [
    url(r'^contribution/(?P<id>\d+)/$', views.contributeprojet, name="contribute"),
]