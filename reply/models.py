from django.db import models
from django.contrib.auth.models import User
from forumlist.models import Post
import os

# Create your models here.

def user_directory_path(instance, filename):
    return os.path.join('reply', filename)

class Reply(models.Model):
	user_id       = models.ForeignKey(User, on_delete = models.CASCADE)
	post_id       = models.ForeignKey(Post, on_delete = models.CASCADE)
	reply_content = models.TextField(max_length = 250)
	reply_image   = models.FileField(upload_to=user_directory_path,blank=True)
	reply_date    = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.reply_content