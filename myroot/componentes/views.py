from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main.html', {})

def mainPage(request):
    return render(request, 'welcome.html', {})