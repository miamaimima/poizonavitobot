from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)



button1, button2, button3, button4 = KeyboardButton(text='📝Рассчитать стоимость заказа'), KeyboardButton(text='💳Заказать'), KeyboardButton(text='💬Отзывы'), KeyboardButton(text='🚚Менеджер')
menu = ReplyKeyboardMarkup(keyboard=[[button1], [button2], [button3, button4]], resize_keyboard=True)
button4, button5 = KeyboardButton(text='Продолжить🚀'), KeyboardButton(text='Отменить⛔️')
orderkeyboardone = ReplyKeyboardMarkup(keyboard=[[button4], [button5]], resize_keyboard=True)
bwd = ReplyKeyboardMarkup(keyboard=[[button5]], resize_keyboard=True)
button6 = KeyboardButton(text='Меню📃')
button7, button8, button9, button10 = KeyboardButton(text='Кроссовки👟'), KeyboardButton(text='Одежда👘'), KeyboardButton(text='Техника📱'), KeyboardButton(text='Другое🟢')
button11, button12 = KeyboardButton(text='Обычная доставка🚛 (14 - 18 дней)'), KeyboardButton(text='Авиа доставка🛩 (3 - 5 дней)')
diliverykeyboard1 = ReplyKeyboardMarkup(keyboard=[[button11], [button12]], resize_keyboard=True)
menusback = ReplyKeyboardMarkup(keyboard=[[button6]], resize_keyboard=True)
diliverykeyboard2 = ReplyKeyboardMarkup(keyboard=[[button7, button8], [button9], [button10], [button6]], resize_keyboard=True)
button13, button14, button15 = KeyboardButton(text='Кольцо/часы💍'), KeyboardButton(text='Косметика🧴'), KeyboardButton(text='Мяч⚽️')
button16, button17, button18, button19, button20, button21 = KeyboardButton(text='Ноутбук/компьютер🖥'), KeyboardButton(text='Наушники/клавиатура⌨️'), KeyboardButton(text='Мышка/коврик для мыши🖱'), KeyboardButton(text='Телефон📱'), KeyboardButton(text='Приставка🎮'), KeyboardButton(text='Камера📷')
button22, button23, button24, button25 = KeyboardButton(text='Куртка🧥'), KeyboardButton(text='Футболка/носки👕🧦'), KeyboardButton(text='Кофта/штаны👖'), KeyboardButton(text='Сумка/рюкзак👝')
diliverykeyboard3 = ReplyKeyboardMarkup(keyboard=[[button13], [button14], [button15]], resize_keyboard=True)
diliverykeyboard4 = ReplyKeyboardMarkup(keyboard=[[button16], [button17, button18], [button19, button20], [button21]], resize_keyboard=True)
diliverykeyboard5 = ReplyKeyboardMarkup(keyboard=[[button22, button23], [button24], [button25]], resize_keyboard=True)
