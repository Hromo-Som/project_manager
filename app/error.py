from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from .database import SessionFactory
from .models import User, Project


def create_user_request(
    name: str,
    email: str,
) -> dict:
    user = User(
        name=name,
        email=email,
    )
    with SessionFactory() as session:
        print(id(session))
        session.add(user)
        try:
            session.flush()
            session.commit()
            return {
                'status': 201,
                'email': user.email,
            }
        except IntegrityError:
            session.rollback()
            return {
                'status': 409,
                'error': 'Пользователь с таким email уже существует',
            }


def main():

    # with SessionFactory.begin() as session:
    #     anna = User(
    #         name='Анна',
    #         email='errors_anna@example.com',
    #         is_active=True
    #     )

    #     project = Project(
    #         name='Task Manager',
    #         owner=anna
    #     )

    #     session.add(anna)

    # with SessionFactory() as session:
    #     another_anna = User(
    #         name='Другая Анна',
    #         email='errors_anna@example.com',
    #         is_active=True
    #     )

    #     try:
    #         session.add(another_anna)
    #         session.flush()
    #     except IntegrityError:
    #         session.rollback()

    #     users = session.scalars(
    #         select(User)
    #         .order_by(User.id)
    #     ).all()

    #     for user in users:
    #         print(f'{user.name} | {user.email}')

    # with SessionFactory() as session:
    #     project = Project(
    #         name='Несуществующий проект',
    #         owner_id=99999
    #     )

    #     try:
    #         session.add(project)
    #         session.flush()
    #     except IntegrityError:
    #         session.rollback()

    #     f_project = session.get(Project, 1)
    #     if f_project:
    #         print(f_project.name)

    # session = SessionFactory()
    # user = User(
    #     name='Другая Анна',
    #     email='errors_anna@example.com',
    #     is_active=True
    # )
    # try:
    #     session.add(user)
    #     session.flush()
    # except IntegrityError:
    #     print(session.is_active)
    #     session.rollback()
    #     print(session.is_active)
    # session.close()

    # session = SessionFactory()
    # mary = User(
    #     name='Мария',
    #     email='errors_maria@example.com',
    #     is_active=True
    # )
    # anna_copy = User(
    #     name='Копия Анны',
    #     email='errors_anna@example.com',
    #     is_active=True
    # )
    # try:
    #     session.add(mary)
    #     session.flush()
    #     mary_id = mary.id
    #     print(mary_id is not None)
    #     session.add(anna_copy)
    #     session.flush()
    # except IntegrityError:
    #     session.rollback()
    # session.close()
    # mary = session.get(User, mary_id)
    # anna = session.get(User, 1)
    # print(mary)
    # print(anna)
    # session.close()

    print(
        create_user_request(
            name='Павел',
            email='errors_pavel@example.com'
        )
    )

    print(
        create_user_request(
            name='Копия Павла',
            email='errors_pavel@example.com'
        )
    )


if __name__ == '__main__':
    main()
