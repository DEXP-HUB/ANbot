import asyncio
import logging
import sys
from aiogram.fsm.context import FSMContext
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from keyboards import categories_button
from Routers.main_category import main_category
from Routers.category_participant import category_participant
from Routers.category_beginner import category_beginner
from Routers.category_society import category_society
from Routers.feed_back import feed_back_router
from DataBase.create_database import create_table


bot = Bot(
    token='6431806104:AAEeWUWZSODI92Va87WbUQNDrVAXdql9KKA',
    default=DefaultBotProperties(parse_mode='HTML'),
)
dp = Dispatcher()
dp.include_routers(main_category, category_participant, category_beginner, feed_back_router, category_society)


@dp.message(CommandStart())
async def get_category(message: Message, state: FSMContext, bot: Bot):
    check_state = await state.get_data()

    if 'message_id' in check_state.keys():
        await bot.delete_message(chat_id=message.chat.id, message_id=check_state['message_id'])
        await state.clear()
        await message.delete()
        await message.answer_photo(caption=open('TextFiles/what_is_an.txt', 'r').read(), photo=FSInputFile(
            filename='banner-2.jpg', path='Photo/banner-2.jpg'), reply_markup=categories_button())

    else:
        await message.delete()
        await message.answer_photo(caption=open('TextFiles/what_is_an.txt', 'r').read(), photo=FSInputFile(
            filename='banner-2.jpg', path='Photo/banner-2.jpg'), reply_markup=categories_button())


async def main():
    create_table()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    asyncio.run(main())
