from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from FSM.fms_feed_back import FeedBack

feed_back_router = Router()


@feed_back_router.callback_query(F.data == 'feed_back')
async def start_fsm(call: CallbackQuery):
    await call.message.answer(text='Опишите ваше предложение по улучшению этого бота.')

