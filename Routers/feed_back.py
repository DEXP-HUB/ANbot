import sqlite3
from aiogram import Router, F
from aiogram.types import (CallbackQuery, BufferedInputFile, InputMediaPhoto, InlineKeyboardMarkup,
                           InlineKeyboardButton, Message)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Photo.read_file_in_photo import read_banner
from TextFiles.read_files import read_what_is_an
from keyboards import categories_button

feed_back_router = Router()


class FeedBack(StatesGroup):
    user_date = State()


@feed_back_router.callback_query(F.data == 'feed_back')
async def start_fsm(call: CallbackQuery, state: FSMContext):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='<<Назад', callback_data="back_category")]])
    await call.message.edit_media(reply_markup=keyboard, media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_banner(), filename='banner-2.jpg'),
        caption='Опишите ваше предложение по улучшению этого бота.'))
    await state.set_state(FeedBack.user_date)


@feed_back_router.message(FeedBack.user_date)
async def add_date_state(message: Message, state: FSMContext):
    with sqlite3.connect("DateBase\\feed_back.db") as write_date:
        user = message.from_user
        write_date.cursor()
        write_date.execute("""INSERT INTO feed_back (first_name, last_name, user_name, message_text)
         VALUES (?, ?, ?, ?)""", (user.first_name, user.last_name, user.username, message.text))
        write_date.commit()
    await state.clear()
    await message.answer('Спасибо за вашу обратную связь.')


@feed_back_router.callback_query(F.data == 'back_category')
async def back_category(call: CallbackQuery, state: FSMContext):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_banner(), filename='banner-2.jpg'),
        caption=read_what_is_an()))
    await state.clear()



