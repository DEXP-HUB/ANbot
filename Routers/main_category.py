from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InputMediaPhoto, BufferedInputFile
from keyboards import beginner_category, participant_category, society_category
from Photo.read_file_in_photo import read_beginner_category, read_participant_category, read_society_category


main_category = Router()


@main_category.callback_query(F.data == 'get_beginner')
async def send_beginner_category(call: CallbackQuery):
    await call.message.edit_media(reply_markup=beginner_category(), media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_beginner_category(), filename='banner-2.jpg'),
        caption='У каждой группы сообщества «Анонимные Наркоманы» есть лишь одна главная цель — предоставить информацию'
                ' о возможности выздоровления тем, кто еще употребляет наркотики и страдает от зависимости.'))


@main_category.callback_query(F.data == 'get_participant')
async def send_participant_category(call: CallbackQuery):
    await call.message.edit_media(reply_markup=participant_category(), media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_participant_category(), filename='participant.jpg'),
        caption='Наше общее благополучие важнее всего, от единства АН зависит личное выздоровление каждого.'))


@main_category.callback_query(F.data == 'get_an_in_society')
async def send_society_category(call: CallbackQuery):
    await call.message.edit_media(reply_markup=society_category(), media=InputMediaPhoto(
        type='photo', media=BufferedInputFile(file=read_society_category(), filename='society.jpg'),
        caption='Наша политика в связях с общественностью строится не на рекламе, а на привлекательности; нам нужно'
                ' всегда сохранять личную анонимность на уровне средств массовой информации.'))

