from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    Text,
    Boolean,
    false,
    CheckConstraint,
    Index,
    ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base
from .task_tag import task_tags

if TYPE_CHECKING:
    from . import User, Tag


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    description: Mapped[str | None] = mapped_column(Text)
    is_completed: Mapped[bool] = mapped_column(Boolean, server_default=false())
    priority: Mapped[int] = mapped_column(nullable=False)
    assignee_id: Mapped[int | None] = mapped_column(
        ForeignKey('users.id'),
        nullable=True
    )
    assignee: Mapped[User | None] = relationship(back_populates='tasks')
    tags: Mapped[list[Tag]] = relationship(
        secondary=task_tags,
        back_populates='tasks'
    )

    __table_args__ = (
        CheckConstraint(
            'priority BETWEEN 1 AND 5',
            name='ck_tasks_priority_range'
        ),
        Index(
            'ix_tasks_completed_priority',
            'is_completed',
            'priority'
        )
    )

    def __repr__(self) -> str:
        return (
            'Задача:\n'
            f'title = {self.title}\n'
            f'description = {self.description}\n'
            f'is_completed = {self.is_completed}'
        )
