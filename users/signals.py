from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)							#when a user is saved, then send this signal to receiver
def create_profile(sender, instance, created, **kwargs):	#this is the receiver which takes these arguments
	if created:
		Profile.objects.create(user=instance)				#if user is created, then create a Profile object with the user equal to the user instance that was created



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):	
	instance.profile.save()