# Generated by Django 3.1.5 on 2022-09-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='news_images/default_news.jpg', upload_to='news_images/'),
        ),
    ]
