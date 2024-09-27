from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def categories_button():
    inline_keyboard_list = [
        [InlineKeyboardButton(text='Новичку', callback_data='get_beginner')],
        [InlineKeyboardButton(text='Участнику', callback_data='get_participant')],
        [InlineKeyboardButton(text='АН в обществе', callback_data='get_an_in_society')],
        [InlineKeyboardButton(text='Обратная связь', callback_data='feed_back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def beginner_category():
    inline_keyboard_list = [
        [InlineKeyboardButton(text='О сообществе «Анонимные Наркоманы»', callback_data='get_about_an')],
        [InlineKeyboardButton(text='Что происходит на собраниях АН', callback_data='get_what_happens_an')],
        [InlineKeyboardButton(text='Вопросы и ответы', callback_data='get_questions_answers')],
        [InlineKeyboardButton(text='Собрания сегодня', web_app=WebAppInfo(url='https://na-msk.ru/schedule-new/'))],
        [InlineKeyboardButton(text='Информация для родственников', web_app=WebAppInfo(url='https://na-msk.ru/info-adults/'))],
        [InlineKeyboardButton(text='<<Назад', callback_data='categories_in_beginner')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def participant_category():
    inline_keyboard_list = [
        [InlineKeyboardButton(text='Собрания сегодня', web_app=WebAppInfo(url='https://na-msk.ru/schedule-member/'))],
        [InlineKeyboardButton(text='Ежедневник', callback_data='get_dilay_planner')],
        [InlineKeyboardButton(text='Принципы сообщества', callback_data='get_community_principles')],
        [InlineKeyboardButton(text='<<Назад', callback_data='categories_in_participant')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def society_category():
    inline_keyboard_list = [
        [InlineKeyboardButton(text='О сообществе «Анонимные Наркоманы»', callback_data='get_about_an')],
        [InlineKeyboardButton(text='Открытые собрания', web_app=WebAppInfo(url='https://na-msk.ru/schedule-pro/'))],
        [InlineKeyboardButton(text='<<Назад', callback_data='categories_in_society')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def beck_feed_back():
    button_feed_back = [
        [InlineKeyboardButton(text='<<Назад', callback_data="back_category")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=button_feed_back)
