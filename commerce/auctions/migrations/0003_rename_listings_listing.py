# Generated by Django 4.1 on 2022-09-06 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listings',
            new_name='Listing',
        ),
    ]
