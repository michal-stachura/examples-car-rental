# Generated by Django 4.1.5 on 2023-01-19 10:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0017_remove_car_unique_car_brand_and_memeber_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="end_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="car",
            name="start_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="motorcycle",
            name="end_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="motorcycle",
            name="start_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]