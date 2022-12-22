# Generated by Django 4.1.2 on 2022-12-01 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_room_text_alter_signup_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='friend_username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend_username', to='myapp.signup'),
        ),
        migrations.AlterField(
            model_name='room',
            name='my_username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_username', to='myapp.signup'),
        ),
    ]
