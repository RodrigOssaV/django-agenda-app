from django.urls import path
from . import views

#localhost:8000/
urlpatterns = [
    path('', views.mainPage, name = 'mainPage'),
    path('home/', views.home, name = 'homePage'),
    
]