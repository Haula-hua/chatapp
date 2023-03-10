# Generated by Django 4.1.2 on 2022-11-11 08:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('friend_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_img', to='myapp.signup')),
                ('friend_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_username', to='myapp.signup')),
                ('my_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_username', to='myapp.signup')),
            ],
        ),
        migrations.RemoveField(
            model_name='text',
            name='friends_name',
        ),
        migrations.RemoveField(
            model_name='text',
            name='my_name',
        ),
        migrations.DeleteModel(
            name='MyFriendsList',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
    ]
