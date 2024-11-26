from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine


engine = create_engine("sqlite:///DataBase/feed_back.db")


class Base(DeclarativeBase):
    pass


class UserFeedBack(Base):
    __tablename__ = "feed_back"

    id: Mapped[Optional[int]] = mapped_column(primary_key=True)
    first_name: Mapped[Optional[str]]
    last_name: Mapped[Optional[str]]
    url_name: Mapped[Optional[str]]
    message_text: Mapped[Optional[str]]
    

    def __repr__(self) -> str:
        return (f"FeedBack(id={self.id}, first_name={self.first_name}, last_name={self.last_name},"
                f"url_name={self.url_name}, message_text{self.message_text}")
