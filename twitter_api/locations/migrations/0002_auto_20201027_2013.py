# Generated by Django 3.1.2 on 2020-10-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]