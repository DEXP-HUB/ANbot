from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from Requests.get_date_site import ParsingDiary
from keyboards import categories_button


category_participant = Router()


@category_participant.callback_query(F.data == 'get_dilay_planner')
async def delay_planner(call: CallbackQuery):
    dairy = ParsingDiary('https://na-russia.org/')
    await call.message.answer(text=dairy.visual_diary())


@category_participant.callback_query(F.data == 'categories_in_participant')
async def post_categories_participant(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open('TextFiles/what_is_an.txt', 'r').read()))


@category_participant.callback_query(F.data == 'get_community_principles')
async def community_principles(call: CallbackQuery):
    (await call.message.answer(text=open('TextFiles/twelve_steps_an.txt', 'r').read()),
     await call.message.answer(text=open('TextFiles/twelve_tradition_an.txt', 'r').read()),
     await call.message.answer(text=open('TextFiles/twelve_ministries_an.txt', 'r').read()))



