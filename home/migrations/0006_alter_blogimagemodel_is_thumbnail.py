# Generated by Django 4.2.5 on 2024-04-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blogimagemodel_is_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimagemodel',
            name='is_thumbnail',
            field=models.BooleanField(default=False, unique=True),
        ),
    ]
