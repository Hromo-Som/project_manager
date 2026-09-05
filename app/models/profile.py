from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

if TYPE_CHECKING:
    from . import User


class Profile(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    timezone: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default='UTC'
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False,
        unique=True
    )
    user: Mapped[User] = relationship(back_populates='profile')
