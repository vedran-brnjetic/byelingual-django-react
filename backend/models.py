from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Story(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='story_images',blank=True)

    def __str__(self):
        return self.name

    class Meta:
	verbose_name_plural = "stories"

class Player(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='player_profiles', default='NoProfileImage.jpg')
    public_name = models.CharField(max_length=30, default='user_public_name')
    language = models.CharField(max_length=3, default='en') #store just the country code and interpolate from that
    isAuthor = models.BooleanField(default=false)
    authorBiography = models.TextField(blank=true)

@receiver(post_save, sender=User)
def create_player_profile(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_player_profile(sender, instance, **kwargs):
    instance.player.save
