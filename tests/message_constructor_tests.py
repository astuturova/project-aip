import unittest

from utils import MessageConstructor


class MessageConstructorTests(unittest.TestCase):
    def test_get_output_message_for_day_given_data_then_correct(self):
        messageConstructor = MessageConstructor()
        data = {'temperatureApparentAvg': -7.96, 'temperatureApparentMax': -2.74, 'temperatureApparentMin': -13.38,
                'temperatureAvg': -1.47, 'temperatureMax': 2.55, 'temperatureMin': -5.79, 'windGustAvg': 11.18,
                'windGustMax': 14.55, 'windGustMin': 7.92, 'windSpeedAvg': 7.4, 'windSpeedMax': 9.52,
                'windSpeedMin': 5.38, 'humidityAvg': 88.29, 'humidityMax': 91.66, 'humidityMin': 85.17,
                'weatherCodeMax': 'небольшой снег 🌨️', 'weatherCodeMin': 'небольшой снег 🌨️',
                'location': 'Москва, Центральный федеральный округ, Россия'}

        with open("forecast_for_day.txt", "r") as f:
            self.assertEqual(messageConstructor.get_output_message_for_day(data, "завтра"), f.read())

    def test_get_output_message_for_day_given_data_then_wrong(self):
        messageConstructor = MessageConstructor()
        data = {'temperatureApparentAvg': -7.96, 'temperatureApparentMax': -2.74, 'temperatureApparentMin': -13.38,
                'temperatureAvg': -1.47, 'temperatureMax': 2.55, 'temperatureMin': -5.79, 'windGustAvg': 11.18,
                'windGustMax': 14.55, 'windGustMin': 7.92, 'windSpeedAvg': 7.4, 'windSpeedMax': 9.52,
                'windSpeedMin': 5.38, 'humidityAvg': 88.29, 'humidityMax': 91.66, 'humidityMin': 85.17,
                'weatherCodeMax': 'небольшой снег 🌨️', 'weatherCodeMin': 'небольшой снег 🌨️',
                'location': 'Москва, Центральный федеральный округ, Россия'}
        with open("forecast_for_day.txt", "r") as f:
            self.assertNotEquals(messageConstructor.get_output_message_for_day(data, "сегодня"), f.read())

    def test_get_output_message_for_week_given_data_then_correct(self):
        messageConstructor = MessageConstructor()
        data = [{'temperatureApparentAvg': -15.55, 'temperatureApparentMax': -9.99, 'temperatureApparentMin': -19.93,
                 'temperatureAvg': -8.88, 'temperatureMax': -6.63, 'temperatureMin': -11.88, 'windGustAvg': 6.72,
                 'windGustMax': 9.5, 'windGustMin': 3.13, 'windSpeedAvg': 4.52, 'windSpeedMax': 6.5,
                 'windSpeedMin': 1.88, 'humidityAvg': 86.71, 'humidityMax': 94, 'humidityMin': 74,
                 'weatherCodeMax': 'облачно ☁️. Будьте осторожны на дорогах!',
                 'weatherCodeMin': 'облачно ☁️. Будьте осторожны на дорогах!', 'time': '15.12.2023',
                 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -12.63, 'temperatureApparentMax': -9.77, 'temperatureApparentMin': -16.61,
                 'temperatureAvg': -6.22, 'temperatureMax': -3.93, 'temperatureMin': -9.65, 'windGustAvg': 7.35,
                 'windGustMax': 9.07, 'windGustMin': 6.3, 'windSpeedAvg': 4.9, 'windSpeedMax': 5.95,
                 'windSpeedMin': 4.14, 'humidityAvg': 86.41, 'humidityMax': 89.6, 'humidityMin': 83.33,
                 'weatherCodeMax': 'небольшой снегопад 🌨️', 'weatherCodeMin': 'небольшой снегопад 🌨️',
                 'time': '16.12.2023', 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -7.96, 'temperatureApparentMax': -2.74, 'temperatureApparentMin': -13.38,
                 'temperatureAvg': -1.47, 'temperatureMax': 2.55, 'temperatureMin': -5.79, 'windGustAvg': 11.18,
                 'windGustMax': 14.55, 'windGustMin': 7.92, 'windSpeedAvg': 7.4, 'windSpeedMax': 9.52,
                 'windSpeedMin': 5.38, 'humidityAvg': 88.29, 'humidityMax': 91.66, 'humidityMin': 85.17,
                 'weatherCodeMax': 'небольшой снег 🌨️', 'weatherCodeMin': 'небольшой снег 🌨️', 'time': '17.12.2023',
                 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -6.49, 'temperatureApparentMax': -2.62, 'temperatureApparentMin': -12.16,
                 'temperatureAvg': -1.25, 'temperatureMax': 1.79, 'temperatureMin': -5.72, 'windGustAvg': 7.57,
                 'windGustMax': 9.22, 'windGustMin': 5.57, 'windSpeedAvg': 5.04, 'windSpeedMax': 6.1,
                 'windSpeedMin': 3.66, 'humidityAvg': 92.77, 'humidityMax': 97.61, 'humidityMin': 90.1,
                 'weatherCodeMax': 'облачно ☁️. Будьте осторожны на дорогах!',
                 'weatherCodeMin': 'облачно ☁️. Будьте осторожны на дорогах!', 'time': '18.12.2023',
                 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -4.03, 'temperatureApparentMax': -3.54, 'temperatureApparentMin': -6.08,
                 'temperatureAvg': 1.21, 'temperatureMax': 1.93, 'temperatureMin': -1.65, 'windGustAvg': 14.2,
                 'windGustMax': 18.3, 'windGustMin': 5.82, 'windSpeedAvg': 6.4, 'windSpeedMax': 8.27,
                 'windSpeedMin': 3.64, 'humidityAvg': 99.05, 'humidityMax': 99.89, 'humidityMin': 95.39,
                 'weatherCodeMax': 'небольшой снегопад 🌨️', 'weatherCodeMin': 'небольшой снегопад 🌨️',
                 'time': '19.12.2023', 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -3.95, 'temperatureApparentMax': -3.15, 'temperatureApparentMin': -5.03,
                 'temperatureAvg': 0.92, 'temperatureMax': 1.73, 'temperatureMin': 0.49, 'windGustAvg': 11.67,
                 'windGustMax': 13.72, 'windGustMin': 10.27, 'windSpeedAvg': 5.36, 'windSpeedMax': 6.69,
                 'windSpeedMin': 4.42, 'humidityAvg': 96.27, 'humidityMax': 99.22, 'humidityMin': 89.14,
                 'weatherCodeMax': 'небольшой снегопад 🌨️', 'weatherCodeMin': 'небольшой снегопад 🌨️',
                 'time': '20.12.2023', 'location': 'Москва, Центральный федеральный округ, Россия'}]
        with open("forecast_for_week.txt", "r") as f:
            self.assertEqual(messageConstructor.get_output_message_for_week(data), f.read())

    def test_get_output_message_for_week_given_data_then_wrong(self):
        messageConstructor = MessageConstructor()
        data = [{'temperatureApparentAvg': -15.55, 'temperatureApparentMax': -9.99, 'temperatureApparentMin': -19.93,
                 'temperatureAvg': -8.88, 'temperatureMax': -6.63, 'temperatureMin': -11.88, 'windGustAvg': 6.72,
                 'windGustMax': 9.5, 'windGustMin': 3.13, 'windSpeedAvg': 4.52, 'windSpeedMax': 6.5,
                 'windSpeedMin': 1.88, 'humidityAvg': 86.71, 'humidityMax': 94, 'humidityMin': 74,
                 'weatherCodeMax': 'облачно ☁️. Будьте осторожны на дорогах!',
                 'weatherCodeMin': 'облачно ☁️. Будьте осторожны на дорогах!', 'time': '15.12.2023',
                 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -12.63, 'temperatureApparentMax': -9.77, 'temperatureApparentMin': -16.61,
                 'temperatureAvg': -6.22, 'temperatureMax': -3.93, 'temperatureMin': -9.65, 'windGustAvg': 7.35,
                 'windGustMax': 9.07, 'windGustMin': 6.3, 'windSpeedAvg': 4.9, 'windSpeedMax': 5.95,
                 'windSpeedMin': 4.14, 'humidityAvg': 86.41, 'humidityMax': 89.6, 'humidityMin': 83.33,
                 'weatherCodeMax': 'небольшой снегопад 🌨️', 'weatherCodeMin': 'небольшой снегопад 🌨️',
                 'time': '16.12.2023', 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -7.96, 'temperatureApparentMax': -2.74, 'temperatureApparentMin': -13.38,
                 'temperatureAvg': -1.47, 'temperatureMax': 2.55, 'temperatureMin': -5.79, 'windGustAvg': 11.18,
                 'windGustMax': 14.55, 'windGustMin': 7.92, 'windSpeedAvg': 7.4, 'windSpeedMax': 9.52,
                 'windSpeedMin': 5.38, 'humidityAvg': 88.29, 'humidityMax': 91.66, 'humidityMin': 85.17,
                 'weatherCodeMax': 'небольшой снег 🌨️', 'weatherCodeMin': 'небольшой снег 🌨️', 'time': '17.12.2023',
                 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -6.49, 'temperatureApparentMax': -2.62, 'temperatureApparentMin': -12.16,
                 'temperatureAvg': -1.25, 'temperatureMax': 1.79, 'temperatureMin': -5.72, 'windGustAvg': 7.57,
                 'windGustMax': 9.22, 'windGustMin': 5.57, 'windSpeedAvg': 5.04, 'windSpeedMax': 6.1,
                 'windSpeedMin': 3.66, 'humidityAvg': 92.77, 'humidityMax': 97.61, 'humidityMin': 90.1,
                 'weatherCodeMax': 'облачно ☁️. Будьте осторожны на дорогах!',
                 'weatherCodeMin': 'облачно ☁️. Будьте осторожны на дорогах!', 'time': '18.12.2023',
                 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -4.03, 'temperatureApparentMax': -3.54, 'temperatureApparentMin': -6.08,
                 'temperatureAvg': 1.21, 'temperatureMax': 1.93, 'temperatureMin': -1.65, 'windGustAvg': 14.2,
                 'windGustMax': 18.3, 'windGustMin': 5.82, 'windSpeedAvg': 6.4, 'windSpeedMax': 8.27,
                 'windSpeedMin': 3.64, 'humidityAvg': 99.05, 'humidityMax': 99.89, 'humidityMin': 95.39,
                 'weatherCodeMax': 'небольшой снегопад 🌨️', 'weatherCodeMin': 'небольшой снегопад 🌨️',
                 'time': '19.12.2023', 'location': 'Москва, Центральный федеральный округ, Россия'},
                {'temperatureApparentAvg': -3.95, 'temperatureApparentMax': -3.15, 'temperatureApparentMin': -5.03,
                 'temperatureAvg': 0.92, 'temperatureMax': 1.73, 'temperatureMin': 0.49, 'windGustAvg': 11.67,
                 'windGustMax': 13.72, 'windGustMin': 10.27, 'windSpeedAvg': 5.36, 'windSpeedMax': 6.69,
                 'windSpeedMin': 4.42, 'humidityAvg': 96.27, 'humidityMax': 99.22, 'humidityMin': 89.14,
                 'weatherCodeMax': 'небольшой снегопад 🌨️', 'weatherCodeMin': 'небольшой снегопад 🌨️',
                 'time': '20.12.2023', 'location': 'Москва, Центральный федеральный округ, Россия'}]
        with open("forecast_for_week.txt", "r") as f:
            self.assertNotEquals(messageConstructor.get_output_message_for_week(data).lower(), f.read())
