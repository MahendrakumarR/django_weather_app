from django.shortcuts import render
from .form import CityForm           # here import from 'form.py' file
from .models import City
import requests
from django.contrib import messages

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},&appid=e7615501807a414c6cbf283b8c65ef20&units=metric'  # this is a API
    if request.method == 'POST':
        form = CityForm(request.POST)
        print(form)
        if form.is_valid():
            NCity = form.cleaned_data['name']
            CCity = City.objects.filter(name=NCity).count()
            if CCity == 0:
                res = requests.get(url.format(NCity)).json()
                if res['cod'] == 200:
                    form.save()
                    messages.success(request," "+NCity+" Added Successfully..!")
                else:
                    messages.error(request,"City Does Not Exists..!")
            else:
                messages.error(request,"City Already Exists..!")

    form = CityForm()            
    return render(request, "weather_app.html",{'form':form})

# Create your views here.
