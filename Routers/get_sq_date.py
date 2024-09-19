import sqlite3 as sq
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from filters_bot import IsAdmin

router_sq_date = Router()


@router_sq_date.message(Command('date'), IsAdmin(6320259544))
async def get_user_date(message: Message):
    with sq.connect('user.db') as sq_file:
        cur = sq_file.cursor()
        date = cur.execute('''SELECT * FROM user_date''').fetchall()

        for i in date:
            await message.answer(text=f'Пользователь: {i[0]}, ID пользователя: {i[1]}, Отправил: {i[2]}, Время: {i[3]}')


