from django.urls import path
from . import views

app_name='talking'

urlpatterns = [
    path('', views.index, name='index'),
    path('neter',views.neter,name='neter'),
    path('path',views.theme,name='theme'),
]