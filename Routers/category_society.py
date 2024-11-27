from aiogram import Router, F
from aiogram.filters import or_f
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from keyboards import categories_button, about_an_sc_buttons, society_category


category_society = Router()


@category_society.callback_query(F.data == 'categories_in_society')
async def post_categories_society(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open('TextFiles/what_is_an.txt', 'r').read()))


@category_society.callback_query(or_f(F.data == 'community_an_sc', F.data == 'target_an_sc', F.data == 'participation_an_sc',
                                      F.data == 'meetings_an_sc', F.data == 'program_an_sc', F.data == 'religion_an_sc'))
async def category_about_an(call: CallbackQuery):
    text = open(file='TextFiles/about_an.txt', mode='r').read().split('\n')
    category = {'community_an_sc': text[2], 'target_an_sc': text[6], 'participation_an_sc': text[10],
                'meetings_an_sc': text[14], 'program_an_sc': text[18], 'religion_an_sc': text[22]}
    await call.message.edit_caption(reply_markup=about_an_sc_buttons(), caption=category[call.data])


@category_society.callback_query(F.data == 'back_about_an_sc')
async def back_about_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=society_category(),
        caption='Наша политика в связях с общественностью строится не на рекламе, а на привлекательности; нам нужно'
                ' всегда сохранять личную анонимность на уровне средств массовой информации.'
        )


@category_society.callback_query(F.data == 'get_about_an_in_society')
async def about_an(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=about_an_sc_buttons())