# Generated by Django 4.0.1 on 2022-01-25 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_busmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='busmodel',
            name='first_class',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='busmodel',
            name='regular_class',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='busmodel',
            name='second_class',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
