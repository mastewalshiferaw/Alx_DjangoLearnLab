from rest_framework import serializers
from django.conf import settings
from .models import Post, Comment

class PostSerializers(serializers.ModelSerailizer):
  class Meta:
    model = Post
    fields = ["id", "author", "title", "content", "created_at", "updated_at"]
    read_only_fields = ["id", "created_at", "updated_at"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]