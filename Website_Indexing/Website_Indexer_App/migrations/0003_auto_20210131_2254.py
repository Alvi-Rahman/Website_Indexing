# Generated by Django 3.1.5 on 2021-01-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Indexer_App', '0002_auto_20210131_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='childpage',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='parentpage',
            name='parent_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]