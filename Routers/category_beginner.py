from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto, BufferedInputFile
from Photo.read_file_in_photo import read_banner
from TextFiles.read_files import read_about_an, read_what_happens_an, read_questions_answers, read_what_is_an
from keyboards import categories_button


category_beginner = Router()


@category_beginner.callback_query(F.data == 'get_about_an')
async def about_an(call: CallbackQuery):
    await call.message.answer(text=read_about_an())


@category_beginner.callback_query(F.data == 'get_what_happens_an')
async def what_happens_an(call: CallbackQuery):
    await call.message.answer(text=read_what_happens_an())


@category_beginner.callback_query(F.data == 'get_questions_answers')
async def questions_answers(call: CallbackQuery):
    await call.message.answer(text=read_questions_answers())


@category_beginner.callback_query(F.data == 'categories_in_beginner')
async def post_categories_beginner(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_banner(), filename='Программа АН'),
        caption=read_what_is_an()))

