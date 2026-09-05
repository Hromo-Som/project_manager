import sqlite3

from sqlalchemy import create_engine, event

from .config import DATABASE_URL, SQL_ECHO


engine = create_engine(DATABASE_URL, echo=SQL_ECHO)


@event.listens_for(engine, "connect")
def set_sqlite_pragma_for_engine(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
