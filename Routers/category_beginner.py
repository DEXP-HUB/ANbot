from aiogram import Router, F
from aiogram.filters import or_f
from aiogram.filters.exception import ExceptionTypeFilter
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile, Message
from aiogram.types.error_event import ErrorEvent
from aiogram.exceptions import TelegramBadRequest
from keyboards import (categories_button, about_an_buttons, questions_answers_button,
                       beginner_category, what_happens_buttons)


category_beginner = Router()


# @category_beginner.error(ExceptionTypeFilter(TelegramBadRequest))
# async def request_error(event: ErrorEvent):
#     pass


@category_beginner.callback_query(F.data == 'get_about_an')
async def about_an(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=about_an_buttons(back_button='back_about_an'))


@category_beginner.callback_query(or_f(F.data == 'community_an', F.data == 'target_an', F.data == 'participation_an',
                                       F.data == 'meetings_an', F.data == 'program_an', F.data == 'religion_an'))
async def category_about_an(call: CallbackQuery):
    text = open(file='TextFiles/about_an.txt', mode='r').read().split('\n')
    category = {'community_an': text[2], 'target_an': text[6], 'participation_an': text[10],
                'meetings_an': text[14], 'program_an': text[18], 'religion_an': text[22]}
    
    await call.message.edit_caption(reply_markup=call.message.reply_markup, caption=category[call.data])


@category_beginner.callback_query(F.data == 'back_about_an')
async def back_about_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=beginner_category(),
        caption='У каждой группы сообщества «Анонимные Наркоманы» есть лишь одна главная цель — предоставить'
               ' информацию o возможности выздоровления тем, кто еще употребляет наркотики и страдает от зависимости.'
        )


@category_beginner.callback_query(F.data == 'get_questions_answers')
async def questions_answers(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=questions_answers_button())


@category_beginner.callback_query(or_f(F.data == 'job_program', F.data == 'program_free',
                                       F.data == 'meetings', F.data == 'help_go'))
async def category_questions_answers(call: CallbackQuery):
    text = open(file='TextFiles/questions_answers.txt', mode='r').read().split('\n')
    category = {'job_program': text[2], 'program_free': text[6], 'meetings': text[10], 'help_go': text[14]}

    await call.message.edit_caption(reply_markup=questions_answers_button(), caption=category[call.data])


@category_beginner.callback_query(or_f(F.data == 'what_happens_an_page1', F.data == 'what_happens_an_page2'))
async def what_happens_an(call: CallbackQuery):
    caption = open(file='TextFiles/what_happens_an.txt', mode='r').read()
    page = {'what_happens_an_page1': caption[0:995], 'what_happens_an_page2': caption[995:]}

    await call.message.edit_caption(reply_markup=what_happens_buttons(), caption=page[call.data])
        

@category_beginner.callback_query(F.data == 'categories_in_beginner')
async def post_categories_beginner(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open('TextFiles/what_is_an.txt', 'r').read()))

