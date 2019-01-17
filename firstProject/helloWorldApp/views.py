from django.shortcuts import render
from django.http import HttpResponse
from helloWorldApp.models import Topic,AccessRecord,Webpage
# Create your views here.
def index(response):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(response,'index.html',context=date_dict)
def hello(response):
    return HttpResponse("<em>Hello World 2</em>")
def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'help.html',context=helpdict)