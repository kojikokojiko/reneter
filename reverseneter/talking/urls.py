from django.urls import path
from . import views

app_name='talking'


# 第一引数の後に/を追加するのを忘れないように
urlpatterns = [
    path('', views.index, name='index'),
    path('neter/',views.neter,name='neter'),
    path('theme/',views.theme,name='theme'),
]