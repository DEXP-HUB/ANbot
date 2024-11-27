from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import Filter
from aiogram.types import Message


class CheckState(Filter):
    async def __call__(self, message: Message,  bot: Bot, state: FSMContext) -> bool:
        self.message_id = await state.get_data()
        if not self.message_id.get('message_id') is None:
            await bot.delete_message(chat_id=message.chat.id, message_id=self.message_id['message_id'])
            state.get_state().close()
        return True
        