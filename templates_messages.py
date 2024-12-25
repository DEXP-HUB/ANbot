from abc import ABC
from os.path import join as path
from keyboards import categories_button


class MessageTemplate(ABC):
    pass


class Start(MessageTemplate):
    CAPTION: str = open(path('TextFiles', 'what_is_an.txt'), 'r').read()
    MARKUP = categories_button()
    PHOTO_NAME: str = 'banner-2.jpg'
    PHOTO_PATH = path('Photo', 'banner-2.jpg')
