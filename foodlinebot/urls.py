# 設定這個LINE Bot應用程式(APP - foodlinebot)的連結網址，所以在Django應用程式(APP)下建立一個urls.py檔案，加入以下的網址設定
from django.urls import path
from . import views
 
urlpatterns = [
    path('callback', views.callback)
]