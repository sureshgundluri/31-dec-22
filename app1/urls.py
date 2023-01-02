from django.urls import path
from app1.views import *
app_name='division'
urlpatterns=[
    path('operations/',operations,name='operations.html'),
]