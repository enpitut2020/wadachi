# Generated by Django 3.0.8 on 2020-07-24 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wadachi_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(default='', null=True),
        ),
    ]
