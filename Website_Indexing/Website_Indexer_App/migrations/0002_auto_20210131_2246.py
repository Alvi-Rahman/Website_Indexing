# Generated by Django 3.1.5 on 2021-01-31 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Indexer_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childpage',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='childpage',
            name='media',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]