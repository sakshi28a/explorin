# Generated by Django 3.1.4 on 2021-01-08 17:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0003_auto_20210108_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='unlikes',
            field=models.ManyToManyField(blank=True, related_name='post_unlikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
