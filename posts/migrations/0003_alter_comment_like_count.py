# Generated by Django 3.2.4 on 2021-07-02 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like_count',
            field=models.IntegerField(null=True),
        ),
    ]
