# Generated by Django 4.2.7 on 2023-11-18 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='av',
            field=models.ImageField(null=True, upload_to='media/user-images/', verbose_name='Аватарка профілю'),
        ),
    ]
