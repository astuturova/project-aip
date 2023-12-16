import unittest

import requests


class TestCase(unittest.TestCase):

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

    def test_get_forecast_for_day_given_RU_SPE_then_correct(self):
        headers = {"accept": "application/json"}
        response = requests.get(
            url=f"https://api.tomorrow.io/v4/weather/forecast?location=RU-SPE&timesteps=1d&apikey=gUV9cyqDoLGF5p6Y8VjSb0CqmdGTYEVs",
            headers=headers)
        self.assertEqual(200, response.status_code)

    def test_get_forecast_for_day_given_RU_TA_then_correct(self):
        headers = {"accept": "application/json"}
        response = requests.get(
            url=f"https://api.tomorrow.io/v4/weather/forecast?location=RU-TA&timesteps=1d&apikey=gUV9cyqDoLGF5p6Y8VjSb0CqmdGTYEVs",
            headers=headers)
        self.assertEqual(200, response.status_code)

    def test_get_forecast_for_day_given_RU_VGG_then_correct(self):
        headers = {"accept": "application/json"}
        response = requests.get(
            url=f"https://api.tomorrow.io/v4/weather/forecast?location=RU-VGG&timesteps=1d&apikey=gUV9cyqDoLGF5p6Y8VjSb0CqmdGTYEVs",
            headers=headers)
        self.assertEqual(200, response.status_code)

    def test_get_forecast_for_day_given_AE_DU_then_correct(self):
        headers = {"accept": "application/json"}
        response = requests.get(
            url=f"https://api.tomorrow.io/v4/weather/forecast?location=AE-DU&timesteps=1d&apikey=gUV9cyqDoLGF5p6Y8VjSb0CqmdGTYEVs",
            headers=headers)
        self.assertEqual(200, response.status_code)

    def test_get_forecast_for_day_given_US_CA_then_correct(self):
        headers = {"accept": "application/json"}
        response = requests.get(
            url=f"https://api.tomorrow.io/v4/weather/forecast?location=US-CA&timesteps=1d&apikey=gUV9cyqDoLGF5p6Y8VjSb0CqmdGTYEVs",
            headers=headers)
        self.assertEqual(200, response.status_code)
