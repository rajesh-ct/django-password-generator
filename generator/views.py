from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': 'rocketraja'})
    # return HttpResponse("Hello There")


def password(request):
    characters = list('abcdefghijklmopqrstuwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUWXYZ"))

    if request.GET.get('uppercase'):
        characters.extend(list("~!@#$%^&*"))

    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


# Create your views here.
def about(request):
    return render(request, 'generator/about.html', {'password': 'rocketraja'})
