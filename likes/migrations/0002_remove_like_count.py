# Generated by Django 3.2.4 on 2021-07-01 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='count',
        ),
    ]
