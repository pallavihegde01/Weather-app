def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * 5/9


def get_temperature_message(temp,feels_like):
    if temp > 35 or feels_like > 35:
        return "It's very hot 🔥"
    elif temp < 15 or feels_like < 15:
        return "It's cold ❄️"
    else:
        return "Weather is pleasant 🌤️"