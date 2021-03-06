from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path("", include("core.urls")),
    path('oauth2/', include('django_auth_adfs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
