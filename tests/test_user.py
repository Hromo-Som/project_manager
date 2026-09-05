import pytest

from sqlalchemy import func, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models import User


def test_create_user(
        db_session: Session
) -> None:
    user = User(
        name='Анна',
        email='test_anna@example.com',
        is_active=True,
    )

    db_session.add(user)
    db_session.flush()

    assert user.id is not None
    assert user.name == 'Анна'

    loaded_user = db_session.get(
        User,
        user.id
    )

    assert loaded_user is user


def test_database_is_empty(
    db_session: Session,
) -> None:
    count = db_session.scalar(
        select(func.count(User.id))
    )

    assert count == 0


def test_duplicate_email(
    db_session: Session
) -> None:

    first_user = User(
        name="Анна",
        email="duplicate@example.com",
        is_active=True,
    )

    db_session.add(first_user)
    db_session.flush()

    second_user = User(
        name="Другая Анна",
        email="duplicate@example.com",
        is_active=True,
    )

    db_session.add(second_user)

    with pytest.raises(IntegrityError):
        db_session.flush()

    db_session.rollback()
