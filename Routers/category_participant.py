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
    

class GetPages:
    @classmethod
    async def get_page1(cls, call_page):
        return await {
        'steps_page1': StepsAN(), 
        'tradition_page1': TraditionAN(), 
        'concepts_page1': MinistriesAn()
        }[call_page]()
    
    @classmethod
    async def get_page2(cls, call_page):
        return await {
        'steps_page2': StepsAN(), 
        'tradition_page2': TraditionAN(), 
        'concepts_page2': MinistriesAn()
        }[call_page]()
    


@category_participant.callback_query(F.data == 'get_dilay_planner')
async def delay_planner(call_page: CallbackQuery):
    dairy = ParsingDiary('https://na-russia.org/')
    await call_page.message.answer(text=dairy.visual_diary())


@category_participant.callback_query(F.data == 'categories_in_participant')
async def post_categories_participant(call_page: CallbackQuery):
    await call_page.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open(path('TextFiles', 'what_is_an.txt'), 'r').read()))


@category_participant.callback_query(F.data == 'get_community_principles')
async def community_principles(call_page: CallbackQuery):
    await call_page.message.edit_caption(
        reply_markup=principles_community(),
        caption='Наше общее благополучие важнее всего, от единства АН зависит личное выздоровление каждого.'
        )


@category_participant.callback_query(or_f(F.data == 'steps_page1', F.data == 'tradition_page1', 
                                          F.data == 'concepts_page1'))
async def principles_page1(call_page: CallbackQuery):
    text, limit = await GetPages().get_page1(call_page.data)

    await call_page.message.edit_caption(
            caption = open(text, 'r').read()[:limit],
            reply_markup = get_page(call_page.data[:-1])
            )


@category_participant.callback_query(or_f(F.data == 'steps_page2', F.data == 'tradition_page2', 
                                          F.data == 'concepts_page2'))
async def principles_page2(call_page: CallbackQuery):
    text, limit = await GetPages().get_page2(call_page.data)

    await call_page.message.edit_caption(
            caption = open(text, 'r').read()[limit:],
            reply_markup = get_page(call_page.data[:-1])
            )

