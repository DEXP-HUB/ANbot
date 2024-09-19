from aiogram import F, Router
from aiogram.types import CallbackQuery, InputMediaPhoto, BufferedInputFile
from Photo.read_file_in_photo import read_banner, read_beginner_category, read_what_happens_an_p
from Requests.get_date_site import ParsingDiary
from TextFiles.read_files import *
from keyboards import categories_button, beginner_category


category_beginner = Router()
category_participant = Router()


@category_beginner.callback_query(F.data == 'get_about_an')
async def about_an(call: CallbackQuery):
    await call.message.answer(text=read_about_an())


@category_beginner.callback_query(F.data == 'get_what_happens_an')
async def what_happens_an(call: CallbackQuery):
    await call.message.answer(text=read_what_happens_an())


@category_beginner.callback_query(F.data == 'get_questions_answers')
async def questions_answers(call: CallbackQuery):
    await call.message.answer(text=read_questions_answers())


@category_participant.callback_query(F.data == 'get_dilay_planner')
async def delay_planner(call: CallbackQuery):
    dairy = ParsingDiary('https://na-russia.org/')
    await call.message.answer(text=dairy.visual_diary())


@category_participant.callback_query(F.data == 'get_community_principles')
async def community_principles(call: CallbackQuery):
    (await call.message.answer(text=read_twelve_steps_an()),
     await call.message.answer(text=read_twelve_tradition_an()),
     await call.message.answer(text=read_twelve_ministries_an()))


@category_beginner.callback_query(F.data == 'categories_in_beginner')
async def post_categories_beginner(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_banner(), filename='Программа АН'),
        caption=read_what_is_an()))


@category_beginner.callback_query(F.data == 'categories_in_participant')
async def post_categories_participant(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_banner(), filename='Программа АН'),
        caption=read_what_is_an()))


@category_beginner.callback_query(F.data == 'categories_in_society')
async def post_categories_society(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_banner(), filename='Программа АН'),
        caption=read_what_is_an()))

