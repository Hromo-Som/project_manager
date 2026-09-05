from app.database.session import SessionFactory
from app.models import User


EMAIL = "unit_of_work@example.com"


def main() -> None:
    with SessionFactory() as session:
        user = User(
            name="Черновое имя",
            email=EMAIL,
            is_active=True,
        )

        print("1. Объект создан")
        print("В session.new:", user in session.new)
        print("id:", user.id)
        print()

        session.add(user)

        print("2. Объект добавлен в Session")
        print("В session.new:", user in session.new)
        print("id:", user.id)
        print()

        user.name = "Итоговое имя"

        print("3. Имя изменено до flush")
        print("name:", user.name)
        print()

        session.flush()

        print("4. Выполнен flush")
        print("В session.new:", user in session.new)
        print(
            "В Identity Map:",
            user in session.identity_map.values(),
        )
        print("id:", user.id)
        print()

        user.name = "Обновлённое имя"

        print("5. Постоянный объект изменён")
        print(
            "В session.dirty:",
            user in session.dirty,
        )
        print()

        session.flush()

        print("6. Второй flush")
        print(
            "В session.dirty:",
            user in session.dirty,
        )
        print()

        session.delete(user)

        print("7. Объект помечен на удаление")
        print(
            "В session.deleted:",
            user in session.deleted,
        )
        print()

        session.rollback()

        print("8. Транзакция отменена")


if __name__ == "__main__":
    main()
