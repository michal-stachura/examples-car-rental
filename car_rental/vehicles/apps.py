from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VehiclesConfig(AppConfig):
    name = "car_rental.vehicles"
    verbose_name = _("Vehicles")

    def ready(self):
        try:
            import car_rental.vehicles.signals  # noqa F401
        except ImportError:
            pass
