import unittest

from utils import MessageConstructor


class MessageConstructorTests(unittest.TestCase):
    # такой же тест написать для вывода на неделю и написать некорректный тест (Просто что нибуьд исправь в expected)
    def test_get_output_message_for_day_given_data_then_correct(self):
        messageConstructor = MessageConstructor()
        data = {
            'temperatureApparentAvg': -7.88,
            'temperatureApparentMax': -2.89,
            'temperatureApparentMin': -13.58,
            'temperatureAvg': -1.52,
            'temperatureMax': 2.3,
            'temperatureMin': -5.98,
            'windGustAvg': 10.65,
            'windGustMax': 14.07,
            'windGustMin': 7.78,
            'windSpeedAvg': 7.06,
            'windSpeedMax': 9.21,
            'windSpeedMin': 5.31,
            'humidityAvg': 89.06,
            'humidityMax': 92.17,
            'humidityMin': 85.49,
            'weatherCodeMax': 'небольшой снег 🌨️',
            'weatherCodeMin': 'небольшой снег 🌨️',
            'location': 'Москва, Центральный федеральный округ, Россия'
        }
        message = " 📍 Вы смотрите погоду в городе Москва, Центральный федеральный округ, Россия\n\n" + " ☺ Ваш персональный прогноз погоды на завтра: \n" + " - В течение дня будет небольшой снег 🌨️\n" + " - 🌡️ Средняя температура воздуха составляет -1.52 ℃, но ощущается как -7.88 ℃\n" + " - 💧 Влажность около 89.06%\n" + " - 🌬️ Ветер дует со скоростью 7.06м/с\n" + " - 💨 А порывы ветра достигают 10.65 м/с"
        self.assertEqual(messageConstructor.get_output_message_for_day(data, "завтра"), message)
