from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return HttpResponse("This is employee profile page.")


