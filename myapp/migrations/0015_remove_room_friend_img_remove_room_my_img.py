# Generated by Django 4.1.2 on 2022-12-16 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_room_friend_img_room_my_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='friend_img',
        ),
        migrations.RemoveField(
            model_name='room',
            name='my_img',
        ),
    ]