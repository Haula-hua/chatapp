# Generated by Django 4.1.2 on 2022-12-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_room_friend_img_remove_room_my_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='status_message',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]