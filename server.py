from flask import Flask, render_template,request
from weather import get_current_weather
from waitress import serve
from utils import fahrenheit_to_celsius, get_temperature_message

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    if not bool(city.strip()):
        city='Kolkata'

    try:
        weather_data = get_current_weather(city)
    except Exception as e:
        print("ERROR:", e)
        return render_template('city-not-found.html')

    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    
    temp_c = fahrenheit_to_celsius(temp)
    feels_like_c = fahrenheit_to_celsius(feels_like)

    message = get_temperature_message(temp_c,feels_like_c)

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{temp_c:.1f}",
        feels_like=f"{feels_like_c:.1f}",
        message=message
    )

if __name__=="__main__":
    serve(app,host="0.0.0.0", port=8000)