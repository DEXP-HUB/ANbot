import asyncio
import sqlite3
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import categories_button, beck_feed_back


feed_back_router = Router()


class FeedBack(StatesGroup):
    user_message = State()


async def write_date(message: Message):
    with sqlite3.connect("DataBase/feed_back.db") as write:
        user = message.from_user
        write.cursor()
        write.execute("""INSERT INTO feed_back (first_name, last_name, user_name, message_text)
        VALUES (?, ?, ?, ?)""", (user.first_name, user.last_name, user.username, message.text))
        write.commit()


async def edit_feed_back(bot: Bot, state: FSMContext, message: Message):
    user_message = await state.get_data() 
    await bot.edit_message_media(
        message_id=user_message['message_id'], chat_id=message.chat.id,
        media=InputMediaPhoto(caption='Спасибо за ваши идеи. Мы ценим это.',
                              media=FSInputFile(filename='banner-2.jpg',
                                                      path='Photo/banner-2.jpg'))
    )
    await asyncio.sleep(2)
    await message.delete()
    await bot.delete_message(chat_id=message.chat.id, message_id=user_message['message_id'])


@feed_back_router.callback_query(F.data == 'feed_back')
async def offers_update_bot(call: CallbackQuery, state: FSMContext):
    await call.message.edit_caption(caption='Опишите ваши идеи по улучшению этого бота.',
                                    reply_markup=beck_feed_back())
    await state.set_state(FeedBack.user_message)
    await state.update_data(message_id=call.message.message_id)


@feed_back_router.message(FeedBack.user_message)
async def working_on_answer(message: Message, state: FSMContext, bot: Bot):
    await write_date(message)
    await edit_feed_back(bot, state, message)
    await bot.send_photo(
        reply_markup=categories_button(),
        photo=FSInputFile(filename='banner-2.jpg', path='Photo/banner-2.jpg'),
        caption=open('TextFiles/what_is_an.txt', 'r').read(), chat_id=message.chat.id
    )
    await state.clear()


@feed_back_router.callback_query(F.data == 'back_category')
async def back_category(call: CallbackQuery, state: FSMContext):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(filename='banner-2.jpg', path='Photo/banner-2.jpg'),
        caption=open('TextFiles/what_is_an.txt', 'r').read()))
    await state.clear()
