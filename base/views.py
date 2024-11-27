from django.shortcuts import render,redirect
import requests
# Create your views here.

api_key='c1506a28da918205d6870fbdf90780ef'
weather_data=None

def home(request):
    global city
    global weather_data
    if request.method=='POST':
        city=request.POST['city']    
        weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
        print(weather_data)
        return redirect('showdata')
 
    return render(request,'home.html',)

def showdata(request):
    context={
            'data':weather_data.json(),
            "city":city
    }
    return render(request,'showdata.html',context)