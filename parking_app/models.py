from django.db import models
from django.utils import timezone
from decimal import Decimal

class VehicleRecord(models.Model): #creating models of the app
    license_plate = models.CharField(max_length=10)
    entry_time = models.DateTimeField(default=timezone.now)
    exit_time = models.DateTimeField(blank=True, null=True)
    total_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,editable=False)

    def calculate_total(self):
        if self.entry_time and self.exit_time: #calculates if there is an entry and exit time
            duration = self.exit_time - self.entry_time #total duration of the car in the parking
            hours = duration.total_seconds() / 3600 #convert to hours
            hourly_rate = Decimal("2.00")   #base cost per hour 
            return round(Decimal(hours) * hourly_rate, 2) #getting total charge 
        return None

    def save(self, *args, **kwargs): #overriding the ddefault save() method 
        if self.exit_time and not self.total_charge: #evaluates if there´s an exit time but still haven't made the charge, and saves it
            self.total_charge = self.calculate_total() #total charge takes the value of total charge
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.license_plate} - {self.entry_time}" 
        #readable string that represents the object
        
        
        