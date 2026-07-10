from django.contrib import admin
from . models import ServiceBooking

@admin.register(ServiceBooking)
class ServiceBookingAdmin(admin.ModelAdmin):
    pass

