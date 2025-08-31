import json , requests
from django.shortcuts import render
from .weather import weather_data

# Create your views here.
def get_city(request):
    city = None
    data = [] # ✅ always define data first

    if request.method == "POST":
        # get city from form input
        city = request.POST.get("city")
        if city:  
            data = weather_data(city)

    return render(request, "weather.html", {"data": data, "city": city})
