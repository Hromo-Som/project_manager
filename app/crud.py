from sqlalchemy import select, delete

from .database import SessionFactory
from .models import User


def main():
    with SessionFactory.begin() as session:
        user1 = User(
            name="Алексей",
            email="crud_alex@example.com",
            is_active=True
        )

        user2 = User(
            name="Мария",
            email="crud_maria@example.com",
            is_active=True
        )

        user3 = User(
            name="Павел",
            email="crud_pavel@example.com",
            is_active=False
        )

        user4 = User(
            name="Елена",
            email="crud_elena@example.com",
            is_active=False
        )

        session.add(user1)
        session.add_all([user2, user3, user4])
        session.flush()
        alex_id = user1.id
        maria_id = user2.id
        pavel_id = user3.id
        elena_id = user4.id

    with SessionFactory.begin() as session:
        print(session.get(User, alex_id))
        print(session.get(User, maria_id))
        print(session.get(User, pavel_id))
        print(session.get(User, elena_id))

    with SessionFactory.begin() as session:
        res1 = session.scalars(select(User).order_by(User.id)).all()
        res2 = session.scalars(
            select(User)
            .where(User.is_active == True)  # noqa: E712
        ).all()
        res3 = session.scalars(select(User.email)).all()
        print(res1)
        print('---------------------')
        print(res2)
        print('---------------------')
        print(res3)

    with SessionFactory.begin() as session:
        session.execute(delete(User))


if __name__ == "__main__":
    main()
