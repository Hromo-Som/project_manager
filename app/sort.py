from sqlalchemy import asc, desc, func, select

from .database import SessionFactory
from .models import Task


def main():
    # with SessionFactory.begin() as session:
    #     tasks = [
    #         Task(
    #             title="Настроить проект",
    #             is_completed=False,
    #             priority=5
    #         ),
    #         Task(
    #             title="Изучить SELECT",
    #             is_completed=True,
    #             priority=4
    #         ),
    #         Task(
    #             title="Написать тесты",
    #             is_completed=False,
    #             priority=3
    #         ),
    #         Task(
    #             title="Исправить баг",
    #             is_completed=False,
    #             priority=5
    #         ),
    #         Task(
    #             title="Обновить README",
    #             is_completed=True,
    #             priority=2
    #         ),
    #         Task(
    #             title="Проверить миграции",
    #             is_completed=False,
    #             priority=4
    #         ),
    #         Task(
    #             title="Создать отчёт",
    #             is_completed=True,
    #             priority=3
    #         ),
    #         Task(
    #             title="Рефакторинг",
    #             is_completed=False,
    #             priority=2
    #         ),
    #         Task(
    #             title="Удалить черновик",
    #             is_completed=True,
    #             priority=1
    #         ),
    #         Task(
    #             title="Подготовить релиз",
    #             is_completed=False,
    #             priority=5
    #         )
    #     ]

    #     session.add_all(tasks)

    # with SessionFactory() as session:
    #     t_priority_up = session.scalars(
    #         select(Task.title)
    #         .order_by(Task.priority, Task.id)
    #     ).all()
    #     t_priority_down = session.scalars(
    #         select(Task.title)
    #         .order_by(-Task.priority, Task.id)
    #     ).all()
    #     t_p_down = session.scalars(
    #         select(Task.title)
    #         .order_by(desc(Task.priority), Task.id)
    #     ).all()
    #     t_p_d = session.scalars(
    #         select(Task.title)
    #         .order_by(Task.priority.desc(), Task.id)
    #     ).all()

    #     print(t_priority_up)
    #     print("-----------")
    #     print(t_priority_down)
    #     print("-----------")
    #     print(t_p_down)
    #     print("-----------")
    #     print(t_p_d)

    # with SessionFactory() as session:
    #     t_page_1 = session.scalars(
    #         select(Task.title)
    #         .order_by(Task.id)
    #         .offset(0)
    #         .limit(4)
    #     ).all()
    #     t_page_2 = session.scalars(
    #         select(Task.title)
    #         .order_by(Task.id)
    #         .offset(4)
    #         .limit(4)
    #     ).all()
    #     t_page_3 = session.scalars(
    #         select(Task.title)
    #         .order_by(Task.id)
    #         .offset(8)
    #         .limit(4)
    #     ).all()
    #     t_page_4 = session.scalars(
    #         select(Task.title)
    #         .order_by(Task.id)
    #         .offset(12)
    #         .limit(4)
    #     ).all()

    #     print(t_page_1)
    #     print("-----------")
    #     print(t_page_2)
    #     print("-----------")
    #     print(t_page_3)
    #     print("-----------")
    #     print(t_page_4)

    # with SessionFactory() as session:
    #     t_uncompl_1 = session.scalars(
    #         select(Task.title)
    #         .where(Task.is_completed.is_(False))
    #         .order_by(Task.priority.desc(), Task.id)
    #         .offset(0)
    #         .limit(2)
    #     ).all()
    #     t_uncompl_2 = session.scalars(
    #         select(Task.title)
    #         .where(Task.is_completed.is_(False))
    #         .order_by(Task.priority.desc(), Task.id)
    #         .offset(2)
    #         .limit(2)
    #     ).all()
    #     t_uncompl_3 = session.scalars(
    #         select(Task.title)
    #         .where(Task.is_completed.is_(False))
    #         .order_by(Task.priority.desc(), Task.id)
    #         .offset(4)
    #         .limit(2)
    #     ).all()

    #     print(t_uncompl_1)
    #     print("-----------")
    #     print(t_uncompl_2)
    #     print("-----------")
    #     print(t_uncompl_3)

    # with SessionFactory() as session:
    #     t_count = session.scalars(
    #         select(func.count(Task.id))
    #     ).all()
    #     t_uncompl_count = session.scalars(
    #         select(func.count(Task.id))
    #         .where(Task.is_completed.is_(False))
    #     ).all()
    #     t_priority_sum = session.scalars(
    #         select(func.sum(Task.priority))
    #     ).all()
    #     t_uncompl_sum = session.scalars(
    #         select(func.sum(Task.priority))
    #         .where(Task.is_completed.is_(False))
    #     ).all()

    #     print(t_count)
    #     print("-----------")
    #     print(t_uncompl_count)
    #     print("-----------")
    #     print(t_priority_sum)
    #     print("-----------")
    #     print(t_uncompl_sum)

    with SessionFactory() as session:
        group_by_status = session.execute(
            select(
                Task.is_completed,
                func.count(Task.id),
                func.sum(Task.priority)
            )
            .group_by(Task.is_completed)
            .order_by(Task.is_completed)
        ).all()
        group_by_priority = session.execute(
            select(
                Task.priority,
                func.count(Task.id)
            )
            .group_by(Task.priority)
            .order_by(func.count(Task.id).desc(), Task.priority)
        ).all()

        print(group_by_status)
        print("-----------")
        print(group_by_priority)


if __name__ == "__main__":
    main()
