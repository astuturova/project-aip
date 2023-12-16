import asyncio
import logging
from datetime import date, timedelta
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from utils import KeyboardConstructor, ForecastService, MessageConstructor

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token)
dp = Dispatcher()
keyboard_constructor = KeyboardConstructor()
forecast_service = ForecastService()
messageConstructor = MessageConstructor()
settings = {}


@dp.message(Command("start"))
async def cmd_random(message: types.Message):
    """Описание функции
    Обработчик команды /start. Принимает входящее сообщение и отвечает ему сообщением с выбором опций.
    Инициализирует глобальную переменную settings.

    Args:
        message (types.Message): входящее сообщение

    Raises:
        ValueError: Если возникает проблема с аргументами.

    """
    chat_id = message.chat.id
    settings[chat_id] = {
        'region': "RU-MOW",
        'timer': 86400,
        "time": 86400
    }
    await message.answer(
        "Привет, я бот, составляющий прогноз погоды",
        reply_markup=keyboard_constructor.get_menu_keyboard()
    )


@dp.callback_query(F.data.startswith("forecast_"))
async def callbacks_num(callback: types.CallbackQuery):
    """Описание функции
    Обработчик нажатия кнопок, относящихся к прогнозу погоды: на сегодня, завтра и на неделю.
    Получает данные из forecast_service, генерирует итоговое сообщение для ответа и изменяет текст сообщения бота.

    Args:
        callback (types.CallbackQuery): ID нажатой кнопки

    Raises:
        ValueError: Если возникает проблема с аргументами.

    """
    action = callback.data.split("_")[1]
    chat_id = callback.message.chat.id
    message = ""
    if action == "tomorrow":
        data = forecast_service.get_forecast_for_day(settings[chat_id]['region'], date.today() + timedelta(days=1))
        message = messageConstructor.get_output_message_for_day(data, "завтра")
    elif action == "today":
        data = forecast_service.get_forecast_for_day(settings[chat_id]['region'], date.today())
        message = messageConstructor.get_output_message_for_day(data, "сегодня")
    elif action == "week":
        data = forecast_service.get_forecast_for_week(settings[chat_id]['region'])
        message = messageConstructor.get_output_message_for_week(data)
    await update_message(callback.message, message)
    await callback.answer()


@dp.callback_query(F.data.startswith("set_"))
async def callbacks_num(callback: types.CallbackQuery):
    """Описание функции
    Обработчик нажатия кнопок, относящихся к настройке бота: таймер и регион.
    Изменяет сообщение бота в соответствии с выбранной настройкой.

    Args:
        callback (types.CallbackQuery): ID нажатой кнопки

    Raises:
        ValueError: Если возникает проблема с аргументами.

    """
    action = callback.data.split("_")[1]

    if action == "region":
        await update_message_to_region_settings(callback.message)
    elif action == "timer":
        await update_message_to_timer_settings(callback.message)

    await callback.answer()


@dp.callback_query(F.data.startswith("region_"))
async def callbacks_num(callback: types.CallbackQuery):
    """Описание функции
    Обработчик нажатия кнопок, относящихся к выбору региона.
    В соответсвии с выбранным регионом изменяет параметр region в глобальной переменной settings.
    Получает данные из forcast_service, генерирует новый прогноз погоды в нужном регионе и изменяет текст сообщения бота.

    Args:
        callback (types.CallbackQuery): ID нажатой кнопки

    Raises:
        ValueError: Если возникает проблема с аргументами.

    """
    action = callback.data.split("_")[1]
    chat_id = callback.message.chat.id

    if action == "moscow":
        settings[chat_id]['region'] = "RU-MOW"
    elif action == "petersburg":
        settings[chat_id]['region'] = "RU-SPE"
    elif action == "kazan":
        settings[chat_id]['region'] = "RU-TA"
    elif action == "volgograd":
        settings[chat_id]['region'] = "RU-VGG"
    elif action == "dubai":
        settings[chat_id]['region'] = "AE-DU"
    elif action == "san-francisco":
        settings[chat_id]['region'] = "US-CA"

    data = forecast_service.get_forecast_for_day(settings[chat_id]['region'], date.today())
    message = messageConstructor.get_output_message_for_day(data, "сегодня")
    await update_message(callback.message, message)

    await callback.answer()


@dp.callback_query(F.data.startswith("timer_"))
async def callbacks_num(callback: types.CallbackQuery):
    """"Описание функции
    Обработчик нажатия кнопок, относящихся к настройке таймера.
    В соответсвии с выбранным интервалом изменяет параметр timer и time в глобальной переменной settings.
    Получает данные из forcast_service, генерирует новый прогноз погоды с выбранным интервалом и изменяет текст сообщения бота.

    Args:
        callback (types.CallbackQuery): ID нажатой кнопки

    Raises:
        ValueError: Если возникает проблема с аргументами.

    """
    action = callback.data.split("_")[1]
    chat_id = callback.message.chat.id

    if action == "minute":
        settings[chat_id]['timer'] = 60
        settings[chat_id]['time'] = 60
    elif action == "hour":
        settings[chat_id]['timer'] = 3600
        settings[chat_id]['time'] = 3600
    elif action == "day":
        settings[chat_id]['timer'] = 43200
        settings[chat_id]['time'] = 43200
    elif action == "cycle":
        settings[chat_id]['timer'] = 86400
        settings[chat_id]['time'] = 86400

    data = forecast_service.get_forecast_for_day(settings[chat_id]['region'], date.today())
    message = messageConstructor.get_output_message_for_day(data, "сегодня")
    await update_message(callback.message, message)
    await callback.answer()


async def update_message(message: types.Message, new_value: str):
    """Описание функции
    Изменяет текст сообщения бота. Устанавливает в качестве нового значения new_value.

    Args:
        message (types.Message): ID нажатой кнопки
        new_value (str): новый текст сообщения, содержащий прогноз погоды

    Raises:
        ValueError: Если возникает проблема с аргументами.

    """
    with suppress(TelegramBadRequest):
        await message.edit_text(
            new_value,
            reply_markup=keyboard_constructor.get_menu_keyboard()
        )


async def update_message_to_region_settings(message: types.Message):
    """Описание функции
    Изменяет текст сообщения бота. Устанавливает в качестве нового значения текст, предлагающий выбрать регион.

    Args:
        message (types.Message): ID нажатой кнопки

    Raises:
        ValueError: Если возникает проблема с аргументами.

    """
    with suppress(TelegramBadRequest):
        await message.edit_text(
            "Выберите регион:",
            reply_markup=keyboard_constructor.get_region_settings_keyboard()
        )


async def update_message_to_timer_settings(message: types.Message):
    """Описание функции
    Изменяет текст сообщения бота. Устанавливает в качестве нового значения текст, предлагающий изменить таймер.

    Args:
        message (types.Message): ID нажатой кнопки

    Raises:
        ValueError: Если возникает проблема с аргументами.

    """
    with suppress(TelegramBadRequest):
        await message.edit_text(
            "Настройте таймер:",
            reply_markup=keyboard_constructor.get_timer_settings_keyboard()
        )


async def send_message_interval():
    """Описание функции
    функуия, которая работает в фоне. Каждую минуту проверяет, должна ли она посылать уведомление о текущей погоде определённому
    пользователю. Уменьшает параметр time переменной settins на 60 секунд. Если time будет равен нулю, то присылает уведомление о
    текущей погоде и устанавливает time в значении переменной timer.

    """
    while True:
        await asyncio.sleep(60)
        for key in settings.keys():
            settings[key]["time"] -= 60
            if settings[key]["time"] == 0:
                data = forecast_service.get_forecast_for_day(settings[key]['region'], date.today())
                message = messageConstructor.get_output_message_for_day(data, "сегодня")
                await bot.send_message(key, text=message, reply_markup=keyboard_constructor.get_menu_keyboard())
            settings[key]["time"] = settings[key]["timer"]


async def main():
    """Описание функции
    Запускает бота и фоновый процесс send_message_interval.

    """
    loop = asyncio.get_event_loop()
    t1 = loop.create_task(send_message_interval())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
