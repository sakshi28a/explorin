# Generated by Django 3.1.4 on 2021-01-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_auto_20210108_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]