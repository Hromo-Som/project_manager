from sqlalchemy import Connection, text, insert, select, update, delete

from .database import engine, users_table


def email_find(conn: Connection, email: str):
    return conn.execute(
        text(
            """
            SELECT *
            FROM users
            WHERE email = :email"""
        ),
        {'email': email}
    ).first()


# statement = insert(users_table).values(
#             name='Алексей',
#             email='alex@example.com',
#         )

# statement = (
#     update(users_table)
#     .where(users_table.c.email == 'core_pavel@example.com')
#     .values({'name': 'Павел Сергеевич'})
# )

statement = (
    delete(users_table)
    .where(users_table.c.email == 'core_elena@example.com')
)


def main():
    with engine.begin() as connection:
        # result = connection.execute(
        #     text(
        #         """
        #         INSERT INTO users (name, email)
        #         VALUES (:name, :email)""",
        #     ),
        #     [
        #         {'name': 'Анна',
        #          'email': 'lesson22_anna@example.com'},
        #         {'name': 'Павел',
        #          'email': 'lesson22_pavel@example.com'},
        #         {'name': 'Елена',
        #          'email': 'lesson22_elena@example.com'},
        #     ]
        # )
        # print(result.rowcount)

        # res = connection.execute(
        #     text(
        #         """
        #         SELECT *
        #         FROM users"""
        #     )
        # )
        # print(res.all())

        # connection.execute(
        #     text(
        #         """
        #         DELETE
        #         FROM users"""
        #     )
        # )

        # res = connection.execute(
        #     text(
        #         """
        #         SELECT * FROM users"""
        #     )
        # ).first()

        # print(connection.execute(
        #     text(
        #         """
        #         SELECT * FROM users"""
        #     )
        # ).all())

        # if res:
        #     print(res[0])
        #     print(res.name)
        #     print(res._mapping['email'])
        #     print(res)

        # print(connection.execute(
        #     text(
        #         """
        #         SELECT * FROM users WHERE id = 4"""
        #     )
        # ).one_or_none())

        # print(connection.execute(
        #     text(
        #         """
        #         SELECT 1"""
        #     )
        # ).one())

        # print(connection.execute(
        #     text(
        #         """
        #         SELECT COUNT(*) FROM users"""
        #     )
        # ).scalar_one())

        # print(connection.execute(
        #     text(
        #         """
        #         SELECT * FROM users"""
        #     )
        # ).mappings().first())

        # connection.execute(
        #     text(
        #         """
        #         INSERT INTO users (name, email)
        #         VALUES (:name, :email)"""
        #     ),
        #     {'name': 'Безопасный пользователь',
        #      'email': 'safe@example.com'}
        # )

        # print(email_find(connection, 'safe@example.com'))
        # print(email_find(connection, "' OR 1=1 --"))

        res = connection.execute(
            statement
        )

        print(res.rowcount)

        res = connection.execute(
            select(users_table)
            .where(users_table.c.email == 'core_elena@example.com')
        ).one_or_none()

        print(res)

        res2 = connection.execute(
            select(users_table)
        ).all()

        print(res2)


if __name__ == '__main__':
    main()
