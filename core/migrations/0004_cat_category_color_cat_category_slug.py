# Generated by Django 4.1.1 on 2022-09-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_cat_category_color_remove_cat_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='category_color',
            field=models.CharField(default='blue', max_length=50),
        ),
        migrations.AddField(
            model_name='cat',
            name='category_slug',
            field=models.SlugField(blank=True, default='#', editable=False),
        ),
    ]
