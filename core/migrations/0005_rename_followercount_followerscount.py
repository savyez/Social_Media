# Generated by Django 4.1.7 on 2023-04-21 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_followercount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FollowerCount',
            new_name='FollowersCount',
        ),
    ]
