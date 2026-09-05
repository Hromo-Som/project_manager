from .database import SessionFactory, SessionNoExpire
from .models import Base, User, Task


def main():
    with SessionFactory.begin() as session:
        print(Base.metadata)
        print(Base.registry)
        print(len(Base.metadata.tables))
        print(len(list(Base.registry.mappers)))

        table_names = sorted(Base.metadata.tables.keys())
        model_names = sorted(
            mapper.class_.__name__ for mapper in Base.registry.mappers
        )

        print(table_names)
        print(model_names)
        print(User.__mapper__)
        print(Task.__mapper__)

        user = User(
            name="Алексей",
            email="alex@example.com",
            is_active=True
        )
        task = Task(
            title="Изучить ORM-модели",
            description=None,
            is_complited=False
        )

        print(user)
        print(task)
        print(User.__table__.c.id.primary_key)
        print(Task.__table__.c.id.primary_key)
        print(type(User.__table__.c.id.type).__name__)
        print(type(Task.__table__.c.id.type).__name__)

    with SessionFactory.begin() as session:
        user = User(
            name="Session User",
            email="session_user@example.com",
            is_active=True,
        )

        session.add(user)
        session.flush()

        user_id = user.id

    with SessionFactory.begin() as session:
        user1 = session.get(User, 1)
        user2 = session.get(User, 1)
        print(user1 is user2)
        print(session.identity_map.values())
        user1.name = 'New name'
        print(user2.name)
        session.rollback()

    with SessionFactory() as session:
        user1 = session.get(User, 1)
        print(session.identity_map.values())

    with SessionFactory() as session:
        user2 = session.get(User, 1)
        print(session.identity_map.values())

    print(user1.id, user2.id)
    print(user1 is user2)

    with SessionFactory() as session:
        user = User(
            name="Черновое имя",
            email="pending_user@example.com",
            is_active=True
        )
        print(user in session.new)

        session.add(user)
        print(user in session.new)

        user.name = 'new name'
        user.name = 'another new name'
        user.name = 'Итоговое имя'
        session.flush()

        user_id = user.id
        print(user in session.new)
        print(session.identity_map.values())

        session.rollback()

    with SessionFactory() as session:
        user = session.get(User, user_id)
        print(user)

    with SessionFactory.begin() as session:
        user1 = User(
            name="Первоначальное имя",
            email="uow_first@example.com",
            is_active=True
        )

        user2 = User(
            name="Пользователь для удаления",
            email="uow_second@example.com",
            is_active=True
        )

        session.add(user1)
        session.add(user2)
        print(user1 in session.new)
        print(user2 in session.new)
        session.flush()

        user1_id = user1.id
        user2_id = user2.id
        print(user1 in session.new)
        print(user2 in session.new)

        user1.name = "Итоговое имя"
        print(user1 in session.dirty)

        session.delete(user2)
        print(user2 in session.deleted)

    with SessionFactory() as session:
        user1 = session.get(User, user1_id)
        user2 = session.get(User, user2_id)

        print(user1)
        print(user2)

    session = SessionFactory()
    user = User(
        name="Flush User",
        email="flush_user@example.com",
        is_active=True
    )
    session.add(user)
    session.flush()
    print(user.id is not None)
    user_id = user.id
    session.rollback()
    session.close()
    with SessionFactory() as session:
        user = session.get(User, user_id)
        print(user)

    session = SessionFactory()
    user = User(
        name="Commit User",
        email="commit_user@example.com",
        is_active=True
    )
    session.add(user)
    session.flush()
    print(user.id is not None)
    user_id = user.id
    session.commit()
    session.close()
    with SessionFactory() as session:
        user = session.get(User, user_id)
        print(user)

    session = SessionFactory()
    print(session.in_transaction())
    user = User(
        name="Test",
        email="test@example.com",
        is_active=True
    )
    session.add(user)
    print(session.in_transaction())
    session.rollback()
    print(session.in_transaction())

    session = SessionFactory()
    user1 = session.get(User, 1)
    user1.name = "new_name"
    user2 = session.get(User, 2)
    session.rollback()

    session = SessionFactory()
    with session.no_autoflush:
        user1 = session.get(User, 1)
        user1.name = "new_name"
        user2 = session.get(User, 2)

    session.flush()
    session.rollback()

    session = SessionFactory()
    user = User(
        name="Close User",
        email="close_user@example.com",
        is_active=True
    )
    session.add(user)
    session.flush()
    user_id = user.id
    session.close()

    session = SessionFactory()
    user = session.get(User, user_id)
    print(user)

    session = SessionFactory()
    user = User(
        name="Close User",
        email="close_user@example.com",
        is_active=True
    )
    session.add(user)
    session.flush()
    user_id = user.id
    session.commit()
    session.close()

    session = SessionFactory()
    user = session.get(User, user_id)
    print(user)

    session1 = SessionNoExpire()
    user1 = session1.get(User, 5)
    session1.commit()

    session2 = SessionFactory()
    user2 = session2.get(User, 5)
    user2.name = "Имя из базы 1"
    session2.commit()

    print(user1.name)
    session1.refresh(user1)
    print(user1.name)

    session1 = SessionNoExpire()
    user1 = session1.get(User, 5)
    session1.commit()

    session2 = SessionFactory()
    user2 = session2.get(User, 5)
    user2.name = "Имя из базы 2"
    session2.commit()

    session1.expire(
        user1,
        ["name"],
    )
    print('-------------')
    print(user1.name)

    session = SessionFactory()
    user = session.get(User, 1)
    user_id = user.id
    session.commit()
    print(user.name)

    session = SessionNoExpire()
    user = session.get(User, 1)
    user_id = user.id
    session.commit()
    print(user.name)



if __name__ == '__main__':
    main()
