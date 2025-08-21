from django.db import models
from django.conf import settings

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts") 
  title = models.CharField(max_length=200) 
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name="comments_made")
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Commented by {self.author}"
  
class Like(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_posts')

  class Meta:
    unique_together = ('post', 'user')

  def __str__(self):
    return f"{self.user.username} liked '{self.post.title}"