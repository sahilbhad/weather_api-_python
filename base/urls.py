from django.urls import path
from .import views


urlpatterns=[
    path('',views.home),
    path('showdata',views.showdata,name='showdata'),
]