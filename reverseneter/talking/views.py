from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def index(request):
    context={'air':''}
    return render(request,'talking/index.html',context)