from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import homepage
from maldivescentral import settings

urlpatterns = [
    path('', homepage),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)