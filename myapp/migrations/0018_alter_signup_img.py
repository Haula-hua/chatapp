# Generated by Django 4.1.2 on 2022-12-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_signup_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='img',
            field=models.FileField(default='img/buta1.jpg', upload_to='img'),
        ),
    ]
