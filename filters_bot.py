from aiogram.filters import BaseFilter
from aiogram import types
from typing import List


class IsAdmin(BaseFilter):
    def __init__(self, user_id: int | List[int]) -> None:
        self.user_id = user_id

    async def __call__(self, message: types.Message) -> bool:
        if isinstance(self.user_id, int):
            return message.from_user.id == self.user_id
        return message.from_user.id in self.user_id