import asyncio
import logging
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import config
from utils import KeyboardConstructor

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token)
dp = Dispatcher()
keyboard_constructor = KeyboardConstructor()


# Отклик на команду старт
@dp.message(Command("start"))
async def cmd_random(message: types.Message):
    await message.answer(
        "Привет, я бот, составляющий проноз погоды",
        reply_markup=keyboard_constructor.get_keyboard()
    )


# Отклик на кнопки "Прогноз погоды на завтра" и "Прогноз погоды на сегодня"
@dp.callback_query(F.data.startswith("forecast_"))
async def callbacks_num(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]

    if action == "tomorrow":
        await update_message(callback.message, "Прогноз погоды на завтра")
    elif action == "today":
        await update_message(callback.message, "Прогноз погоды на сегодня")

    await callback.answer()

# Отклик на кнопки "Прогноз погоды на завтра" и "Прогноз погоды на сегодня"
@dp.callback_query(F.data.startswith("set_"))
async def callbacks_num(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]

    if action == "region":
        await update_message(callback.message, "Выбрана настройка региона")
    elif action == "timer":
        await update_message(callback.message, "Выбрана настройка таймера")

    await callback.answer()


# Эта функция обновляет текст сообщения
async def update_message(message: types.Message, new_value: str):
    with suppress(TelegramBadRequest):
        await message.edit_text(
            new_value,
            reply_markup=keyboard_constructor.get_keyboard()
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
