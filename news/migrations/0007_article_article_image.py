# Generated by Django 3.2.2 on 2021-05-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='articles/'),
        ),
    ]