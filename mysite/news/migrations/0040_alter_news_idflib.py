# Generated by Django 3.2.13 on 2022-09-12 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0039_auto_20220912_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='idflib',
            field=models.IntegerField(null=True, verbose_name='id flibusta'),
        ),
    ]
