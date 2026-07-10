from django import forms
from .models import PurchaseBooking

class PurchaseBookingForm(forms.ModelForm):
    class Meta:
        model=PurchaseBooking
        fields=["phone","message"]
        
