import asyncio
from aiogram import Bot, Dispatcher
from config import Config, load_config
from filters.inchat import IsNotSubscriber
from handlers import on_start, subscribe, order, calcprice, managersandotzivi
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram.client.default import DefaultBotProperties
from keyboards.inline import keyboardonstart


storage = MemoryStorage()



config: Config = load_config()
bot = Bot(token=config.tgbot.token, default=DefaultBotProperties(parse_mode='HTML'))

async def main() -> None:
    dp = Dispatcher(storage=storage)
    is_not_subscriber = IsNotSubscriber(bot=bot, channel_id=config.tgbot.channel_id)
    @dp.message(is_not_subscriber)
    async def not_subscribed_handler(message: Message):
        await message.delete()
        await message.answer(text=LEXICON_RU['unsubhelp'], reply_markup=keyboardonstart)

    dp.include_routers(subscribe.router, order.router, managersandotzivi.router,  calcprice.router, on_start.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
