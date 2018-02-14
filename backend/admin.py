from django.contrib import admin
from .models import Story, Player, Act, Location
# Register your models here.

admin.site.register(Story)
admin.site.register(Player)
admin.site.register(Act)
admin.site.register(Location)
