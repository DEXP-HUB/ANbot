from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def categories_button() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [InlineKeyboardButton(text='Новичку', callback_data='get_beginner')],
        [InlineKeyboardButton(text='Участнику', callback_data='get_participant')],
        [InlineKeyboardButton(text='АН в обществе', callback_data='get_an_in_society')],
        [InlineKeyboardButton(text='Обратная связь', callback_data='feed_back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def beginner_category() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [InlineKeyboardButton(text='О сообществе «Анонимные Наркоманы»', callback_data='get_about_an')],
        [InlineKeyboardButton(text='Что происходит на собраниях АН', callback_data='what_happens_an_page1')],
        [InlineKeyboardButton(text='Вопросы и ответы', callback_data='get_questions_answers')],
        [InlineKeyboardButton(text='Собрания сегодня', web_app=WebAppInfo(url='https://na-msk.ru/schedule-new/'))],
        [InlineKeyboardButton(text='Информация для родственников', web_app=WebAppInfo(url='https://na-msk.ru/info-adults/'))],
        [InlineKeyboardButton(text='<<Назад', callback_data='categories_in_beginner')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def participant_category() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [InlineKeyboardButton(text='Собрания сегодня', web_app=WebAppInfo(url='https://na-msk.ru/schedule-member/'))],
        [InlineKeyboardButton(text='Ежедневник', callback_data='get_dilay_planner')],
        [InlineKeyboardButton(text='Принципы сообщества', callback_data='get_community_principles')],
        [InlineKeyboardButton(text='<<Назад', callback_data='categories_in_participant')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def society_category() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [InlineKeyboardButton(text='О сообществе «Анонимные Наркоманы»', callback_data='get_about_an_in_society')],
        [InlineKeyboardButton(text='Открытые собрания', web_app=WebAppInfo(url='https://na-msk.ru/schedule-pro/'))],
        [InlineKeyboardButton(text='<<Назад', callback_data='categories_in_society')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def beck_feed_back() -> InlineKeyboardMarkup:
    button_feed_back = [
        [InlineKeyboardButton(text='<<Назад', callback_data='back_category')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=button_feed_back)


def about_an_buttons() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [InlineKeyboardButton(text='Сообщество', callback_data='community_an'), 
         InlineKeyboardButton(text='Цель', callback_data='target_an')],
        [InlineKeyboardButton(text='Участие', callback_data='participation_an'), 
         InlineKeyboardButton(text='Собрания', callback_data='meetings_an')],
        [InlineKeyboardButton(text='Программа', callback_data='program_an'), 
         InlineKeyboardButton(text='Религия', callback_data='religion_an')],
        [InlineKeyboardButton(text='<<Назад', callback_data='back_about_an')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def about_an_sc_buttons() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [InlineKeyboardButton(text='Сообщество', callback_data='community_an_sc'), 
         InlineKeyboardButton(text='Цель', callback_data='target_an_sc')],
        [InlineKeyboardButton(text='Участие', callback_data='participation_an_sc'), 
         InlineKeyboardButton(text='Собрания', callback_data='meetings_an_sc')],
        [InlineKeyboardButton(text='Программа', callback_data='program_an_sc'), 
         InlineKeyboardButton(text='Религия', callback_data='religion_an_sc')],
        [InlineKeyboardButton(text='<<Назад', callback_data='back_about_an_sc')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def questions_answers_button() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [InlineKeyboardButton(text='Как работает программа?', callback_data='job_program'), 
         InlineKeyboardButton(text='Точно бесплатно?', callback_data='program_free')],
        [InlineKeyboardButton(text='Почему собрания в храмах и наркодиспансерах?', callback_data='meetings')],
        [InlineKeyboardButton(text='Можете меня проводить, я боюсь потеряться?', callback_data='help_go')],
        [InlineKeyboardButton(text='<<Назад', callback_data='get_beginner')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)


def what_happens_buttons() -> InlineKeyboardMarkup:
    inline_keyboard_list = [
        [InlineKeyboardButton(text='<<', callback_data='what_happens_an_page1'), 
         InlineKeyboardButton(text='>>', callback_data='what_happens_an_page2')],
        [InlineKeyboardButton(text='<<Назад', callback_data='get_beginner')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard_list)