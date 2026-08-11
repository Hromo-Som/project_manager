from sqlalchemy import (
    Column,
    Table,
    Integer,
    String,
    Text,
    ForeignKey,
    Boolean
)

from .metadata import metadata


users_table = Table('users',
                    metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(100), nullable=False),
                    Column('email', String(255), nullable=False))


projects_table = Table('projects',
                       metadata,
                       Column('id', Integer, primary_key=True),
                       Column('name', String(150), nullable=False),
                       Column('description', Text, nullable=True),
                       Column('owner_id',
                              Integer,
                              ForeignKey('users.id'),
                              nullable=False))


tasks_table = Table('tasks',
                    metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String(200), nullable=False),
                    Column('description', Text, nullable=True),
                    Column('is_complited', Boolean, nullable=False),
                    Column('project_id',
                           Integer,
                           ForeignKey('projects.id'),
                           nullable=False),
                    Column('priority', Integer, nullable=False))
