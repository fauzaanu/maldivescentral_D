from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import homepage, searchview, homepage_filtered,add_view,adder_view
from maldivescentral import settings
from django.contrib.sitemaps.views import sitemap
from core.sitemap import CategorySiteMap

sitemaps = {
    'post': CategorySiteMap
}


urlpatterns = [
    path('', homepage, name="home"),
    path('search',searchview, name='search'),
    path('adder',adder_view, name='adder'),
    path('cat/<str:catname>',homepage_filtered, name="filtered"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap')
    #path('add',add_view,name='add_up')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)