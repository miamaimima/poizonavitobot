from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.filters import StateFilter
from aiogram.types import Message, FSInputFile
from aiogram import Router
from keyboards.keyboard import orderkeyboardone, bwd, menu
from lexicon.lexicon import LEXICON_RU
import json



router = Router()

JSON_FILE_PATH = 'managers.json'


async def notification(user_data, jsonfilepath=JSON_FILE_PATH):
    from main import bot
    with open(jsonfilepath, 'r') as f:
        manager_ids = json.load(f)
        for manager in manager_ids:
            try:
                await bot.send_message(manager, text=f"Новый заказ:\n<b>Ссылка:</b>\n{user_data['productmessage']}\n<b>Дополнения:</b>\n<code>{user_data['modificationmessage']}</code>\n<b>Цена:</b>\n{user_data['pricemessage']}\n<b>Покупатель:</b> @{user_data['userid']}")
            except:
                pass

def write_to_json(data, file_path=JSON_FILE_PATH):
    with open(file_path, 'a') as f:
        json.dump(data, f)
        f.write('\n')

class FSMFillForm(StatesGroup):
    product = State()
    additions = State()
    price = State()
    managers = State()



@router.message(lambda message: message.text == "💳Заказать", StateFilter(default_state))
async def order(message: Message, state: FSMContext):
    if message.from_user.username != None:
        await message.answer(text=LEXICON_RU['order1'], reply_markup=orderkeyboardone)
        await state.set_state(FSMFillForm.product)
    if message.from_user.username == None:
        await message.answer_photo(caption=LEXICON_RU['order2'], reply_markup=menu, photo=FSInputFile('photo/us1.jpg'))

@router.message(lambda message: message.text == 'Продолжить🚀', StateFilter(FSMFillForm.product))
async def product(message: Message, state: FSMContext):
    await message.answer_photo(caption=LEXICON_RU['url'], reply_markup=bwd, photo=FSInputFile('photo/url.jpg'))
    await state.set_state(FSMFillForm.additions)


@router.message((lambda message: message.text == 'Отменить⛔️'), ~(StateFilter(default_state)))
async def backward(message: Message, state: FSMContext):
    await message.answer(text='Будем ждать вас снова!', reply_markup=menu)
    await state.clear()

@router.message(StateFilter(FSMFillForm.additions))
async def additions(message: Message, state: FSMContext):
    await state.update_data(productmessage=message.text)
    await message.answer_photo(caption=LEXICON_RU['modification'], photo=FSInputFile('photo/modification.png'))
    await state.set_state(FSMFillForm.price)

@router.message(StateFilter(FSMFillForm.price))
async def price(message: Message, state: FSMContext):
    await state.update_data(modificationmessage=message.text)
    await message.answer_photo(caption=LEXICON_RU['price'], photo=FSInputFile('photo/price.jpg'))
    await state.set_state(FSMFillForm.managers)


@router.message(StateFilter(FSMFillForm.managers), lambda message: message.text.isdigit())
async def managers(message: Message, state: FSMContext):
    await state.update_data(pricemessage=message.text)
    await message.answer_photo(caption=LEXICON_RU['gotovo'], reply_markup=menu, photo=FSInputFile('photo/gotovo.png'))
    user_data = await state.get_data()
    user_data['userid'] = message.from_user.username
    await notification(user_data=user_data)
    await state.clear()



@router.message(StateFilter(FSMFillForm.managers))
async def managers(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['not_price'])