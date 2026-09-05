from sqlalchemy.orm import sessionmaker

from . import engine


SessionFactory = sessionmaker(engine)  # type: ignore[call-overload]

SessionNoExpire = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)  # type: ignore[call-overload]
