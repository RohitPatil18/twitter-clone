# Generated by Django 3.1.2 on 2020-10-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='title',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]