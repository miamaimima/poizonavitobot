import asyncio
from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.types import FSInputFile, Message
from keyboards.keyboard import bwd, menu, menusback, diliverykeyboard1, diliverykeyboard2, diliverykeyboard3, diliverykeyboard4, diliverykeyboard5
from lexicon.lexicon import LEXICON_RU

router = Router()

class FSMFillPrice(StatesGroup):
    deliveryst = State()
    producttype = State()
    modifstate = State()
    value = State()

pricedict = {}

@router.message((lambda message: message.text == 'Отменить⛔️'), ~(StateFilter(default_state)))
async def backward(message: Message, state: FSMContext):
    await message.answer(text='Будем ждать вас снова!', reply_markup=menu)
    await state.clear()

@router.message(lambda message: message.text == 'Меню📃')
async def onmenu(message: Message, state: FSMContext):
    await message.answer_photo(photo=FSInputFile('photo/menu.jpg'), caption=LEXICON_RU['help'], reply_markup=menu)
    await state.clear()

@router.message(lambda message: message.text == '📝Рассчитать стоимость заказа', StateFilter(default_state))
async def deliveryy(message: Message, state: FSMContext):
    await message.answer_photo(caption=LEXICON_RU['diliver'], photo=FSInputFile('photo/image.png'), reply_markup=diliverykeyboard1)
    await state.set_state(FSMFillPrice.deliveryst)

@router.message(lambda message: message.text == 'Обычная доставка🚛 (14 - 18 дней)', StateFilter(FSMFillPrice.deliveryst))
async def tovarchik(message: Message, state: FSMContext):
    await state.update_data(deliverys=0)
    await message.answer(text=LEXICON_RU['category'], reply_markup=diliverykeyboard2)
    await state.set_state(FSMFillPrice.producttype)

@router.message(lambda message: message.text == 'Авиа доставка🛩 (3 - 5 дней)', StateFilter(FSMFillPrice.deliveryst))
async def tovarchik2(message: Message, state: FSMContext):
    await state.update_data(deliverys=1)
    await message.answer(text=LEXICON_RU['category'], reply_markup=diliverykeyboard2)
    await state.set_state(FSMFillPrice.producttype)

@router.message(lambda message: message.text in ['Кроссовки👟', 'Одежда👘', 'Техника📱', 'Другое🟢'], StateFilter(FSMFillPrice.producttype))
async def viz(message: Message, state: FSMContext):
    product_type = message.text
    await state.update_data(product_type=product_type)
    if product_type == 'Кроссовки👟':
        await state.set_state(FSMFillPrice.value)
        await message.answer(text=LEXICON_RU['price'], reply_markup=menusback)
    elif product_type == 'Одежда👘':
        await message.answer(text=LEXICON_RU['productt'], reply_markup=diliverykeyboard5)
        await state.set_state(FSMFillPrice.modifstate)
    elif product_type == 'Техника📱':
        await message.answer(text=LEXICON_RU['productt'], reply_markup=diliverykeyboard4)
        await state.set_state(FSMFillPrice.modifstate)
    elif product_type == 'Другое🟢':
        await message.answer(text=LEXICON_RU['productt'], reply_markup=diliverykeyboard3)
        await state.set_state(FSMFillPrice.modifstate)

        
@router.message(StateFilter(FSMFillPrice.modifstate), lambda message: message.text in [
    'Кольцо/часы💍', 'Косметика🧴', 'Мяч⚽️',
    'Ноутбук/компьютер🖥', 'Наушники/клавиатура⌨️', 'Мышка/коврик для мыши🖱', 'Телефон📱', 'Приставка🎮', 'Камера📷',
    'Куртка🧥', 'Футболка/носки👕🧦', 'Кофта/штаны👖', 'Сумка/рюкзак👝'
])
async def modific(message: Message, state: FSMContext):
    await state.set_state(FSMFillPrice.value)
    await message.answer(text=LEXICON_RU['price'], reply_markup=menusback)
@router.message(StateFilter(FSMFillPrice.value), lambda message: message.text.isdigit())
async def value(message: Message, state: FSMContext):
    await state.update_data(values=message.text)
    pricedict[message.from_user.id] = await state.get_data()
    prices = int(pricedict[message.from_user.id]['values'])
    if pricedict[message.from_user.id]['deliverys'] == 1:
        gottetprice = round(prices * 14 + prices * 0.4 * 14 + 1500, 1)
        await message.answer_photo(photo=FSInputFile('photo/raschet.png'), caption=f'Итоговая цена составляет📈:\n\n<tg-spoiler>~{gottetprice} <b>руб</b></tg-spoiler> + 400 руб за КГ.\nПримечание:\n<b>Авиа доставка в три раза быстрее чем обычная</b>', reply_markup=menusback)
    if pricedict[message.from_user.id]['deliverys'] == 0:
        gottetprice = round(prices * 14 + prices * 0.4 * 14, 1)
        await message.answer_photo(photo=FSInputFile('photo/raschet.png'), caption=f'Итоговая цена составляет📈:\n\n<tg-spoiler>~{gottetprice} <b>руб</b></tg-spoiler> + 400 руб за КГ.\n', reply_markup=menusback)
    await state.clear()

@router.message(StateFilter(FSMFillPrice.value))
async def value_invalid(message: Message):
    await message.answer(text=LEXICON_RU['not_price'])
