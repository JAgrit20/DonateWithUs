# Generated by Django 2.2.17 on 2021-03-21 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0007_auto_20210321_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ngoprofile',
            old_name='owner2',
            new_name='ngo_creator',
        ),
    ]
