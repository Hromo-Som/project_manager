from sqlalchemy import and_, not_, or_, select, delete

from .database import SessionFactory
from .models import Task, User


def main():
    # with SessionFactory.begin() as session:
    #     users = [
    #         User(
    #             name="Анна",
    #             email="anna@company.com",
    #             is_active=True
    #         ),
    #         User(
    #             name="Мария",
    #             email="maria@example.com",
    #             is_active=True
    #         ),
    #         User(
    #             name="Павел",
    #             email="pavel@company.com",
    #             is_active=False
    #         ),
    #         User(
    #             name="Елена",
    #             email="elena@example.org",
    #             is_active=True
    #         ),
    #         User(
    #             name="Андрей",
    #             email="andrey@example.com",
    #             is_active=False
    #         ),
    #         User(
    #             name="АНТОН",
    #             email="anton@company.com",
    #             is_active=False
    #         )
    #     ]

    #     tasks = [
    #         Task(
    #             title="Изучить SQL",
    #             description="Основы WHERE",
    #             is_completed=False,
    #             priority=5
    #         ),
    #         Task(
    #             title="Написать документацию",
    #             description=None,
    #             is_completed=False,
    #             priority=3
    #         ),
    #         Task(
    #             title="Исправить баг",
    #             description="Ошибка авторизации",
    #             is_completed=True,
    #             priority=4
    #         ),
    #         Task(
    #             title="Проверить отчёт",
    #             description=None,
    #             is_completed=True,
    #             priority=2
    #         ),
    #         Task(
    #             title="SQL практика",
    #             description="Фильтры и условия",
    #             is_completed=False,
    #             priority=4
    #         ),
    #         Task(
    #             title="Уборка",
    #             description="Низкий приоритет",
    #             is_completed=False,
    #             priority=1
    #         ),
    #         Task(
    #             title="Готовность 50%",
    #             description="Проверка символа процента",
    #             is_completed=False,
    #             priority=2
    #         ),
    #         Task(
    #             title="Готовность 500",
    #             description="Контрольное название",
    #             is_completed=False,
    #             priority=2
    #         )
    #     ]

    #     session.add_all(users)
    #     session.add_all(tasks)

    # with SessionFactory() as session:
    #     uc_tasks = session.scalars(
    #         select(Task.title)
    #         .where(
    #             Task.is_completed.is_(False),
    #             Task.priority >= 4
    #         )
    #     ).all()
    #     mid_priority_tasks = session.scalars(
    #         select(Task.title)
    #         .where(
    #             and_(
    #                 Task.priority <= 4,
    #                 Task.priority >= 2
    #             )
    #         )
    #     ).all()
    #     uncompleted_tasks = session.scalars(
    #         select(Task.title)
    #         .where(
    #             and_(
    #                 Task.is_completed.is_(False),
    #                 Task.priority >= 4
    #             )
    #         )
    #     ).all()
    #     print(uc_tasks)
    #     print("-----------------")
    #     print(mid_priority_tasks)
    #     print("-----------------")
    #     print(uncompleted_tasks)

    # with SessionFactory() as session:
    #     anna_or_mary = session.scalars(
    #         select(User.name)
    #         .where(
    #             or_(
    #                 User.name == "Анна",
    #                 User.name == "Мария"
    #             )
    #         )
    #     ).all()
    #     tasks = session.scalars(
    #         select(Task.title)
    #         .where(
    #             or_(
    #                 and_(
    #                     Task.is_completed.is_(False),
    #                     Task.priority >= 4
    #                 ),
    #                 Task.title == "Исправить баг"
    #             )
    #         )
    #     ).all()
    #     not_anna_or_mary = session.scalars(
    #         select(User.name)
    #         .where(
    #             not_(
    #                 or_(
    #                     User.name == "Анна",
    #                     User.name == "Мария"
    #                 )
    #             )
    #         )
    #     ).all()

    #     print(anna_or_mary)
    #     print("-----------------")
    #     print(tasks)
    #     print("-----------------")
    #     print(not_anna_or_mary)

    # with SessionFactory() as session:
    #     like = session.scalars(
    #         select(User.name)
    #         .where(
    #             User.name.like("%ия")
    #         )
    #     ).all()
    #     ilike = session.scalars(
    #         select(User.name)
    #         .where(
    #             User.name.ilike("ан%")
    #         )
    #     ).all()
    #     contains_email = session.scalars(
    #         select(User.name)
    #         .where(
    #             User.email.contains("@company.com")
    #         )
    #     ).all()
    #     contains_task = session.scalars(
    #         select(Task.title)
    #         .where(
    #             Task.title.contains("50%", autoescape=True)
    #         )
    #     ).all()

    #     print(like)
    #     print("-----------------")
    #     print(ilike)
    #     print("-----------------")
    #     print(contains_email)
    #     print("-----------------")
    #     print(contains_task)

    # with SessionFactory() as session:
    #     t_without_desc = session.scalars(
    #         select(Task.title)
    #         .where(
    #             Task.description.is_(None)
    #         )
    #     ).all()
    #     t_uncompleted = session.scalars(
    #         select(Task.title)
    #         .where(
    #             Task.is_completed.is_(False),
    #             Task.description.is_not(None)
    #         )
    #     ).all()
    #     u_inactive = session.scalars(
    #         select(User.name)
    #         .where(
    #             User.is_active.is_(False)
    #         )
    #     ).all()

    #     print(t_without_desc)
    #     print("-----------------")
    #     print(t_uncompleted)
    #     print("-----------------")
    #     print(u_inactive)

    # with SessionFactory() as session:
    #     t_priority = session.scalars(
    #         select(Task.title)
    #         .where(
    #             Task.priority.in_([1, 5])
    #         )
    #     ).all()
    #     u_active = session.scalars(
    #         select(User.name)
    #         .where(
    #             User.is_active.is_(True),
    #             User.name.in_(["Анна", "Елена", "Павел"])
    #         )
    #     ).all()
    #     t_not_priority = session.scalars(
    #         select(Task.title)
    #         .where(
    #             Task.priority.not_in([1, 2])
    #         )
    #     ).all()
    #     u_empty_ids = session.scalars(
    #         select(User.name)
    #         .where(
    #             User.id.in_([])
    #         )
    #     ).all()

    #     print(t_priority)
    #     print("-----------------")
    #     print(u_active)
    #     print("-----------------")
    #     print(t_not_priority)
    #     print("-----------------")
    #     print(u_empty_ids)

    with SessionFactory.begin() as session:
        # session.execute(delete(Task))
        # session.execute(delete(User).where(User.id >= 5))


if __name__ == "__main__":
    main()
