from django.contrib import admin

from car_rental.vehicles.models import Car, Motorcycle

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "member",
        "production_year",
        "color",
        "seats"
    ]

    list_filter = [
        "brand",
    ]

    search_fields = [
        "id",
        "name",
        "member__id",
        "member__name",
    ]

@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "member",
        "production_year",
        "color",
        "seats"
    ]

    list_filter = [
        "brand",
    ]

    search_fields = [
        "id",
        "name",
        "member__id",
        "member__name",
    ]