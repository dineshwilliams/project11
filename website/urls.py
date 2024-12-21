from django.urls import path
from .views import *

app_name='website'

urlpatterns=[
      path('',home,name='home'),
      path('courses/',courses,name='courses'),
      path('bootcamp/',bootcamp,name='bootcamp'),
      path('request/',request,name='request'),
      path('sign/',sign,name='sign'),
]