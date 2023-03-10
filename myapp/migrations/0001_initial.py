# Generated by Django 4.1.2 on 2022-11-10 10:30

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('img', models.FileField(upload_to='img')),
                ('private', models.BooleanField(default=False, help_text='check to create a private account')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=2000)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('friends_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendself_name', to='myapp.signup')),
                ('my_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myserlf_name', to='myapp.signup')),
            ],
        ),
        migrations.CreateModel(
            name='MyFriendsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_friends', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_imusername', to='myapp.signup')),
                ('my_imusername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myserlf_imusername', to='myapp.signup')),
            ],
        ),
    ]
