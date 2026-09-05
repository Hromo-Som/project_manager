from sqlalchemy import and_, not_, or_, select, delete, func

from .database import SessionFactory
from .models import Task, User


def main():
    # with SessionFactory() as session:
    #     tasks = [
    #         Task(
    #             title="Изучить JOIN",
    #             is_completed=False,
    #             priority=5,
    #             assignee_id=1
    #         ),
    #         Task(
    #             title="Написать отчёт",
    #             is_completed=True,
    #             priority=3,
    #             assignee_id=1
    #         ),
    #         Task(
    #             title="Исправить баг",
    #             is_completed=False,
    #             priority=4,
    #             assignee_id=3
    #         ),
    #         Task(
    #             title="Рефакторинг",
    #             is_completed=False,
    #             priority=2,
    #             assignee_id=2
    #         ),
    #         Task(
    #             title="Общая задача",
    #             is_completed=False,
    #             priority=1,
    #             assignee_id=4
    #         )
    #     ]

    #     session.add_all(tasks)
    #     session.commit()

    # with SessionFactory() as session:
    #     tasks_with_assignee = session.scalars(
    #         select(Task.title)
    #         .join(User)
    #         .order_by(Task.id)
    #     ).all()
    #     users_outerjoin = session.scalars(
    #         select(User.name)
    #         .outerjoin(Task)
    #         .order_by(User.id, Task.id)
    #     ).all()

    #     print(tasks_with_assignee)
    #     print(users_outerjoin)

    # with SessionFactory() as session:
    #     tasks_with_assignee = session.scalars(
    #         select(Task.title)
    #         .join(Task.assignee)
    #         .order_by(Task.id)
    #     ).all()
    #     users_outerjoin = session.scalars(
    #         select(User.name)
    #         .outerjoin(User.tasks)
    #         .order_by(User.id, Task.id)
    #     ).all()

    #     print(tasks_with_assignee)
    #     print(users_outerjoin)

    # with SessionFactory() as session:
    #     tasks_with_assignee = session.scalars(
    #         select(Task.title)
    #         .join(User, Task.assignee_id == User.id)
    #         .order_by(Task.id)
    #     ).all()
    #     tasks_outerjoin = session.scalars(
    #         select(Task.title)
    #         .outerjoin(User, Task.assignee_id == User.id)
    #         .order_by(User.id, Task.id)
    #     ).all()

    #     print(tasks_with_assignee)
    #     print(tasks_outerjoin)

    # with SessionFactory() as session:
    #     task_user = session.execute(
    #         select(User.name, Task.title)
    #         .outerjoin(Task, User.id == Task.assignee_id)
    #         .order_by(User.id, Task.id)
    #     ).all()

    #     for user, task in task_user:
    #         if not task:
    #             print(user, "Нет задач")
    #         else:
    #             print(user, task)

    with SessionFactory() as session:
        user_any_priority = session.scalars(
            select(User.name)
            .where(User.tasks.any(Task.priority >= 4))
        ).all()
        user_any_task = session.scalars(
            select(User.name)
            .where(~User.tasks.any())
        ).all()
        task_has_active = session.scalars(
            select(Task.title)
            .where(Task.assignee.has(User.is_active.is_(True)))
        ).all()
        task_has_active_join = session.scalars(
            select(Task.title)
            .join(Task.assignee)
            .where(User.is_active.is_(True))
        ).all()

        print(user_any_priority)
        print(user_any_task)
        print(task_has_active)
        print(task_has_active_join)


if __name__ == "__main__":
    main()
