"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Swagger - API documentation tool - dependencies
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger - API documentation tool
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="A sample API for learning DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # 4 API endpoint , including users
    path('api/v1/', include('posts.urls')),
    # API Login URL
    path('api-auth/', include('rest_framework.urls')),
    # API endpoints for handling authentication securely in Django Rest Framework.(login/logout/...)
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',  # Signup API endpoints for handling authentication via dj-rest-auth & django-allauth
         include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui(  # schema-swagger-ui
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
]
