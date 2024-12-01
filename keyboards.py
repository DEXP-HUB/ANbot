from aiogram.types import InlineKeyboardButton as Button
from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.exceptions import TelegramBadRequest





def categories_button() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [Button(text='Новичку', callback_data='get_beginner')],
        [Button(text='Участнику', callback_data='get_participant')],
        [Button(text='АН в обществе', callback_data='get_an_in_society')],
        [Button(text='Обратная связь', callback_data='feed_back')]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def beginner_category() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [Button(text='О сообществе «Анонимные Наркоманы»', callback_data='get_about_an')],
        [Button(text='Что происходит на собраниях АН', callback_data='what_happens_an_page1')],
        [Button(text='Вопросы и ответы', callback_data='get_questions_answers')],
        [Button(text='Собрания сегодня', web_app=WebAppInfo(url='https://na-msk.ru/schedule-new/'))],
        [Button(text='Информация для родственников', web_app=WebAppInfo(url='https://na-msk.ru/info-adults/'))],
        [Button(text='<<Назад', callback_data='categories_in_beginner')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def participant_category() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [Button(text='Собрания сегодня', web_app=WebAppInfo(url='https://na-msk.ru/schedule-member/'))],
        [Button(text='Ежедневник', callback_data='get_dilay_planner')],
        [Button(text='Принципы сообщества', callback_data='get_community_principles')],
        [Button(text='<<Назад', callback_data='categories_in_participant')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def society_category() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [Button(text='О сообществе «Анонимные Наркоманы»', callback_data='get_about_an_in_society')],
        [Button(text='Открытые собрания', web_app=WebAppInfo(url='https://na-msk.ru/schedule-pro/'))],
        [Button(text='<<Назад', callback_data='categories_in_society')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def beck_feed_back() -> InlineKeyboardMarkup:
    button_feed_back = [
        [Button(text='<<Назад', callback_data='back_category')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=button_feed_back)


def about_an_buttons(back_button: str) -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [Button(text='Сообщество', callback_data='community_an'), 
         Button(text='Цель', callback_data='target_an')],
        [Button(text='Участие', callback_data='participation_an'), 
         Button(text='Собрания', callback_data='meetings_an')],
        [Button(text='Программа', callback_data='program_an'), 
         Button(text='Религия', callback_data='religion_an')],
        [Button(text='<<Назад', callback_data=back_button)]
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def questions_answers_button() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [Button(text='Как работает программа?', callback_data='job_program'), 
         Button(text='Точно бесплатно?', callback_data='program_free')],
        [Button(text='Почему собрания в храмах и наркодиспансерах?', callback_data='meetings')],
        [Button(text='Можете меня проводить, я боюсь потеряться?', callback_data='help_go')],
        [Button(text='<<Назад', callback_data='get_beginner')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def what_happens_buttons() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [Button(text='<<', callback_data='what_happens_an_page1'), 
         Button(text='>>', callback_data='what_happens_an_page2')],
        [Button(text='<<Назад', callback_data='get_beginner')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)