from django.conf.urls import url
from helloWorldApp import views
urlpatterns = [
    url(r'^$',views.help,name='help'),
]