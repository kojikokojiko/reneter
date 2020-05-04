from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def index(request):
    
    return render(request,'talking/index.html')


def neter(request):
    return render(request,'talking/neter.html')


def theme(request):
    return render(request,'talking/theme.html')
