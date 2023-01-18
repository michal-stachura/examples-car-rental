from django.contrib import admin

from car_rental.members.models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "status",
        "is_vip"
    ]

    list_filter = [
        "is_vip",
    ]

    search_fields = [
        "id",
        "name"
    ]