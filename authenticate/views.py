from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required()


def home(request):
    return render(request, 'blog/dashboard.html')

# @login_required()


def photos(request):
    return HttpResponse('Photos')
