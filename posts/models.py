from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField(max_length=1200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)	#if user is deleted, delete the posts as well
	date_posted = models.DateTimeField(default=timezone.now)	


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})