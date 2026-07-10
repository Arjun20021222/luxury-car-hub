from django import forms
from .models import ServiceBooking

class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model=ServiceBooking
        fields=[
            "phone",

            "car_brand",

            "car_model",

            "registration_number",

            "manufacturing_year",

            "problem_description",

            "preferred_service_date",
        ]
        