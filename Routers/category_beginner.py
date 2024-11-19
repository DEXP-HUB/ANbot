from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from keyboards import categories_button, about_an_buttons


category_beginner = Router()


@category_beginner.callback_query(F.data == 'get_about_an')
async def about_an(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=about_an_buttons())


@category_beginner.callback_query(F.data == 'community_an')
async def community_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=about_an_buttons(),
        caption='Мы — выздоравливающие зависимые, которые регулярно собираются для того, чтобы помогать друг другу'
          'оставаться чистыми. Международное сообщество «Анонимные Наркоманы» существует с 1953 года, первая группа'
          ' в России провела собрание в 1990 году. Сегодня в 144 странах мира проводится 70000 собраний АН '
          ' еженедельно. В 280 городах России проводится больше 3000 собраний еженедельно. В Москве'
          ' и Московской области более 260 групп АН проводит более 900 собраний еженедельно (данные 2023 года).'
    )


@category_beginner.callback_query(F.data == 'target_an')
async def target_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=about_an_buttons(),
        caption='У каждой группы сообщества «Анонимные Наркоманы» есть лишь одна главная цель — предоставить'
          ' информацию о возможности выздоровления тем, кто еще употребляет наркотики и страдает от зависимости.' 
          ' Вот уже 60 лет основная идея АН остается неизменной — любой, совершенно любой зависимый может прекратить' 
          ' употреблять наркотики, потерять желание употреблять и найти новый путь в жизни.'
    )


@category_beginner.callback_query(F.data == 'participation_an')
async def participation_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=about_an_buttons(),
        caption='Единственным условием для членства в Анонимных Наркоманах является желание прекратить употребление.' 
          ' Мы не входим в состав других организаций, не платим ни вступительных, ни членских взносов, не подписываем'
          ' гарантий и никому не даем никаких обещаний. Мы не связаны ни с одной политической, религиозной или'
          ' правоохранительной организацией, никто и никогда не осуществляет за нами надзор.'
          ' Участие в сообществе АН бесплатно!'
          ' Каждый из нас уже заплатил за право выздоравливать своей собственной болью.'
    )


@category_beginner.callback_query(F.data == 'meetings_an')
async def meetings_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=about_an_buttons(),
        caption='Присоединиться к нам может каждый, независимо от возраста, национальности, сексуальной ориентации,'
          ' убеждений, религии или отсутствия таковой. Собрания АН приветствуют любого зависимого, для которого' 
          ' наркотики стали серьезной проблемой. Неважно, откуда мы пришли, какое получили воспитание, и чем мы' 
          ' занимаемся - двери АН открыты для нас.'
    )


@category_beginner.callback_query(F.data == 'program_an')
async def program_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=about_an_buttons(),
        caption='Помощь одного зависимого другому обладает ни с чем не сравнимой терапевтической ценностью.'
          ' Мы — непрофессиональное сообщество и используем все, что помогает выздоравливать другим зависимым,' 
          ' которые с помощью Анонимных Наркоманов научились жить без наркотиков. Наше выздоровление стало возможным' 
          ' благодаря принципам, известным как Двенадцать Шагов Анонимных Наркоманов.'
    )


@category_beginner.callback_query(F.data == 'program_an')
async def program_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=about_an_buttons(),
        caption='Помощь одного зависимого другому обладает ни с чем не сравнимой терапевтической ценностью.'
          ' Мы — непрофессиональное сообщество и используем все, что помогает выздоравливать другим зависимым,' 
          ' которые с помощью Анонимных Наркоманов научились жить без наркотиков. Наше выздоровление стало возможным' 
          ' благодаря принципам, известным как Двенадцать Шагов Анонимных Наркоманов.'
    )


@category_beginner.callback_query(F.data == 'religion_an')
async def religion_an(call: CallbackQuery):
    await call.message.edit_caption(
        reply_markup=about_an_buttons(),
        caption='Анонимные Наркоманы — это духовная, но не религиозная программа.'
          ' Право на Бога в своем собственном понимании является общим для всех, в нем не кроется никаких хитростей.' 
          ' Это означает, что в сообщество АН приходят зависимые, имеющие самые различные вероисповедания и'
          ' представляющие широкий круг конфессий, а также атеисты и агностики.'
    )


@category_beginner.callback_query(F.data == 'get_what_happens_an')
async def what_happens_an(call: CallbackQuery):
    await call.message.answer(text=open('TextFiles/what_happens_an.txt', 'r').read())


@category_beginner.callback_query(F.data == 'get_questions_answers')
async def questions_answers(call: CallbackQuery):
    await call.message.answer(text=open('TextFiles/questions_answers.txt', 'r').read())


@category_beginner.callback_query(F.data == 'categories_in_beginner')
async def post_categories_beginner(call: CallbackQuery):
    await call.message.edit_media(reply_markup=categories_button(), media=InputMediaPhoto(
        type='photo', media=FSInputFile(path='Photo/banner-2.jpg', filename='banner-2.jpg'),
        caption=open('TextFiles/what_is_an.txt', 'r').read()))

