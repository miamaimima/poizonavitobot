from aiogram.types import Message, FSInputFile
from lexicon.lexicon import LEXICON_RU
from aiogram import Router
from keyboards.keyboard import menu
router = Router()


@router.message(lambda message: message.text == '💬Отзывы')
async def otzivi(message: Message):
    await message.answer_photo(photo=FSInputFile('photo/otzivi.png'), caption=LEXICON_RU['otzivi'])
    
@router.message(lambda message: message.text == '🚚Менеджер')
async def otzivi(message: Message):
    await message.answer(text=LEXICON_RU['managers'])