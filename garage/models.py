from django.db import models
from django.contrib.auth.models import User

class ServiceBooking(models.Model):
    STATUS_CHOICES =[
        ("Pending","Pending"),
        ("Approved","Approved"),
        ("Completed","Completed"),
    ]

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    phone=models.CharField(max_length=10)

    car_brand = models.CharField(max_length=100)

    car_model = models.CharField(max_length=100)

    registration_number = models.CharField(max_length=30)

    manufacturing_year = models.PositiveIntegerField()

    problem_description = models.TextField()

    preferred_service_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.car_brand} {self.car_model}"