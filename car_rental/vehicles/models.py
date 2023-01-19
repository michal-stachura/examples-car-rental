from enum import Enum
from django.db import models
from django.utils.timezone import now

from car_rental.members.models import Member


class Car(models.Model):
    class BRAND(Enum):
        ford = ("ford", "Ford")
        fiat = ("fiat", "Fiat")
        toyo = ("toyo", "Toyota")
        kia = ("kia", "Kia")
        peug = ("peug", "Peugeot")
        citr = ("citr", "Citroen")
        chev = ("chev", "Chevrolet")

    brand = models.CharField(
        max_length=4,
        blank=True,
        choices=[x.value for x in BRAND],
        default=BRAND.ford.value[0]
    )
    model = models.CharField(max_length=120)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    production_year = models.PositiveSmallIntegerField(
        choices=tuple((x,) * 2 for x in range(2010, now().year + 1)), default=2010
    )
    color = models.CharField(max_length=20, default="White")
    seats = models.PositiveSmallIntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    air_condition = models.BooleanField(default=True)

    class Meta:
        ordering = ["brand", "production_year"]
        constraints = [
            models.UniqueConstraint(
                fields = ["member", "brand"],
                name = "unique_car_brand_and_memeber",
                condition = models.Q(production_year__lte=2016),
                violation_error_message = "You can add only one old car within car brand. Old <= 2016.",
            ),
            models.CheckConstraint(
                check = models.Q(end_date__gte=models.F("start_date")),
                name = "check_start_and_end_date",
                violation_error_message = "Start date must be before end date."
            ),
            models.CheckConstraint(
                check = (
                    models.Q(
                        color__iexact="black",
                        air_condition=True
                    )
                    | ~models.Q(color__iexact="black")
                ),
                name = "check_air_condition",
                violation_error_message = "Black cars must have air condition."
            )
        ]

    def __str__(self) -> str:
        return f"{self.model} ({self.BRAND[self.brand].value[1]})"


class Motorcycle(models.Model):

    class BRAND(Enum):
        suzu = ("suzu", "Suzuki")
        yama = ("yama", "Yamaha")
        harl = ("harl", "Harley Davidson")
        
    brand = models.CharField(
        max_length=4,
        blank=True,
        choices=[x.value for x in BRAND],
        default=BRAND.suzu.value[0]
    )
    model = models.CharField(max_length=120)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    production_year = models.PositiveSmallIntegerField(
        choices=tuple((x,) * 2 for x in range(2010, now().year + 1)), default=2010
    )
    color = models.CharField(max_length=20, default="White")
    seats = models.PositiveSmallIntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ["brand", "production_year"]

    def __str__(self) -> str:
        return f"{self.model} ({self.BRAND[self.brand].value[1]})"
