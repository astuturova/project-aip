from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Найстройка", callback_data="setting"),
    InlineKeyboardButton(text="Погода на сегодня", callback_data="weather_today")],
    [InlineKeyboardButton(text="Погода на завтра", callback_data="weathe_tomorrow"),
    InlineKeyboardButton(text="Поставить таймер", callback_data="set_timer")],
    [InlineKeyboardButton(text="Другие регионы", callback_data="change_region"),
    InlineKeyboardButton(text="Настроить уведомления", callback_data="set_notifications")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])