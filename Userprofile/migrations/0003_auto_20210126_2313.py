# Generated by Django 2.2.17 on 2021-01-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0002_auto_20210126_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Userimg',
            field=models.ImageField(default=False, upload_to='User/'),
        ),
    ]