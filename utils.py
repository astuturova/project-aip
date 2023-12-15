import requests
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from datetime import datetime


class ForecastService:
    weatherCode = {
        "0": "Unknown",

        "1000": "солнечно ☀️",
        "1100": "преимущественно солнечно 🌤️",
        "1101": "переменная облачность ⛅️",
        "1102": "преимущественно облачно 🌥️",
        "1001": "облачно ☁️. Будьте осторожны на дорогах!",
        "2000": "туман 😶‍🌫️. Будьте осторожны на дорогах!",
        "2100": "лёгкий туман 😶‍🌫️",
        "4000": "морось ☔️",
        "4001": "дождливо ☔️. Не забудьте взять зонт!",
        "4200": "небольшой дождь ☔️. Рекомендую Вам взять зонт!",
        "4201": "ливень 🌧️. Будьте осторожны и не забудьте взять зонт!",
        "5000": "снегопад 🌨️",
        "5001": "небольшой снегопад 🌨️",
        "5100": "небольшой снег 🌨️",
        "5101": "метель 🥶. Будьте осторожны на дорогах!",
        "6000": "изморозь 🥶",
        "6001": "град 🧊",
        "6200": "лёгкий град 🧊",
        "6201": "сильный град 🧊. Будьте осторожны и не забудьте взять зонт!",
        "7000": "мокрый снег 🌨️",
        "7101": "сильный мокрый снег 🌨️",
        "7102": "немного мокрого снега 🌨️",
        "8000": "гроза 🌩️. Будьте осторожны!"
    }

    def get_forecast_for_day(self, name: str, date):
        url = f"https://api.tomorrow.io/v4/weather/forecast?location={name}&timesteps=1d&apikey=GpZe9ZkYHUc34zdWZJ8r0GffrepVdW7B"

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers)

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
            # print(json_data["timelines"]["daily"])
            # data = json_data["timelines"]["daily"][1]["values"]
            for elem in json_data["timelines"]["daily"]:
                if elem["time"][:len(str(date))] == str(date):
                    data = elem["values"]
                    print(elem["time"])
                    for key in out:
                        if key in ["weatherCodeMax", "weatherCodeMin"]:
                            out[key] = self.weatherCode[str(data[key])]
                            continue
                        out[key] = data[key]
            out["location"] = json_data['location']['name']
            if name == "AE-DU":
                out['location'] = "United Arab Emirates, Dubai"
        return out

    def get_forecast_for_week(self, name):
        url = f"https://api.tomorrow.io/v4/weather/forecast?location={name}&timesteps=1d&apikey=GpZe9ZkYHUc34zdWZJ8r0GffrepVdW7B"

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers)

        output_array = []

        if response.ok:
            json_data = response.json()
            # print(json_data["timelines"]["daily"])
            # data = json_data["timelines"]["daily"][1]["values"]
            for elem in json_data["timelines"]["daily"]:
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
                data = elem["values"]
                out["time"] = datetime.strptime(elem["time"], '%Y-%m-%dT%H:%M:%SZ').date().strftime("%d.%m.%Y")
                for key in out:
                    if key in ["weatherCodeMax", "weatherCodeMin"]:
                        out[key] = self.weatherCode[str(data[key])]
                        continue
                    if key != "time":
                        out[key] = data[key]
                output_array.append(out)
                out["location"] = json_data['location']['name']
                if name == "AE-DU":
                    out['location'] = "United Arab Emirates, Dubai"
        return output_array


class KeyboardConstructor:

    def get_menu_keyboard(self):
        buttons = [
            [
                types.InlineKeyboardButton(text="⏰ Погода на завтра", callback_data="forecast_tomorrow"),
                types.InlineKeyboardButton(text="🎏 Погода на сегодня", callback_data="forecast_today")
            ],
            [
                types.InlineKeyboardButton(text="📅 Погода на неделю", callback_data="forecast_week")
            ],
            [
                types.InlineKeyboardButton(text="Регион", callback_data="set_region"),
                types.InlineKeyboardButton(text="Таймер", callback_data="set_timer")
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def get_region_settings_keyboard(self):
        buttons = [
            [
                types.InlineKeyboardButton(text="Москва", callback_data="region_moscow"),
                types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="region_petersburg")
            ],
            [
                types.InlineKeyboardButton(text="Казань", callback_data="region_kazan"),
                types.InlineKeyboardButton(text="Волгоград", callback_data="region_volgograd")
            ],
            [
                types.InlineKeyboardButton(text="Дубай", callback_data="region_dubai"),
                types.InlineKeyboardButton(text="Сан-Франциско", callback_data="region_san-francisco")
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def get_timer_settings_keyboard(self):
        buttons = [
            [
                types.InlineKeyboardButton(text="1 минута", callback_data="timer_minute"),
                types.InlineKeyboardButton(text="1 час", callback_data="timer_hour")
            ],
            [
                types.InlineKeyboardButton(text="12 часов", callback_data="timer_day"),
                types.InlineKeyboardButton(text="24 часов", callback_data="timer_cycle")
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard
