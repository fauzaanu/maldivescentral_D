# Generated by Django 4.1.1 on 2022-09-26 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cat_category_blank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='category_color',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='category_slug',
        ),
    ]
