from django.shortcuts import render
import requests, json
import urllib.request 
import string
from django.http import HttpResponse

def get_celsius(k):
    c = k - 273.15
    c1 = round(c,2)
    return c1

def get_farenheit(k):
     f = ((k - 273.15) * (9/5)) + 32 
     f1 = round(f,2)
     return f1

# Create your views here.
def index(req):
    if req.method == 'POST':
        try:
            city = req.POST['enter']
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6fe78dc40ed1bd883c269688d2f35273'
            r = requests.get(url.format(city)).json()

            # source = urllib.request.urlopen(
            #     'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=6fe78dc40ed1bd883c269688d2f35273').read()
            # r = json.loads(source) 

            city1 = city.upper()
            data = {
                'city' : city1,
                'temperature': r['main']['temp'],
                'temp_in_celsius' : get_celsius(r['main']['temp']),
                'temp_in_farenheit' : get_farenheit(r['main']['temp']),
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon']
            }
            # print(data)
        except Exception as e:
            return HttpResponse('<h1>City Not Found</h1>')
    else:
        data = {}
    return render(req, 'weather/index.html', {'data': data})

