import sqlite3
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


feed_back_router = Router()


class FeedBack(StatesGroup):
    user_date = State()


@feed_back_router.callback_query(F.data == 'feed_back')
async def start_fsm(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text='Опишите ваше предложение по улучшению этого бота.')
    await state.set_state(FeedBack.user_date)


@feed_back_router.message()
async def add_date_state(message: Message, state: FSMContext):
    with sqlite3.connect("DateBase\\feed_back.db") as write_date:
        user = message.from_user
        write_date.cursor()
        write_date.execute("""INSERT INTO feed_back (first_name, last_name, user_name, message_text)
         VALUES (?, ?, ?, ?)""", (user.first_name, user.last_name, user.username, message.text))
        write_date.commit()

    await state.clear()
    await message.answer(text='Спасибо за вашу обратную связь, мы обязательно учтём это.')







