# Generated by Django 3.2.13 on 2022-08-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0026_alter_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='id_flib',
            field=models.IntegerField(default=0),
        ),
    ]
