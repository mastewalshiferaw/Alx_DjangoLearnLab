from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
  recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_recieved')
  actor = models.ForeiggnKey(User, on_delte=models.CASCADE, related_name='notification_set')
  verb = models.CharField(max_length=200)
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  target = GenericForeignKey("content_type", "object_id")

timestamp = models.DateTimeField(auto_now_add=True)