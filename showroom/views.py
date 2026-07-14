from django.shortcuts import render,get_object_or_404,redirect
from .models import Car,PurchaseBooking
from .forms import PurchaseBookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def car_list(request):
    cars=Car.objects.all()
    return render (request,"showroom/car_list.html",{"cars":cars})

def car_detail(request,pk):
    car=get_object_or_404(Car,id=pk)
    return render(request,"showroom/car_detail.html",{"car":car})

@login_required
def book_car(request,pk):
    car=get_object_or_404(Car,id=pk)

    if not car.available:
        messages.error(
            request,"This car is currently unavailable"
        )
        return redirect("car_detail",pk=car.id)
    
    if PurchaseBooking.objects.filter(
        user=request.user,
        car=car
    ).exists():

        messages.error(
            request,
            "You have already booked this car."
        )

        return redirect("car_detail", pk=car.id)
    
    if request.method=='POST':
        form=PurchaseBookingForm(request.POST)
        if form.is_valid():
            booking=form.save(commit=False)
            booking.user=request.user
            booking.car=car
            booking.save()
            car.available=False
            car.save()
            messages.success(request,"Your Booking has been submitted successfully.")
            return redirect("car_detail",pk=car.id)
    else:
        form=PurchaseBookingForm()

    return render(request,"showroom/book_car.html",{"form":form,"car":car,})

@login_required
def my_bookings(request):
    bookings=PurchaseBooking.objects.filter(user=request.user)
    return render(request,"showroom/my_bookings.html",{"bookings":bookings})

