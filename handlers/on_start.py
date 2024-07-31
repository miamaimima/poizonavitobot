from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboard import menu
from aiogram import Router
router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    photo = FSInputFile('photo/menu.jpg')
    await message.answer_photo(photo=FSInputFile('photo/menu.jpg'), caption=LEXICON_RU['help'], reply_markup=menu)
    await state.clear()



@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer_photo(photo=FSInputFile('photo/menu.jpg'), caption=LEXICON_RU['help'], reply_markup=menu)


@router.message()
async def unknow(message: Message):
    await message.answer(text=LEXICON_RU['unk'])