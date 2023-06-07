from django.shortcuts import render, HttpResponse
from .models import Car

def car_form(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        year = request.POST.get("year")
        price = request.POST.get("price")
        color = request.POST.get("color")
        mileage = request.POST.get("mileage")
        car = Car(brand=brand, model=model, year=year, price=price, color=color, mileage=mileage)
        car.save()
        return HttpResponse("<h1>Car information saved successfully</h1>")
    return render(request, "car_form.html")


