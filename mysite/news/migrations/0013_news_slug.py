# Generated by Django 3.2.13 on 2022-08-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='slug1', max_length=255, unique=True, verbose_name='Url'),
        ),
    ]
