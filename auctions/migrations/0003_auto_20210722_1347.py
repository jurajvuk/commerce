# Generated by Django 3.1.2 on 2021-07-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='listing',
            name='category',
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', to='auctions.Category'),
        ),
    ]