from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto, BufferedInputFile
from Photo.read_file_in_photo import read_banner
from TextFiles.read_files import read_what_is_an
from keyboards import categories_button


category_society = Router()


@category_society.callback_query(F.data == 'categories_in_society')
async def post_categories_society(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_banner(), filename='Программа АН'),
        caption=read_what_is_an()))
