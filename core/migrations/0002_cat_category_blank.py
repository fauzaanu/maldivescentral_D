# Generated by Django 4.1.1 on 2022-09-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='category_blank',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
