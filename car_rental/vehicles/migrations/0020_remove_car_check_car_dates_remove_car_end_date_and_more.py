# Generated by Django 4.1.5 on 2023-01-19 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0019_car_check_car_dates"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="car",
            name="check_car_dates",
        ),
        migrations.RemoveField(
            model_name="car",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="car",
            name="start_date",
        ),
        migrations.RemoveField(
            model_name="motorcycle",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="motorcycle",
            name="start_date",
        ),
    ]