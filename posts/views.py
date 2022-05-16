# posts/views.py
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .models import Post
# custom permission
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer , UserSerializer


# ListCreateAPIView: For our Blog API we want to list all available blog posts as a read-write endpoint
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# RetrieveUpdateDestroyAPIView: We  want to make the individual blog posts available to be read, updated, or deleted.
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # only author of post can edit/delete the post, any other user has read permission
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# ListCreateAPIView: want to list all available users as a read-write endpoint
class UserList(generics.ListCreateAPIView):  
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# RetrieveUpdateDestroyAPIView: We want to make the individual user posts available to be read, updated, or deleted.
class UserDetail(generics.RetrieveUpdateDestroyAPIView):  
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
