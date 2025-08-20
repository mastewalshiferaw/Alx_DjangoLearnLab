from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  bio = models.TextField(blank=True, null=True)
  profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
  
  following = models.ManyToManyField("self", symmetrical=False, related_name="followers", blank=True)

  def follow(self, user):
    if user != self:
      self.following.add(user)
  def unfollow(self, user):
    self.following.remove(user)
  def is_following(self, user):
    return self.following.filter(id=user.id).exists()

  def __str__(self):
    return self.username



