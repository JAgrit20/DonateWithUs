# Generated by Django 2.2.17 on 2021-01-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='needrequest',
            name='body',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='needrequest',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]