# Generated by Django 4.2.5 on 2023-11-28 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_postmodel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='slug',
        ),
    ]