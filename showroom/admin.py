from django.contrib import admin
from .models import Car,PurchaseBooking

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "brand",
        "model",
        "year",
        "price",
        "available",
    )


    search_fields=(
        "brand",
        "model",
    )

    list_filter=(
        "brand",
        "available",
        "fuel_type",
    )

@admin.register(PurchaseBooking)
class PurchaseBookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "car",
        "status",
        "booking_date",
    )

    list_filter = (
        "status",
    )