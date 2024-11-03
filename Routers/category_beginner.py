from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from keyboards import categories_button


category_beginner = Router()


@category_beginner.callback_query(F.data == 'get_about_an')
async def about_an(call: CallbackQuery):
    await call.message.answer(text=open('TextFiles/about_an.txt', 'r').read())


@category_beginner.callback_query(F.data == 'get_what_happens_an')
async def what_happens_an(call: CallbackQuery):
    await call.message.answer(text=open('TextFiles/what_happens_an.txt', 'r').read())


@category_beginner.callback_query(F.data == 'get_questions_answers')
async def questions_answers(call: CallbackQuery):
    await call.message.answer(text=open('TextFiles/questions_answers.txt', 'r').read())


@category_beginner.callback_query(F.data == 'categories_in_beginner')
async def post_categories_beginner(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open('TextFiles/what_is_an.txt', 'r').read()))

