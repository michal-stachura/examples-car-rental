# Generated by Django 4.1.5 on 2023-01-19 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0002_car_check_air_condition"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="car",
            name="check_air_condition",
        ),
    ]
