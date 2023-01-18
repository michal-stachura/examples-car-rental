# Generated by Django 4.1.5 on 2023-01-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0012_remove_car_unique_car_brand_and_memeber_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="car",
            name="unique_car_brand_and_memeber",
        ),
        migrations.AddConstraint(
            model_name="car",
            constraint=models.UniqueConstraint(
                fields=("member", "brand"), name="unique_car_brand_and_memeber"
            ),
        ),
    ]
