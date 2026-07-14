from django import forms
from .models import ServiceBooking
from datetime import date

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
        widgets={
            "preferred_service_date":forms.DateInput(
                attrs={"type":"date"})
        }
    def clean_manufacturing_year(self):
        year=self.cleaned_data["manufacturing_year"]
        current_year=date.today().year
        if year>current_year:
            raise forms.ValidationError(
                "Manufacturing year cannot be greater than the current year"
            )
        return year
    
    def clean_preferred_service_date(self):
        service_date=self.cleaned_data["preferred_service_date"]
        if service_date <=date.today():
            raise forms.ValidationError(
                "Service date cannot be in the past"
            )
        return service_date
    def clean_phone(self):

        phone = self.cleaned_data["phone"]

        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone number must contain only digits."
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return phone
    
    def clean_problem_description(self):

        description = self.cleaned_data["problem_description"]

        if len(description.strip()) < 10:
            raise forms.ValidationError(
                "Problem description should contain at least 10 characters."
            )

        return description