# Generated by Django 4.1.2 on 2022-11-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_signup_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='text',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='img',
            field=models.FileField(default='static/img/buta1.jpg', upload_to='img'),
        ),
    ]
