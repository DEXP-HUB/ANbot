from aiogram import Router, F
from aiogram.filters import or_f
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from keyboards import categories_button, about_an_buttons


category_beginner = Router()


@category_beginner.callback_query(F.data == 'get_about_an')
async def about_an(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=about_an_buttons())


@category_beginner.callback_query(or_f(F.data == 'community_an', F.data == 'target_an', F.data == 'participation_an',
                                       F.data == 'meetings_an', F.data == 'program_an', F.data == 'religion_an'))
async def get_category(call: CallbackQuery):
    text = open(file='TextFiles/about_an.txt', mode='r').read().split('\n')
    category = {'community_an': text[2], 'target_an': text[6], 'participation_an': text[10],
              'meetings_an': text[14], 'program_an': text[18], 'religion_an': text[22]}
    await call.message.edit_caption(reply_markup=about_an_buttons(), caption=category[call.data])
    

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

