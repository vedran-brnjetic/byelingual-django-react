from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Story
from django.core import serializers
# Create your views here.

def index(request):
    return (HttpResponse("<h1>Koohii Onegai <b> ByeLingual</b></h1>"))

def userList(request):
    results = dict(users=list(User.objects.values('first_name','last_name','email')))
    return (JsonResponse(results))

def storyList(request):
    results = dict(stories=list(Story.objects.values('name','image','description')))
    return (JsonResponse(results))
