from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)

from .config import ASYNC_DATABASE_URL, SQL_ECHO

async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=SQL_ECHO,
    hide_parameters=True,
    )

AsyncSessionFactory = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
