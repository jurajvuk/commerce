# Generated by Django 3.1.2 on 2021-07-29 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image_url',
        ),
    ]