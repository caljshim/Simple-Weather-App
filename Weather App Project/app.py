from tkinter import *
from tkinter import messagebox
import requests

api_key = '3253651e650882d0741fca5531df5bbc'

def get_weather(city):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial")

    if weather_data.json()['cod'] == '404':
        return None
    else: 
        weather = weather_data.json()['weather'][0]['description']
        temperature = round(weather_data.json()['main']['temp'])
        humidity = weather_data.json()['main']['humidity']
        icon = weather_data.json()['weather'][0]['icon']
        wind_speed = weather_data.json()['wind']['speed']
        country_name = weather_data.json()['sys']['country']
        all_data = (weather, temperature, humidity, wind_speed, icon, country_name)
        return all_data

def search():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        location_lbl['text'] = " ".join(w.capitalize() for w in city.split()) + ', ' + weather[5]
        img['bitmap'] = f'Icons1/{weather[4]}@2x.png'
        temp_lbl['text'] = f'{weather[1]}°F, {round(((weather[1] - 32) * (5/9)))}°C'
        weather_lbl['text'] = " ".join(w.capitalize() for w in weather[0].split())
    else:
        messagebox.showerror('Error', f'{city} not found. Please enter a different city.')

weather_app = Tk()
weather_app.title("Weather App")
weather_app.geometry('500x350')
weather_app.resizable(False, False)

city_text = StringVar()
city_entry = Entry(weather_app, textvariable=city_text)
city_entry.pack()

search_button = Button(weather_app, text='Search City', width=12, command=search)
search_button.pack()

location_lbl = Label(weather_app, text='', font=('bold', 20))
location_lbl.pack()

img = Label(weather_app, image='')
img.pack()

temp_lbl = Label(weather_app, text='', font=('normal', 14))
temp_lbl.pack()

weather_lbl = Label(weather_app, text='', font=('normal', 14))
weather_lbl.pack()

weather_app.mainloop()