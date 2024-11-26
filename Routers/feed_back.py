import asyncio
from sqlalchemy.orm import Session
from aiogram.filters import and_f, invert_f
from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import categories_button, beck_feed_back
from DataBase.feed_back_model import UserFeedBack, engine



feed_back_router = Router()


class FeedBack(StatesGroup):
    user_message = State()


async def write_date(message: Message):
    with Session(engine) as session:
        feed_back = UserFeedBack(
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            url_name=message.from_user.username,
            message_text=message.text
        )
        session.add(feed_back)
        session.commit()


async def edit_feed_back(bot: Bot, message: Message, state: FSMContext):
    user_message = await state.get_data()

    await bot.edit_message_media(
        message_id=user_message['message_id'], chat_id=message.chat.id,
        media=InputMediaPhoto(caption='Спасибо за ваши идеи. Мы ценим это.', 
        media=FSInputFile(filename='banner-2.jpg', path='Photo/banner-2.jpg'))
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


@feed_back_router.message(and_f(FeedBack.user_message, invert_f(F.text)))
async def message_not_text(message: Message, state: FSMContext, bot: Bot):
    user_message = await state.get_data()

    try:
        await bot.edit_message_media(
            chat_id=message.chat.id,
            reply_markup=beck_feed_back(),
            message_id=user_message['message_id'], 
            media=InputMediaPhoto(
                caption='В качестве обратной связи можно отправлять только текст!!!', 
                media=FSInputFile(filename='banner-2.jpg', path='Photo/banner-2.jpg')
                )
            )
        await message.delete()

    except TelegramBadRequest:
        await message.delete()


@feed_back_router.message(and_f(FeedBack.user_message, F.text))
async def working_on_answer(message: Message, state: FSMContext, bot: Bot):
    await write_date(message)
    await edit_feed_back(bot, message, state)

    await bot.send_photo(
        reply_markup=categories_button(),
        caption=open('TextFiles/what_is_an.txt', 'r').read(), chat_id=message.chat.id,
        photo=FSInputFile(filename='banner-2.jpg', path='Photo/banner-2.jpg'),
    )

    await state.clear()


@feed_back_router.callback_query(F.data == 'back_category')
async def back_category(call: CallbackQuery, state: FSMContext):
    await call.message.edit_media(
            reply_markup=categories_button(), 
            media=InputMediaPhoto(
                type='photo', 
                caption=open('TextFiles/what_is_an.txt', 'r').read(),
                media=FSInputFile(
                    filename='banner-2.jpg', 
                    path='Photo/banner-2.jpg')))
    
    await state.clear()
