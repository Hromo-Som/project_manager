from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from . import Base
from .task_tag import task_tags

if TYPE_CHECKING:
    from . import Task


class Tag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    category: Mapped[str] = mapped_column(String(50))
    tasks: Mapped[list[Task]] = relationship(
        secondary=task_tags,
        back_populates='tags'
    )

    __table_args__ = (
        UniqueConstraint('name', 'category', name='uq_tags_name_category'),
    )
