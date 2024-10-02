from sqlalchemy.orm import Mapped
from .. import Base


class Task(Base):
    __tablename__ = "tasks"

    author: Mapped[str]
    content: Mapped[str]