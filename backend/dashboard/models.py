from django.db import models


class Asset(models.Model):
    asset_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    purchase_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.asset_code} - {self.name}"