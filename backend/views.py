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
    query = User.objects.all().select_related('player')
    results = serializers.serialize("json", dict(query), fields=('first_name','email','nickname','avatar','language'))
    return (JsonResponse(results))

def storyList(request):
    results = dict(stories=list(Story.objects.values('name','image','description')))
    return (JsonResponse(results))
