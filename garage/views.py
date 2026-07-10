from django.shortcuts import render,redirect
from .forms import ServiceBookingForm
from django.contrib.auth.decorators import login_required
from .models import ServiceBooking


@login_required
def book_service(request):
    if request.method=="POST":
        form=ServiceBookingForm(request.POST)
        if form.is_valid():
            booking=form.save(commit=False)
            booking.user=request.user
            booking.save()

            return redirect("dashboard")
    else:
        form=ServiceBookingForm()

    return render(request,"garage/book_service.html",{"form":form})


@login_required
def my_services(request):
    services=ServiceBooking.objects.filter(user=request.user)
    return render(request,"garage/my_services.html",{"services":services})
