# Generated by Django 3.1.2 on 2021-07-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
