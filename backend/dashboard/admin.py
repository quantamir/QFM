from django.contrib import admin
from .models import Asset


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