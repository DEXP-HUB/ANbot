from abc import ABC
from os.path import join as path
from keyboards import categories_button, beginner_category, participant_category, society_category


class CommandMessage(ABC):
    pass


class CallbackMessage(ABC):
    pass


class StartMessage(CommandMessage):
    CAPTION: str = open(path('TextFiles', 'what_is_an.txt'), 'r').read()
    MARKUP = categories_button()
    PHOTO_NAME: str = 'banner-2.jpg'
    PHOTO_PATH: str = path('Photo', 'banner-2.jpg')


class GetBeginner(CallbackMessage):
    CAPTION: str = ('У каждой группы сообщества «Анонимные Наркоманы» есть лишь одна главная цель — предоставить'    
              'информацию о возможности выздоровления тем, кто еще употребляет наркотики и страдает от зависимости.')
    MARKUP = beginner_category()
    PHOTO_NAME: str = 'beginner.jpg'
    PHOTO_PATH: str = path('Photo', 'beginner.jpg')
    MEDIA_TYPE: str = 'photo'


class GetParticipant(CallbackMessage):
    CAPTION: str = 'Наше общее благополучие важнее всего, от единства АН зависит личное выздоровление каждого.'
    MARKUP: str = participant_category()
    PHOTO_NAME: str = 'participant.jpg'
    PHOTO_PATH: str = path('Photo', 'participant.jpg')
    MEDIA_TYPE: str = 'photo'


class GetSociety(CallbackMessage):
    CAPTION: str = ('Наша политика в связях с общественностью строится не на рекламе, а на привлекательности; нам нужно'
                ' всегда сохранять личную анонимность на уровне средств массовой информации.')
    MARKUP = society_category()
    PHOTO_NAME: str = 'society.jpg'
    PHOTO_PATH: str = path('Photo', 'society.jpg')
    MEDIA_TYPE: str = 'photo'







    
    
