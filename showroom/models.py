from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):

    brand = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    year = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=12, decimal_places=2)

    color = models.CharField(max_length=50)

    fuel_type = models.CharField(max_length=50)

    transmission = models.CharField(max_length=50)

    description = models.TextField()

    image = models.ImageField(upload_to="cars/")

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.brand}{self.model}"


class PurchaseBooking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    message=models.TextField()
    booking_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=20,default="Pending")
    
    def __str__(self):
        return f"{self.user.username}{self.car.brand}{self.car.model}"
    