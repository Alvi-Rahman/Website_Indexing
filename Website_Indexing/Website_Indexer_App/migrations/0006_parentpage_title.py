# Generated by Django 3.1.5 on 2021-01-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Indexer_App', '0005_auto_20210131_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentpage',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]