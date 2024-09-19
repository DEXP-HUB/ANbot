import asyncio
import logging
import sys
import datetime
import sqlite3 as sq
from aiogram import Bot, Dispatcher
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from Photo.read_file_in_photo import read_banner
from keyboards import categories_button
from Routers.keyboards_category import keyboards_category
from Routers.sub_categories import category_participant, category_beginner
from Routers.get_sq_date import router_sq_date
from TextFiles.read_files import read_what_is_an

bot = Bot(
    token='',
    default=DefaultBotProperties(parse_mode='HTML'),
)
dp = Dispatcher()
dp.include_routers(keyboards_category, category_participant, category_beginner, router_sq_date)


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.answer_photo(caption=read_what_is_an(), photo=BufferedInputFile(
        filename='Программа АН', file=read_banner()), reply_markup=categories_button())

    with sq.connect('user.db') as sq_file:
        ms = message
        con = sq_file.cursor()
        time = datetime.datetime.now().strftime('%H:%M:%S')
        con.execute('''INSERT INTO user_data (name, id, button, datatime) VALUES (?, ?, ?, ?)''',
                    (ms.from_user.username, ms.from_user.id, ms.text, time))


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    asyncio.run(main())
