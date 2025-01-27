from os.path import join as path
from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from keyboards import categories_button, about_an_buttons, society_category


category_society = Router()


@category_society.callback_query(F.data == 'categories_in_society')
async def post_categories_society(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open(path('TextFiles', 'what_is_an.txt'), 'r').read()))


@category_society.callback_query(F.data == 'get_about_an_in_society')
async def about_an(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=about_an_buttons(back_button='back_about_an_sc'))


@category_society.callback_query(F.data == 'back_about_an_sc')
async def back_about_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=society_category(),
        caption='Наша политика в связях с общественностью строится не на рекламе, а на привлекательности; нам нужно'
                ' всегда сохранять личную анонимность на уровне средств массовой информации.'
        )


