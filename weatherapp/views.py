from django.shortcuts import render


def home(request):
    return render(request, "weather_app.html")
# Create your views here.
