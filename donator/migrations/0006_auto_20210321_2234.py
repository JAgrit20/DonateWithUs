# Generated by Django 2.2.17 on 2021-03-21 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donator', '0005_product_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='owner',
            new_name='product_owner',
        ),
    ]
