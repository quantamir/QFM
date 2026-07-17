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


class Employee(models.Model):
    personnel_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10, blank=True)
    mobile = models.CharField(max_length=15, blank=True)

    class Department(models.TextChoices):
        SERVICES = "SERVICES", "خدمات"
        SECURITY = "SECURITY", "حراست"
        LAUNDRY = "LAUNDRY", "لاندری"
        CSSD = "CSSD", "CSSD"
        WAREHOUSE = "WAREHOUSE", "انبار خدمات"
        TRANSPORT = "TRANSPORT", "حمل و نقل"

    department = models.CharField(
        max_length=20,
        choices=Department.choices,
        default=Department.SERVICES,
    )

    job_title = models.CharField(max_length=100)
    hire_date = models.DateField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"