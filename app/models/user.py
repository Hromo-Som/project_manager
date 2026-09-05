from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

if TYPE_CHECKING:
    from . import Task, Project, Profile, ProjectMembership


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    tasks: Mapped[list[Task]] = relationship(back_populates='assignee')
    projects: Mapped[list[Project]] = relationship(
        back_populates='owner',
        cascade='all, delete-orphan',
        passive_deletes=True
    )
    profile: Mapped[Profile | None] = relationship(back_populates='user')
    project_memberships: Mapped[list[ProjectMembership]] = relationship(
        back_populates='user'
    )

    def __repr__(self) -> str:
        return (
            'Пользователь:\n'
            f'name = {self.name}\n'
            f'email = {self.email}\n'
            f'is_active = {self.is_active}'
        )
