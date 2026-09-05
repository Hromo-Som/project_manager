import os

from dotenv import load_dotenv

load_dotenv()


def get_bool_env(
        name: str,
        default: bool = False,
) -> bool:
    raw_value = os.getenv(
        name,
        str(default)
    )

    return raw_value.strip().lower() in {
        '1',
        'true',
        'yes',
        'on'
    }


DATABASE_URL = os.environ['DATABASE_URL']
ASYNC_DATABASE_URL = os.environ['ASYNC_DATABASE_URL']

SQL_ECHO = get_bool_env(
    'SQL_ECHO',
    default=False
)
