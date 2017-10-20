from django.conf.urls import url
from django.contrib import admin
from . import views


app_name='projet'
urlpatterns = [
    url(r'^projet/', views.projet, name="projet"),
]