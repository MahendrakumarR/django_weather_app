from django.shortcuts import render,redirect
from .form import CityForm           # here import from 'form.py' file
from .models import City
import requests
from django.contrib import messages

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},&appid=e7615501807a414c6cbf283b8c65ef20&units=metric'  # this is a API
    if request.method == 'POST':
        form = CityForm(request.POST)
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

    cities = City.objects.all()
    data=[]
    for city in cities:
        res = requests.get(url.format(city)).json()
        city_weather = {
            'city'        : city,
            'temperature' : res['main']['temp'],
            'description' : res['weather'][0]['description'],
            'country'     : res['sys']['country'],
            'icon'        : res['weather'][0]['icon'],
        }
        data.append(city_weather)
    context = {'data' : data, 'form':form}
    return render(request, "weather_app.html",context)

def delete_city(request,CName):
    City.objects.get(name=CName).delete()
    messages.success(request," "+CName+" Removed Successfully..!")
    return redirect('Home')

# Create your views here.
