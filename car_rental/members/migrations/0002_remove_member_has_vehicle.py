# Generated by Django 4.0.8 on 2023-01-16 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='has_vehicle',
        ),
    ]
