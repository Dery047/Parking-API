from django.db import models
from django.utils import timezone
from decimal import Decimal

class VehicleRecord(models.Model):
    license_plate = models.CharField(max_length=10)
    entry_time = models.DateTimeField(default=timezone.now)
    exit_time = models.DateTimeField(blank=True, null=True)
    total_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,editable=False)

    def calculate_total(self):
        if self.entry_time and self.exit_time:
            duration = self.exit_time - self.entry_time
            hours = duration.total_seconds() / 3600
            hourly_rate = Decimal("5.00")  
            return round(Decimal(hours) * hourly_rate, 2)
        return None

    def save(self, *args, **kwargs):
        if self.exit_time and not self.total_charge:
            self.total_charge = self.calculate_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.license_plate} - {self.entry_time}"
