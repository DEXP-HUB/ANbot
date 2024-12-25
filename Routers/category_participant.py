from typing import Tuple
from abc import ABC, abstractmethod
from os.path import join as path
from aiogram import F, Router
from aiogram.filters import or_f
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from Requests.get_date_site import ParsingDiary
from keyboards import categories_button, principles_community, get_page


category_participant = Router()


class PrinciplesCommunity(ABC):
    @abstractmethod
    async def __call__(self):
        pass

class StepsAN(PrinciplesCommunity):
    async def __call__(self) -> Tuple[str, int]:
        return path('TextFiles', 'twelve_steps_an.txt'), 620
    

class TraditionAN(PrinciplesCommunity):
    async def __call__(self) -> Tuple[str, int]:
        return path('TextFiles', 'twelve_tradition_an.txt'), 996


class MinistriesAn(PrinciplesCommunity):
    async def __call__(self) -> Tuple[str, int]:
        return path('TextFiles', 'twelve_ministries_an.txt'), 925


@category_participant.callback_query(F.data == 'get_dilay_planner')
async def delay_planner(call: CallbackQuery):
    dairy = ParsingDiary('https://na-russia.org/')
    await call.message.answer(text=dairy.visual_diary())


@category_participant.callback_query(F.data == 'categories_in_participant')
async def post_categories_participant(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open(path('TextFiles', 'what_is_an.txt'), 'r').read()))


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
    principles = {
        'steps_an': StepsAN(), 
        'tradition_an': TraditionAN(), 
        'service_concepts': MinistriesAn()
        }
    
    text, limit = await principles[call.data[:-1]]()

    await call.message.edit_caption(
            caption = {
                '1': open(text, 'r').read()[:limit], 
                '2': open(text, 'r').read()[limit:]
                }[call.data[-1]],
            reply_markup = get_page(call.data[:-1])
            )
    
   




