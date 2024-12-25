import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from filters import CheckState
from tokens import token_bot
from templates_messages import Start
from Routers.main_category import main_category
from Routers.category_participant import category_participant
from Routers.category_beginner import category_beginner
from Routers.category_society import category_society
from Routers.feed_back import feed_back_router
from DataBase.feed_back_model import Base, engine


bot = Bot(token=token_bot, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()
dp.include_routers(main_category, category_participant, category_beginner, feed_back_router, category_society)


@dp.message(CommandStart(), CheckState())
async def get_category(message: Message):
    await message.delete()
    await message.answer_photo(caption=Start.CAPTION, reply_markup=Start.MARKUP,
                               photo=FSInputFile(filename=Start.PHOTO_NAME, path=Start.PHOTO_PATH))

        
async def main():
    Base.metadata.create_all(engine)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_description(language_code='ru', description='Здравствуйте, этот телеграм-бот предназначен для того, чтобы помочь людям выздоравливать от наркотической зависимости. Через этого бота вы сможете узнать подробнее о сообществе "Анонимные Наркоманы".')
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        # filename='bot.log',
        # filemode='a',
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
              "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    asyncio.run(main())
