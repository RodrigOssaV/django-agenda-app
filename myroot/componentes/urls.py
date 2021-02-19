from django.urls import path
from . import views

#localhost:8000/
urlpatterns = [
    #path('', views.home, name = 'home'),
    path('', views.mainPage, name = 'mainPage')
]