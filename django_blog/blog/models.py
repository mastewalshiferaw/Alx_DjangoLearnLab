from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils import timezone



class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk':self.pk})
  
class Comment(models.Model):
  post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
  content = models.TextField(max_length=500)

  created_at = models.DateTimeField(default=timezone.now)

  updated_at = models.DateTimeField(default=timezone.now)