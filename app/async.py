import asyncio

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from .database import AsyncSessionFactory, async_engine
from .models import User, Tag, Task, Project, Profile


async def get_active_users() -> list[User]:
    req = (select(User)
           .where(User.is_active.is_(True))
           .order_by(User.id))
    async with AsyncSessionFactory() as session:
        res = await session.execute(req)
        users = res.scalars().all()
        return list(users)


async def create_user(user: User) -> int:

    async with AsyncSessionFactory.begin() as session:
        session.add(user)
        print(user.id)
        await session.flush()
        user_id = user.id
        print(user_id)
        return user_id


async def get_projects_with_owners() -> list[Project]:
    req = (select(Project)
           .options(
               joinedload(Project.owner)
           )
           .order_by(Project.id))

    async with AsyncSessionFactory() as session:
        res = await session.execute(req)
        projects = res.scalars().all()
        return list(projects)


async def get_users_with_projects() -> list[User]:
    req = (select(User)
           .options(
               selectinload(User.projects)
           )
           .order_by(User.id))

    async with AsyncSessionFactory() as session:
        res = await session.execute(req)
        users = res.scalars().all()
        return list(users)


async def get_tasks_with_tags() -> list[Task]:
    req = (select(Task)
           .options(
               selectinload(Task.tags)
           )
           .order_by(Task.id))

    async with AsyncSessionFactory() as session:
        res = await session.execute(req)
        tasks = res.scalars().all()
        return list(tasks)


async def main():
    # async with AsyncSessionFactory.begin() as session:
    #     users = [
    #         User(
    #             name='Анна',
    #             email='async_anna@example.com',
    #             is_active=True,
    #             projects=[
    #                 Project(
    #                     name='API Service'
    #                 ),
    #                 Project(
    #                     name='CRM System'
    #                 )
    #             ]
    #         ),
    #         User(
    #             name='Павел',
    #             email='async_pavel@example.com',
    #             is_active=False,
    #             projects=[
    #                 Project(
    #                     name='Analytics'
    #                 )
    #             ]
    #         ),
    #         User(
    #             name='Мария',
    #             email='async_maria@example.com',
    #             is_active=True
    #         )
    #     ]

    #     tasks = [
    #         Task(
    #             title='Изучить AsyncSession',
    #             priority=5,
    #             tags=[
    #                 Tag(
    #                     name='SQLAlchemy',
    #                     category='Async'
    #                 )
    #             ]
    #         ),
    #         Task(
    #             title='Настроить asyncpg',
    #             priority=5,
    #             tags=[
    #                 Tag(
    #                     name='PostgreSQL',
    #                     category='Async'
    #                 )
    #             ]
    #         ),
    #         Task(
    #             title='Написать документацию',
    #             priority=3
    #         )
    #     ]

    #     session.add_all(users + tasks)

    # async with AsyncSessionFactory() as session:
    #     await session.execute(select(1))
    #     print(type(AsyncSessionFactory).__name__)

    # try:
    #     active_users = await get_active_users()
    #     for user in active_users:
    #         print(user.name)
    #     print(len(active_users))
    #     print(all(isinstance(user, User) for user in active_users))
    # finally:
    #     await async_engine.dispose()

    # try:
    #     elena = User(
    #         name='Елена',
    #         email='async_elena@example.com',
    #         is_active=True
    #     )
    #     elena_id = await create_user(elena)
    #     async with AsyncSessionFactory() as session:
    #         elena = await session.get(User, elena_id)
    #         if elena:
    #             print(elena.name)
    #             print(elena.email)
    #             print(elena.is_active)
    # finally:
    #     await async_engine.dispose()

    # try:
    #     projects = await get_projects_with_owners()
    #     for project in projects:
    #         if project.owner:
    #             print(f'{project.name} | {project.owner.name}')
    #     print(len(projects))
    # finally:
    #     await async_engine.dispose()

    try:
        users = await get_users_with_projects()
        for user in users:
            if user.projects:
                for project in user.projects:
                    print(f'{user.name} | {project.name}')
            else:
                print(f'{user.name} | нет проектов')

        tasks = await get_tasks_with_tags()
        for task in tasks:
            if task.tags:
                for tag in task.tags:
                    print(f'{task.title} | {tag.name}')
            else:
                print(f'{task.title} | тегов нет')
    finally:
        await async_engine.dispose()


if __name__ == '__main__':
    asyncio.run(main())
