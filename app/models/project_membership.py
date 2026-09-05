from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

if TYPE_CHECKING:
    from . import User, Project


class ProjectMembership(Base):
    __tablename__ = 'project_memberships'

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        primary_key=True
    )
    project_id: Mapped[int] = mapped_column(
        ForeignKey('projects.id'),
        primary_key=True
    )
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    user: Mapped[User] = relationship(back_populates='project_memberships')
    project: Mapped[Project] = relationship(back_populates='memberships')
