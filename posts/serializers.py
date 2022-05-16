# posts/serializers.py
# At the top of the file we have imported Django REST Framework’s serializers class and our own models. 
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # we specified which fields to include and explicitly set the model to use
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)