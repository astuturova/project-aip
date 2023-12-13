import requests
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get_forecast_for_day(name: str):
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={name}&timesteps=1d&apikey=nGhxMDMjU1iN1rxuRzh6n5lkUxFulrtJ"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    weatherCode = {
        "0": "Unknown",
        "1000": "Clear, Sunny",
        "1100": "Mostly Clear",
        "1101": "Partly Cloudy",
        "1102": "Mostly Cloudy",
        "1001": "Cloudy",
        "2000": "Fog",
        "2100": "Light Fog",
        "4000": "Drizzle",
        "4001": "Rain",
        "4200": "Light Rain",
        "4201": "Heavy Rain",
        "5000": "Snow",
        "5001": "Flurries",
        "5100": "Light Snow",
        "5101": "Heavy Snow",
        "6000": "Freezing Drizzle",
        "6001": "Freezing Rain",
        "6200": "Light Freezing Rain",
        "6201": "Heavy Freezing Rain",
        "7000": "Ice Pellets",
        "7101": "Heavy Ice Pellets",
        "7102": "Light Ice Pellets",
        "8000": "Thunderstorm"
    }

    out = {
        "temperatureApparentAvg": None,
        "temperatureApparentMax": None,
        "temperatureApparentMin": None,
        "temperatureAvg": None,
        "temperatureMax": None,
        "temperatureMin": None,
        "windGustAvg": None,
        "windGustMax": None,
        "windGustMin": None,
        "windSpeedAvg": None,
        "windSpeedMax": None,
        "windSpeedMin": None,
        "humidityAvg": None,
        "humidityMax": None,
        "humidityMin": None,
        "weatherCodeMax": None,
        "weatherCodeMin": None
    }

    if response.ok:
        json_data = response.json()
        data = json_data["timelines"]["daily"][0]["values"]
        for key in out:
            if key in ["weatherCodeMax", "weatherCodeMin"]:
                out[key] = weatherCode[str(data[key])]
                continue
            out[key] = data[key]
    return out


class KeyboardConstructor():

    def get_keyboard(self):
        buttons = [
            [
                types.InlineKeyboardButton(text="Погода на завтра", callback_data="forecast_tomorrow"),
                types.InlineKeyboardButton(text="Погода на сегодня", callback_data="forecast_today")
            ],
            [
                types.InlineKeyboardButton(text="Настроить регион", callback_data="set_region"),
                types.InlineKeyboardButton(text="Настроить таймер", callback_data="set_timer")
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard
