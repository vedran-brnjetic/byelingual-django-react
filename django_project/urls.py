"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from backend import views
from django.conf import settings

urlpatterns = [
    url(r'^authors/(?P<int:author_id>)/stories$', views.storiesByAuthor, name='storiesByAuthor'),
    url(r'^stories/(?P<int:story_id>)/acts$', views.actsByStory, name='actsByStory'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stories/$', views.storyList, name='storyList'),
    url(r'^users/$', views.userList, name='userList'),
    url(r'^authors/$', views.authorList, name='authorList'),
    url(r'^$', views.index, name='index'),

]
