from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Story, Player, Act, Location
from django.core import serializers
# Create your views here.

def index(request):
    return (HttpResponse("<h1>Koohii Onegai <b> ByeLingual</b></h1>"))

def userList(request):
    results = dict(users=list(Player.objects.values('public_name','language','avatar','user__email','user__first_name')))
    return (JsonResponse(results))

def storyList(request):
    results = dict(stories=list(Story.objects.values('name','image','description','author__public_name')))
    return (JsonResponse(results))

def authorList(request):
    results = dict(authors=list(Player.objects.filter(isAuthor=True).values('public_name','language','avatar','user__email','authorBiography')))
    return (JsonResponse(results))

def storiesByAuthor(request, author_id):
    results = dict(
        stories=list(
            Story.objects.filter(author__id=author_id).values(
                'name',
                'image',
                'description'
            )
        )
    )

def actsByStory(request, story_id):
    results = dict (
        acts = list(
            Act.objects.filter(story__id=story_id).values(
                'title',
                'cover_image',
                'main_language',
                'foreign_language'
                'soundtrack'
            )
        )
    )
