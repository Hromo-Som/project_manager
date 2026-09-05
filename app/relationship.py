from sqlalchemy.exc import IntegrityError
from sqlalchemy import delete, select
from sqlalchemy.orm import joinedload, selectinload

from .models import Project, User, Profile, Base, Task, Tag, ProjectMembership
from .models.task_tag import task_tags
from .database import SessionFactory


def main():
    # print(User.projects.property.uselist)
    # print(Project.owner.property.uselist)
    # print(
    #     Project.__table__.c.owner_id.foreign_keys
    # )
    # with SessionFactory.begin() as session:
    #     user = User(
    #         name='Анна',
    #         email='relations_anna@example.com',
    #         is_active=True
    #     )
    #     project1 = Project(
    #         name='SQLAlchemy Course',
    #         owner=user
    #     )
    #     project2 = Project(
    #         name='Task Manager'
    #     )
    #     user.projects.append(project2)
    #     session.add(user)
    #     print(project1.owner is user)
    #     print(project1 in user.projects)
    #     print(project2.owner is user)
    #     print(project2 in user.projects)
    #     print(len(user.projects))
    #     session.flush()
    #     print(user.id is not None)
    #     print(project1.id is not None)
    #     print(project2.id is not None)
    #     print(project1.owner_id == user.id)
    #     print(project2.owner_id == user.id)
    #     user_id = user.id
    #     project1_id = project1.id
    #     project2_id = project2.id

    # with SessionFactory() as session:
    #     user = session.get(User, user_id)
    #     for project in user.projects:
    #         print(project.name)

    # print(User.profile.property.uselist)
    # print(Profile.user.property.uselist)
    # print(
    #     Profile.__table__.c.user_id.unique
    # )
    # print(
    #     Profile.__table__.c.user_id.foreign_keys
    # )

    # with SessionFactory.begin() as session:
    #     user = User(
    #         name='Мария',
    #         email='relations_maria@example.com',
    #         is_active=True
    #     )
    #     profile = Profile(
    #         bio='Backend-разработчик',
    #         timezone='Europe/Moscow'
    #     )

    #     user.profile = profile

    #     session.add(user)
    #     print(user.profile is profile)
    #     print(profile.user is user)
    #     session.flush()
    #     print(user.id is not None)
    #     print(profile.id is not None)
    #     print(profile.user_id == user.id)
    #     user_id = user.id

    # with SessionFactory() as session:
    #     user = session.get(User, user_id)
    #     print(user.profile.bio)
    #     print(user.profile.timezone)
    #     profile = session.get(Profile, 1)
    #     print(profile.user.name)

    # with SessionFactory() as session:
    #     profile = Profile(
    #         bio='Второй профиль',
    #         timezone='UTC',
    #         user_id=6
    #     )

    #     try:
    #         session.add(profile)
    #         session.flush()
    #         session.commit()
    #     except IntegrityError:
    #         session.rollback()

    # with SessionFactory() as session:
    #     user = session.get(User, 6)
    #     print(user.profile.bio)

    # print("task_tags" in Base.metadata.tables)
    # print(list(task_tags.primary_key.columns.keys()))
    # print(Task.tags.property.uselist)
    # print(Tag.tasks.property.uselist)
    # print(Task.tags.property.secondary is task_tags)
    # print(Tag.tasks.property.uselist)

    # with SessionFactory.begin() as session:
    #     task1 = Task(
    #         title='Изучить ORM',
    #         priority=5
    #     )
    #     task2 = Task(
    #         title='Разобрать JOIN',
    #         priority=4
    #     )
    #     tag1 = Tag(
    #         name='SQLAlchemy',
    #         category='technology'
    #     )
    #     tag2 = Tag(
    #         name='ORM',
    #         category='technology'
    #     )
    #     tag3 = Tag(
    #         name='JOIN',
    #         category='sql'
    #     )

    #     task1.tags.append(tag1)
    #     task1.tags.append(tag2)
    #     task2.tags.extend([tag1, tag3])
    #     session.add_all([task1, task2])
    #     print(task1.tags)
    #     print(task2.tags)
    #     print(task1 in tag1.tasks)
    #     print(task2 in tag1.tasks)
    #     print(len(tag1.tasks))
    #     session.flush()
    #     task1_id = task1.id
    #     tag1_id = tag1.id

    # with SessionFactory() as session:
    #     task = session.get(Task, task1_id)
    #     for tag in task.tags:
    #         print(tag.name)

    #     tag = session.get(Tag, tag1_id)
    #     for task in tag.tasks:
    #         print(task.title)

    # with SessionFactory.begin() as session:
    #     task = session.get(Task, 6)
    #     tag = session.get(Tag, 1)
    #     task.tags.remove(tag)
    #     session.flush()

    # print(
    #     list(
    #         ProjectMembership
    #         .__table__
    #         .primary_key
    #         .columns  # type: ignore
    #         .keys()
    #     )
    # )
    # print(User.project_memberships.property.uselist)
    # print(Project.memberships.property.uselist)
    # print(ProjectMembership.user.property.uselist)
    # print(ProjectMembership.project.property.uselist)

    # with SessionFactory.begin() as session:
    #     user_anna = session.get(User, 1)
    #     user_pavel = session.get(User, 3)
    #     user_elena = session.get(User, 4)
    #     project = session.get(Project, 2)

    #     project.owner = user_anna
    #     membership_pavel = ProjectMembership(
    #         user=user_pavel,
    #         project=project,
    #         role='developer'
    #     )
    #     membership_elena = ProjectMembership(
    #         user=user_elena,
    #         project=project,
    #         role='tester'
    #     )
    #     session.add_all([membership_pavel, membership_elena])
    #     session.flush()
    #     print(membership_pavel.user is user_pavel)
    #     print(membership_pavel.project is project)
    #     print(membership_pavel in user_pavel.project_memberships)
    #     print(membership_pavel in project.memberships)
    #     print(membership_elena.user is user_elena)
    #     print(membership_elena.project is project)
    #     print(membership_elena in user_elena.project_memberships)
    #     print(membership_elena in project.memberships)
    #     print(project.memberships)
    #     print(len(project.memberships))
    #     project_id = project.id
    #     pavel_id = user_pavel.id
    #     elena_id = user_elena.id

    # with SessionFactory() as session:
    #     project = session.get(Project, project_id)
    #     for membership in project.memberships:
    #         print(f'{membership.user.name} | {membership.role}')

    #     membership = session.get(
    #         ProjectMembership,
    #         {
    #             'user_id': pavel_id,
    #             'project_id': project_id
    #         }
    #     )
    #     membership.role = 'lead developer'
    #     session.flush()
    #     membership = session.get(
    #         ProjectMembership,
    #         {
    #             'user_id': pavel_id,
    #             'project_id': project_id
    #         }
    #     )
    #     print(membership.role)

    # with SessionFactory() as session:
    #     membership = ProjectMembership(
    #         user_id=pavel_id,
    #         project_id=project_id,
    #         role='observer'
    #     )

    #     try:
    #         session.add(membership)
    #         session.commit()
    #     except IntegrityError:
    #         session.rollback()

    # with SessionFactory.begin() as session:
    #     anna = User(
    #         name='Анна',
    #         email='cascade_nullable_anna@example.com'
    #     )
    #     project1 = session.get(Project, 2)
    #     project2 = Project(
    #         name='CRM System'
    #     )
    #     anna.projects.extend([project1, project2])
    #     session.add(anna)
    #     session.flush()
    #     anna_id = anna.id

    # with SessionFactory() as session:
    #     anna = session.get(User, 7)
    #     session.delete(anna)
    #     session.flush()
    #     session.commit()

    # with SessionFactory.begin() as session:
    #     pavel = User(
    #         name='Павел',
    #         email='cascade_required_pavel@example.com'
    #     )
    #     project1 = Project(
    #         name='API Service'
    #     )
    #     project2 = session.get(Project, 2)
    #     project3 = session.get(Project, 3)
    #     pavel.projects.extend([project1, project2, project3])
    #     session.add(pavel)

    # with SessionFactory() as session:
    #     pavel = session.get(User, 7)

    #     try:
    #         session.delete(pavel)
    #         session.flush()
    #     except IntegrityError:
    #         session.rollback()

    # with SessionFactory.begin() as session:
    #     anna = User(
    #         name='Анна',
    #         email='cascade_nullable_anna@example.com'
    #     )
    #     mary = User(
    #         name='Мария',
    #         email='cascade_nullable_mary@example.com'
    #     )
    #     anna_project1 = Project(
    #         name='Проект Анны 1',
    #         owner=anna
    #     )
    #     anna_project2 = Project(
    #         name='Проект Анны 2',
    #         owner=anna
    #     )
    #     mary_project1 = Project(
    #         name='Проект Марии 1',
    #         owner=mary
    #     )
    #     mary_project2 = Project(
    #         name='Проект Марии 2',
    #         owner=mary
    #     )

    #     session.add_all([anna, mary])

    # with SessionFactory() as session:
    #     anna = session.get(User, 8)
    #     session.delete(anna)
    #     session.commit()

    # with SessionFactory() as session:
    #     mary = session.get(User, 9)
    #     mary_project1 = session.get(Project, 7)
    #     mary.projects.remove(mary_project1)
    #     session.commit()

    # with SessionFactory.begin() as session:
    #     elena = User(
    #         name='Елена',
    #         email='cascade_db_elena@example.com'
    #     )
    #     project1 = Project(
    #         name='Backend'
    #     )
    #     project2 = Project(
    #         name='Frontend'
    #     )
    #     project3 = Project(
    #         name='Documentation'
    #     )

    #     elena.projects.extend([project1, project2, project3])
    #     session.add(elena)

    # with SessionFactory() as session:
    #     session.execute(delete(User).where(User.id == 10))
    #     session.commit()

    # with SessionFactory.begin() as session:
    #     alexey = User(
    #         name='Алексей',
    #         email='cascade_passive_alex@example.com'
    #     )
    #     project1 = Project(
    #         name='Payments'
    #     )
    #     project2 = Project(
    #         name='Notifications'
    #     )
    #     project3 = Project(
    #         name='Analytics'
    #     )

    #     alexey.projects.extend([project1, project2, project3])
    #     session.add(alexey)

    # with SessionFactory() as session:
    #     user = session.get(User, 10)
    #     session.delete(user)
    #     session.commit()

    # with SessionFactory.begin() as session:
    #     anna = User(
    #         name='Анна',
    #         email='anna@example.com',
    #         profile=Profile(
    #             timezone='Europe/Moscow'
    #         ),
    #         projects=[
    #             Project(
    #                 name='API Service'
    #             ),
    #             Project(
    #                 name='CRM System'
    #             )
    #         ]
    #     )
    #     pavel = User(
    #         name='Павел',
    #         email='pavel@example.com',
    #         projects=[
    #             Project(
    #                 name='Analytics'
    #             )
    #         ]
    #     )
    #     mary = User(
    #         name='Мария',
    #         email='mary@example.com',
    #         profile=Profile(
    #             timezone='UTC'
    #         )
    #     )
    #     tag1 = Tag(
    #         name='ORM',
    #         category='SQLAlchemy'
    #     )
    #     tag2 = Tag(
    #         name='JOIN',
    #         category='SQLAlchemy'
    #     )
    #     tasks = [
    #         Task(
    #             title='Изучить ORM',
    #             priority=5,
    #             tags=[tag1, tag2]
    #         ),
    #         Task(
    #             title='Разобрать JOIN',
    #             priority=5,
    #             tags=[tag1, tag2]
    #         ),
    #         Task(
    #             title='Написать документацию',
    #             priority=3
    #         )
    #     ]
    #     session.add_all([anna, pavel, mary] + tasks)

    # with SessionFactory() as session:
    #     users = session.scalars(
    #         select(User)
    #         .order_by(User.id)
    #     ).all()

    #     for user in users:
    #         if user.projects:
    #             for project in user.projects:
    #                 print(f'{user.name} | {project.name}')
    #         else:
    #             print(f'{user.name} | проектов нет')

    # with SessionFactory() as session:
    #     projects = session.scalars(
    #         select(Project)
    #         .options(
    #             joinedload(Project.owner)
    #         )
    #         .order_by(Project.id)
    #     ).all()

    #     for project in projects:
    #         if project.owner:
    #             print(f'{project.name} | {project.owner.name}')

    # with SessionFactory() as session:
    #     users = session.scalars(
    #         select(User)
    #         .options(
    #             joinedload(User.profile)
    #         )
    #         .order_by(User.id)
    #     ).all()

    #     for user in users:
    #         if user.profile:
    #             print(f'{user.name} | {user.profile.timezone}')
    #         else:
    #             print(f'{user.name} | Профиль отсутствует')

    # with SessionFactory() as session:
    #     users = session.scalars(
    #         select(User)
    #         .options(
    #             joinedload(User.projects)
    #         )
    #         .order_by(User.id)
    #     ).unique().all()

    #     for user in users:
    #         if user.projects:
    #             for project in user.projects:
    #                 print(f'{user.name} | {project.name}')
    #         else:
    #             print(f'{user.name} | пустая коллекция')

    # with SessionFactory() as session:
    #     users = session.scalars(
    #         select(User)
    #         .options(
    #             selectinload(User.projects)
    #         )
    #         .order_by(User.id)
    #     ).all()

    #     for user in users:
    #         if user.projects:
    #             for project in user.projects:
    #                 print(f'{user.name} | {project.name}')
    #         else:
    #             print(f'{user.name} | пустая коллекция')

    with SessionFactory() as session:
        tasks = session.scalars(
            select(Task)
            .options(
                selectinload(Task.tags)
            )
            .order_by(Task.id)
        ).all()

        for task in tasks:
            if task.tags:
                for tag in task.tags:
                    print(f'{task.title} | {tag.name} | {tag.category}')
            else:
                print(f'{task.title} | тегов нет')


if __name__ == '__main__':
    main()
