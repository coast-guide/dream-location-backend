"""backend URL Configuration

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
from django.urls import path, include, re_path
from listings.api import views as listing_api_views
from users.api import views as users_api_views

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Listings API",
      default_version='v1',
      description="Get all listings added from frontend of dream-location app",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', listing_api_views.ListingList.as_view()),
    path('api/listings/create/', listing_api_views.ListingCreate.as_view()),
    path('api/listings/<int:pk>/',
         listing_api_views.ListingDetail.as_view()),
    path('api/listings/<int:pk>/delete/',
         listing_api_views.ListingDelete.as_view()),
    path('api/listings/<int:pk>/update/',
         listing_api_views.ListingUpdate.as_view()),
    path('api/profiles/', users_api_views.ProfileList.as_view()),
    path('api/profiles/<int:seller>/', users_api_views.ProfileDetail.as_view()),
    path('api/profiles/<int:seller>/update/',
         users_api_views.ProfileUpdate.as_view()),

    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
