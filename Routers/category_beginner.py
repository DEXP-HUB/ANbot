from aiogram import Router, F
from aiogram.filters import or_f
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from keyboards import categories_button, about_an_buttons, questions_answers_button, society_category, beginner_category


category_beginner = Router()


async def beginner_or_society(call: CallbackQuery) -> tuple:
    caption = ('У каждой группы сообщества «Анонимные Наркоманы» есть лишь одна главная цель — предоставить'
               ' информацию o возможности выздоровления тем, кто еще употребляет наркотики и страдает от зависимости.',
               'Наша политика в связях с общественностью строится не на рекламе, а на привлекательности; нам нужно'
               ' всегда сохранять личную анонимность на уровне средств массовой информации.')
    return {'back_about_an': (beginner_category(), caption[0]), 
            'back_about_an_society': (society_category(), caption[1])}[call.data]



@category_beginner.callback_query(F.data == 'get_about_an')
async def about_an(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=about_an_buttons())


@category_beginner.callback_query(or_f(F.data == 'community_an', F.data == 'target_an', F.data == 'participation_an',
                                       F.data == 'meetings_an', F.data == 'program_an', F.data == 'religion_an'))
async def category_about_an(call: CallbackQuery):
    text = open(file='TextFiles/about_an.txt', mode='r').read().split('\n')
    category = {'community_an': text[2], 'target_an': text[6], 'participation_an': text[10],
                'meetings_an': text[14], 'program_an': text[18], 'religion_an': text[22]}
    await call.message.edit_caption(reply_markup=about_an_buttons(), caption=category[call.data])


@category_beginner.callback_query(or_f(F.data == 'back_about_an', F.data == 'back_about_an_society'))
async def back_about_an(call: CallbackQuery):
    data = await beginner_or_society(call)
    await call.message.edit_caption(reply_markup=data[0], caption=data[1])


@category_beginner.callback_query(F.data == 'get_questions_answers')
async def questions_answers(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=questions_answers_button())


@category_beginner.callback_query(or_f(F.data == 'job_program', F.data == 'program_free',
                                       F.data == 'meetings', F.data == 'help_go'))
async def category_questions_answers(call: CallbackQuery):
    text = open(file='TextFiles/questions_answers.txt', mode='r').read().split('\n')
    category = {'job_program': text[2], 'program_free': text[6], 'meetings': text[10], 'help_go': text[14]}
    await call.message.edit_caption(reply_markup=questions_answers_button(), caption=category[call.data])


@category_beginner.callback_query(F.data == 'get_what_happens_an')
async def what_happens_an(call: CallbackQuery):
    await call.message.edit_caption(caption=open('TextFiles/what_happens_an.txt', 'r').read())
    # await call.message.answer(text=open('TextFiles/what_happens_an.txt', 'r').read())


@category_beginner.callback_query(F.data == 'categories_in_beginner')
async def post_categories_beginner(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open('TextFiles/what_is_an.txt', 'r').read()))

