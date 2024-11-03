from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from keyboards import categories_button


category_society = Router()


@category_society.callback_query(F.data == 'categories_in_society')
async def post_categories_society(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open('TextFiles/what_is_an.txt', 'r').read()))
