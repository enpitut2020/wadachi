# Generated by Django 3.0.8 on 2020-07-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wadachi_app', '0004_auto_20200727_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='brick',
            name='memo',
            field=models.TextField(default='brickのフィードバックサンプル'),
            preserve_default=False,
        ),
    ]
