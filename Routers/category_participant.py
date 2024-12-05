from typing import Tuple
from aiogram import F, Router
from aiogram.filters import or_f
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from Requests.get_date_site import ParsingDiary
from keyboards import categories_button, principles_community, get_page


category_participant = Router()


async def get_path(dir: str, call_data: str) -> Tuple[str, int]:
    return {
        'steps_an': (f'{dir}/twelve_steps_an.txt', 620), 
        'tradition_an': (f'{dir}/twelve_tradition_an.txt', 996),
        'service_concepts': (f'{dir}/twelve_ministries_an.txt', 925)
        }[call_data]


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
    await call.message.edit_caption(
        reply_markup=principles_community(),
        caption='Наше общее благополучие важнее всего, от единства АН зависит личное выздоровление каждого.'
        )


@category_participant.callback_query(or_f(F.data == 'steps_an1', F.data == 'tradition_an1', 
                                          F.data == 'service_concepts1',
                                          F.data == 'steps_an2', F.data == 'tradition_an2', 
                                          F.data == 'service_concepts2'))
async def categories_principles(call: CallbackQuery):
    path, limit = await get_path('TextFiles', call.data[:-1])
    read_file = lambda path: open(path, 'r').read()
    caption = {'1': read_file(path)[:limit], '2': read_file(path)[limit:]}

    await call.message.edit_caption(
            caption=caption[call.data[-1]],
            reply_markup=get_page(call.data[:-1])
            )
    
   




