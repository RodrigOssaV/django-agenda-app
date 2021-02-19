from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'main.html', {})

@unauthenticated_user
def mainPage(request):
    return render(request, 'welcome.html', {})