from .database import engine, metadata


def main():
    print(metadata.tables.keys())
    metadata.create_all(engine)


if __name__ == '__main__':
    main()
