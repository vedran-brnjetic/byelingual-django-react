from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Story, Player
from django.core import serializers
# Create your views here.

def index(request):
    return (HttpResponse("<h1>Koohii Onegai <b> ByeLingual</b></h1>"))

def userList(request):
    results = dict(users=list(Player.objects.values('public_name','language','avatar','user__email','user__first_name')))
    return (JsonResponse(results))

def storyList(request):
    results = dict(stories=list(Story.objects.values('name','image','description')))
    return (JsonResponse(results))

def authorList(request):
    results = dict(authors=list(Player.objects.values('public_name','language','avatar','user__email','authorBiography').get(isAuthor=true)))
