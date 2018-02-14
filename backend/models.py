from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def author_story_directory_path(instance, filename):
    return 'author_{0}/story_{1}/act_{2}/{3}'.format(instance.story.author.id,instance.story.id,instance.title,filename)

# Create your models here.
class Story(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='story_images',blank=True)
    author = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
	verbose_name_plural = "stories"

class Player(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='player_profiles', default='NoProfileImage.jpg')
    public_name = models.CharField(max_length=30, default='user_public_name')
    language = models.CharField(max_length=3, default='en') #store just the country code and interpolate from that
    isAuthor = models.BooleanField(default=False)
    authorBiography = models.TextField(blank=True)

    def __str__(self):
        return self.public_name

@receiver(post_save, sender=User)
def create_player_profile(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_player_profile(sender, instance, **kwargs):
    instance.player.save


class Act(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to=author_story_directory_path, blank=True)
    main_language = models.CharField(max_length=3)
    foreign_language = models.CharField(max_length=3)
    soundtrack = models.FileField(upload_to=author_story_directory_path, blank=True)
    story = models.ForeignKey( Story, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Location(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to=author_story_directory_path, blank=True)
    act = models.ForeignKey(Act, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
