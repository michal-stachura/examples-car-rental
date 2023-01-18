from enum import Enum
from django.db import models
from django.utils.timezone import now

from car_rental.members.models import Member

class Car(models.Model):

    class BRAND(Enum):
        ford = ("for", "Ford")
        fiat = ("fia", "Fiat")
        toyota = ("toy", "Toyota")
        kia = ("kia", "Kia")
        peugeot = ("peu", "Peugeot")
        citroen = ("cit", "Citroen")
        chevrolet = ("che", "Chevrolet")
        

    brand = models.CharField(
        max_length=3,
        blank=True,
        choices=[x.value for x in BRAND],
        default=BRAND.ford.value[0]
    )
    model = models.CharField(max_length=120)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    production_year = models.PositiveSmallIntegerField(
        choices=tuple((x,)*2 for x in range(2010, now().year +1)),
        default=2010
    )
    color = models.CharField(max_length=20, default="White")
    seats = models.PositiveSmallIntegerField(default=1)
    air_condition = models.BooleanField(default=True)

    class Meta:
        ordering = ["brand", "production_year"]

    def __str__(self) -> str:
        return f"{self.model} ({self.brand})"
    

class Motorcycle(models.Model):

    BRAND_SUZUKI = "suz"
    BRAND_YAMAHA = "yam"
    BRAND_HARLEY = "har"
    
    BRANDS = [
        (BRAND_SUZUKI, "Suzuki"),
        (BRAND_YAMAHA, "Yamaha"),
        (BRAND_HARLEY, "Harley Davidson")
    ]

    PRODUCTION_YEARS = (
        (2010, 2010),
        (2011, 2011),
        (2012, 2012),
        (2013, 2013),
        (2014, 2014),
        (2015, 2015),
        (2016, 2016),
        (2017, 2017),
        (2018, 2018),
        (2019, 2019),
        (2020, 2020),
        (2021, 2021),
        (2022, 2022),        
    )

    brand = models.CharField(
        max_length=3,
        blank=True,
        choices=BRANDS
    )
    model = models.CharField(max_length=120)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    production_year = models.PositiveSmallIntegerField(
        choices=PRODUCTION_YEARS,
        default=PRODUCTION_YEARS[0]
    )
    color = models.CharField(max_length=20, default="White")
    seats = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["brand", "production_year"]

    def __str__(self) -> str:
        return f"{self.model} ({self.brand})"
