from django.contrib import admin
from .models import Asset, Employee


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "asset_code",
        "name",
        "department",
        "manufacturer",
        "is_active",
    )

    search_fields = (
        "asset_code",
        "name",
        "serial_number",
    )

    list_filter = (
        "department",
        "is_active",
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "personnel_code",
        "first_name",
        "last_name",
        "department",
        "job_title",
        "is_active",
    )

    search_fields = (
        "personnel_code",
        "first_name",
        "last_name",
    )

    list_filter = (
        "department",
        "is_active",
    )