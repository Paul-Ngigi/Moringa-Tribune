# Generated by Django 3.2.2 on 2021-05-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='post',
            field=models.TextField(default='something'),
        ),
    ]
