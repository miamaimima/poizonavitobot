from aiogram.types import Message, CallbackQuery
import json
from aiogram.filters import Command
from lexicon.lexicon import LEXICON_RU
from aiogram import F
from aiogram import Router
from filters.inchat import IsNotSubscriber, IsAdmin
from keyboards.keyboard import menu
from main import bot, config
router = Router()


JSON_FILE_PATH = 'managers.json'
is_admin = IsAdmin(bot=bot, channel_id=config.tgbot.channel_id)
is_not_subscriber = IsNotSubscriber(bot=bot, channel_id=config.tgbot.channel_id)





@router.message(Command(commands='manager'), (is_admin))
async def mng(message: Message):
    await message.answer(text=LEXICON_RU['manager'])
    user_data = message.from_user.id
    try:
        with open(JSON_FILE_PATH, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    if user_data not in data:
        data.append(user_data)
        with open(JSON_FILE_PATH, 'w') as f:
            json.dump(data, f)


@router.callback_query(F.data.in_(['examitioncheck']), ~(is_not_subscriber))
async def subscribe(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['notsubs'],
        reply_markup=menu)
    await callback.message.delete()
    
@router.callback_query(F.data.in_(['examitioncheck']))
async def notsubscribe(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['subs'],
        reply_markup=callback.message.reply_markup
    )
    


    
