from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InputMediaPhoto, FSInputFile
from templates_messages import GetBeginner, GetParticipant, GetSociety


main_category = Router()


@main_category.callback_query(F.data == 'get_beginner')
async def send_beginner_category(call: CallbackQuery):
    await call.message.edit_media(reply_markup=GetBeginner.MARKUP, media=InputMediaPhoto(
        type=GetBeginner.MEDIA_TYPE, media=FSInputFile(path=GetBeginner.PHOTO_PATH, filename=GetBeginner.PHOTO_NAME),
        caption=GetBeginner.CAPTION))


@main_category.callback_query(F.data == 'get_participant')
async def send_participant_category(call: CallbackQuery):
    await call.message.edit_media(reply_markup=GetParticipant.MARKUP, media=InputMediaPhoto(
        type=GetParticipant.MEDIA_TYPE, media=FSInputFile(path=GetParticipant.PHOTO_PATH, filename=GetParticipant.PHOTO_NAME),
        caption=GetParticipant.CAPTION))


@main_category.callback_query(F.data == 'get_an_in_society')
async def send_society_category(call: CallbackQuery):
    await call.message.edit_media(reply_markup=GetSociety.MARKUP, media=InputMediaPhoto(
        type=GetSociety.MEDIA_TYPE, media=FSInputFile(path=GetSociety.PHOTO_PATH, filename=GetSociety.PHOTO_NAME),
        caption=GetSociety.CAPTION))

