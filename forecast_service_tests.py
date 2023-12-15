from utils import ForecastService

import unittest

import requests


class TestCase(unittest.TestCase):

    # Протестировать все name (Например RU-SPE и другие)
    def test_get_forecast_for_day_given_RU_MOW_then_correct(self):
        headers = {"accept": "application/json"}
        response = requests.get(
            url=f"https://api.tomorrow.io/v4/weather/forecast?location=RU-MOW&timesteps=1d&apikey=gUV9cyqDoLGF5p6Y8VjSb0CqmdGTYEVs",
            headers=headers)
        self.assertEqual(200, response.status_code)

    def test_get_forecast_for_day_given_empty_location_then_correct(self):
        headers = {"accept": "application/json"}
        response = requests.get(
            url=f"https://api.tomorrow.io/v4/weather/forecast?location=&timesteps=1d&apikey=gUV9cyqDoLGF5p6Y8VjSb0CqmdGTYEVs",
            headers=headers)
        self.assertEqual(400, response.status_code)
