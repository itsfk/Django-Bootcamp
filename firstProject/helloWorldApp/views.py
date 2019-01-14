from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(response):
    my_dict = {'insert_me':"Hello i am from views.py"}
    return render(response,'index.html',context=my_dict)
def hello(response):
    return HttpResponse("<em>Hello World 2</em>")
def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'help.html',context=helpdict)