from django.contrib.sitemaps import Sitemap
from django.urls import reverse, path

from .models import Cat


class CategorySiteMap(Sitemap):
    changefreq = 'never'
    priority = 0.9

    def items(self):
        return Cat.objects.all()

    # def location(self, item):
    #     return item
