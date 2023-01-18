from django.db import models

from car_rental.utils.common_model import CommonModel


class Member(CommonModel):

    STATUS_PENING = "pending"
    STATUS_ACTIVE = "active"
    STATUS_BLOCKED = "blocked"

    MEMBER_STATUSES = [
        (STATUS_PENING, "Pending"),
        (STATUS_ACTIVE, "Active"),
        (STATUS_BLOCKED, "Blocked"),
    ]

    name = models.CharField(max_length=50, null=False)
    status = models.CharField(max_length=12, blank=True, choices=MEMBER_STATUSES)
    is_vip = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name}"
