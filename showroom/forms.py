from django import forms
from .models import PurchaseBooking

class PurchaseBookingForm(forms.ModelForm):
    class Meta:
        model=PurchaseBooking
        fields=["phone","message"]
        
    def clean_phone(self):
        phone=self.cleaned_data["phone"]
        if len(phone)!=10:
            raise forms.ValidationError(
                "phone number must exactly 10 digits"
            )
        
        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone  number must contain only digits"
            )
        return phone
        
    def clean_message(self):

        message = self.cleaned_data["message"]

        if len(message.strip()) < 15:
            raise forms.ValidationError(
                "Message should contain at least 15 characters."
            )

        return message