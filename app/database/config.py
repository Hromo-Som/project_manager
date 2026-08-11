DATABASE_URL = 'sqlite:///project_manager.db'
DATABASE_URL_PSYCOPG2 = ('postgresql+psycopg2://postgres:postgres'
                         '@localhost:5432/project_manager')
DATABASE_URL_PSYCOPG = ('postgresql+psycopg://postgres:postgres'
                        '@localhost:5432/project_manager')
DATABASE_URL_ASYNCPG = ('postgresql+asyncpg://postgres:postgres'
                        '@localhost:5432/project_manager')
