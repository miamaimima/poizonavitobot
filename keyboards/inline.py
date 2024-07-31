from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


subscribe = InlineKeyboardButton(
    text='Подписаться!',
    url='https://t.me/POIZONmarketskhv'
)

examination = InlineKeyboardButton(
    text='Проверка подписки',
    callback_data='examitioncheck'
)

keyboardonstart = InlineKeyboardMarkup(
    inline_keyboard=[[subscribe], [examination]]
)

clothing = InlineKeyboardButton(
    text='Одежда👘',
    callback_data='clothing'
)
shoes = InlineKeyboardButton(
    text='Кроссовки👟',
    callback_data='shoes'
)


keyboardcalc = InlineKeyboardMarkup(
    inline_keyboard=[[clothing], [shoes]]
)