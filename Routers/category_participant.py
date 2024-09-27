from aiogram import F, Router
from aiogram.types import CallbackQuery
from Requests.get_date_site import ParsingDiary
from TextFiles.read_files import *


category_participant = Router()


@category_participant.callback_query(F.data == 'get_dilay_planner')
async def delay_planner(call: CallbackQuery):
    dairy = ParsingDiary('https://na-russia.org/')
    await call.message.answer(text=dairy.visual_diary())


@category_participant.callback_query(F.data == 'get_community_principles')
async def community_principles(call: CallbackQuery):
    (await call.message.answer(text=read_twelve_steps_an()),
     await call.message.answer(text=read_twelve_tradition_an()),
     await call.message.answer(text=read_twelve_ministries_an()))



