from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram import Bot

class IsNotSubscriber(BaseFilter):
    def __init__(self, bot: Bot, channel_id: str):
        self.bot = bot
        self.channel_id = channel_id

    async def __call__(self, message: Message) -> bool:
        chat_member = await self.bot.get_chat_member(chat_id=self.channel_id, user_id=message.from_user.id)
        return chat_member.status not in ('member', 'administrator', 'creator')



class IsAdmin(BaseFilter):
    def __init__(self, bot: Bot, channel_id: str):
        self.bot = bot
        self.channel_id = channel_id

    async def __call__(self, message: Message) -> bool:
        chat_member = await self.bot.get_chat_member(chat_id=self.channel_id, user_id=message.from_user.id)
        return chat_member.status in ('administrator', 'creator')
    
    
    
