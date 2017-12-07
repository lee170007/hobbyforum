from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

def user_directory_path(instance, filename):
    return os.path.join('post', filename)

class Post(models.Model):
	user_id      = models.ForeignKey(User, on_delete = models.CASCADE)
	post_caption = models.CharField(max_length = 50)
	post_content = models.TextField(max_length = 250)
	post_image   = models.FileField(upload_to=user_directory_path,blank=True)
	post_date    = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.post_caption