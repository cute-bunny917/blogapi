# posts/urls.py
from django.urls import path
from .views import PostList, PostDetail , UserList , UserDetail


urlpatterns = [
    path('users/', UserList.as_view()), # API endpoint : List Users
    path('users/<int:pk>/', UserDetail.as_view()), # API endpoint : read, update , delete individual user
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]
