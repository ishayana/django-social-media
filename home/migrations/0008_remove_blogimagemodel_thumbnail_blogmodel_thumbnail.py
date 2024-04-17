# Generated by Django 4.2.5 on 2024-04-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_blogimagemodel_is_thumbnail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogimagemodel',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='blog_image/'),
        ),
    ]