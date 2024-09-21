from aiogram.fsm.state import State, StatesGroup


class FeedBack(StatesGroup):
    name = State()
    description = State()
