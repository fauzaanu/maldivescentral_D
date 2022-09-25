from django.db import models
from django.utils.text import slugify


# Create your models here.

class Cat(models.Model):
    category_name=models.CharField(max_length=100)
    category_slug = models.SlugField(unique=False, blank=False, editable=False, default='#')

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Cat, self).save(*args, **kwargs)


class Listing(models.Model):
    listing_name = models.CharField(max_length=100)
    listing_description = models.TextField(max_length=100)
    listing_seo_name = models.SlugField(unique=True, blank=False, editable=False)
    listing_original_url = models.CharField(max_length=200, default="#")
    listing_category = models.ManyToManyField(Cat)

    def save(self, *args, **kwargs):
        self.listing_seo_name = slugify(self.listing_name)
        super(Listing, self).save(*args, **kwargs)

    def __str__(self):
        return self.listing_name
