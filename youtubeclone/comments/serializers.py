from rest_framework import serializers
from .models import Comment

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comments', 'title', 'description', 'replies']
